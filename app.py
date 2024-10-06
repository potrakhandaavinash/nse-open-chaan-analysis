#https://github.com/jugaad-py/jugaad-data/blob/master/jugaad_data/nse/live.py
import requests
from aiohttp import web
from connections import NSELive
import process.processdata as process
import aiohttp_cors
from datetime import datetime
import asyncio
from concurrent.futures import ThreadPoolExecutor
from TestV2 import get_all_options
from process.processdata import test

nse=NSELive()

class StartApp(object):
    def __init__(self,app):
        self.app=app
        self.executor = ThreadPoolExecutor(max_workers=20)

    async def broadcom_json(self,request):
        dic={"1":2}
        data=requests.get("https://www.broadcom.com/api/getmetadata?url=&locale=en-us")
        print("1")
        a=dic["1"]
        return web.json_response(data.json())
    async def handle(self,request):
        return web.Response(text="Hello, World!")

    async def api_request(self,request):
        data = nse.live_index()
        return web.json_response(data)

    async def option_an(self,request):
        url_params = request.query
        query = {}
        for key, val in url_params.items():
            query[key] = val
        print(query['symbol'])
        # will make call to nse and bring all the option chain
        data = nse.equities_option_chain(symbol=query['symbol'])
        #print("data",data)
        # it will filter all the option chain list by using OI % change
        filtered_data = await process.test(data)
        # print("data", filtered_data)
        return web.json_response(filtered_data)

    async def thick_data(self,request):
        data = nse.get_all_sybbols()
        # a = await get_all_options()
        # all_options=[]
        # for i in a:
        #     process_data=await test(i)
        #     if process_data and 'data' in process_data and process_data['data']:
        #         if len(process_data['data']) > 5:
        #             all_options.append(process_data)
        # print(len(all_options))
        return web.json_response(data)

    async def process_all_opt(self,request):
        generic_url_start = datetime.now()
        # loop = asyncio.get_event_loop()
        all_options = await process.all_options()

        # all_raw_json = await get_all_options()
        # all_options = {}
        # for i in all_raw_json:
        #     process_data = await test(i)
        #     if process_data and 'data' in process_data and process_data['data']:
        #         if len(process_data['data']) >= 5:
        #             all_options[process_data['data'][0]['underlying']]=process_data


        all_options["timetaken_for_getjson"] = (datetime.now() - generic_url_start).total_seconds()
        return web.json_response(all_options)

    @staticmethod
    def run_coroutine_in_thread(coroutine_func):
        return asyncio.run(coroutine_func())

    async def hc(self,request):
        return web.Response(text="hhhh")



if __name__ == '__main__':
    app = web.Application()
    handler = StartApp(app)
    app.router.add_get('/', handler.handle)
    app.router.add_get('/hc', handler.api_request)
    app.router.add_get('/option', handler.option_an)
    app.router.add_get('/thickdata', handler.thick_data)
    app.router.add_get('/processalloptions', handler.process_all_opt)
    app.router.add_get('/broadcomjson', handler.broadcom_json)
    # Configure default CORS settings.
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
    web.run_app(app)
