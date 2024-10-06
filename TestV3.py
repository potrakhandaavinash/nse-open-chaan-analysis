import aiohttp
import asyncio
from aiohttp import web
from concurrent.futures import ThreadPoolExecutor
from test import NSELive
import aiohttp_cors
from datetime import datetime
import process.readandwritejson as rw
import json
class App1(object):
    def __init__(self, app):
        self.app = app
        self.executor = ThreadPoolExecutor(max_workers=100)

    async def pass1(self, request):
        print("Processing request...")
        generic_url_start = datetime.now()
        async with NSELive() as nse:
            symbol = "ABB"
            option_chain = await nse.equities_option_chain(symbol)
            all_symbols = await nse.get_all_symbols()
            print(all_symbols)

            # tasks = [nse.equities_option_chain(symbol) for symbol in all_symbols]
            # responses = await asyncio.gather(*tasks, return_exceptions=True)

            tasks = {symbol: nse.equities_option_chain(symbol) for symbol in all_symbols}
            responses = await asyncio.gather(*tasks.values(), return_exceptions=True)
            responses_dict = {symbol: response for symbol, response in zip(tasks.keys(), responses)}
            res={}
            res1=[]
            for i in responses_dict:
                # print(i)
                if isinstance(responses_dict[i], dict) and 'data' in responses_dict[i] and len(responses_dict[i]['data']) > 5:
                    # print(i)
                    res[i]=responses_dict[i]
                    res1.append(i)
        res["timetaken_for_getjson"] = (datetime.now() - generic_url_start).total_seconds()
        rw.write_res(res1)
        # print(res1)
        return web.json_response(res)

    async def getsymbol(self,request):
        url_params = request.query
        query = {}
        for key, val in url_params.items():
            query[key] = val
        print(query['symbol'])
        symbol=query['symbol']
        async with NSELive() as nse:
            # symbol = "SBIN"
            option_chain = await nse.equities_unprocessed_option_chain(symbol)

        return web.json_response(option_chain)

    async def pass2(self, request):
        dic = {1: 2}
        return web.json_response(dic)

    async def get_datajson(self,request):
        with open('process/data.json', 'r') as json_file:
            data = json.load(json_file)
        return web.json_response(data)

if __name__ == '__main__':
    app = web.Application()
    web_app = App1(app)
    app.router.add_get('/hc', web_app.pass1)
    app.router.add_get('/', web_app.pass2)
    app.router.add_get('/symbol', web_app.getsymbol)
    app.router.add_get('/datajson', web_app.get_datajson)


    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    # Apply CORS to all routes.
    for route in list(app.router.routes()):
        cors.add(route)
    web.run_app(app, port=8082)
