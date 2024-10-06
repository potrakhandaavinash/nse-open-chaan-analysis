# import aiohttp
# from aiohttp import web
# import asyncio
# import datetime , time
# from connections import NSELive
# import requests
# nse=NSELive()
# class Test(object):
#     def __init__(self,app):
#         self.app=app
#
#     async def hello_world(self,request):
#         print("hello1111111")
#         dict = {1: 2}
#         tasks = {}
#         all_options = nse.get_all_sybbols()
#         print(all_options)
#         async with aiohttp.ClientSession() as session:
#             for i in all_options:
#                 url = "https://www.broadcom.com/api/getjson?url=&locale=en-us&updated_date=2024-07-17T21:55:11.504000Z&type=home&id=blt0904847a2c7150a5_en-us"
#
#                 url=url+"&a="+str(i)
#                 print(url)
#                 tasks[i]=self.fetch(session, url)
#
#             responses = await asyncio.gather(*tasks.values())
#         for i in responses:
#             return web.json_response(i)
#             break
#         return web.json_response(responses)
#
#     async def fetch(self, session, url):
#         async with session.get(url) as response:
#             return await response.text()
#     async def hello_world1(self,request):
#         print("hello2222222")
#         url="https://www.nseindia.com/option-chain"
#         req=requests.get(url)
#         print(req)
#         dict={1:2}
#         return web.json_response(dict)
#
#     async def api_request1(self,request):
#         data = nse.get_all_sybbols()
#         return web.json_response(data)
#
#
#
# if __name__ == '__main__':
#     app = web.Application()
#     handler = Test(app)
#     loop = asyncio.get_event_loop()
#     app.router.add_get('/hc',handler.hello_world)
#     app.router.add_get('/hc1', handler.hello_world1)
#     app.router.add_get('/hc11', handler.api_request1)
#
#     web.run_app(app, port=8082)

"""
    Implements live data fetch functionality
"""
from datetime import datetime
import aiohttp
import asyncio


class NSELive:
    time_out = 5
    base_url = "https://www.nseindia.com/api"
    page_url = "https://www.nseindia.com/get-quotes/equity?symbol=LT"
    _routes = {
        "stock_meta": "/equity-meta-info",
        "stock_quote": "/quote-equity",
        "stock_derivative_quote": "/quote-derivative",
        "market_status": "/marketStatus",
        "chart_data": "/chart-databyindex",
        "market_turnover": "/market-turnover",
        "equity_derivative_turnover": "/equity-stock",
        "all_indices": "/allIndices",
        "live_index": "/equity-stockIndices",
        "index_option_chain": "/option-chain-indices",
        "equity_option_chain": "/option-chain-equities",
        "currency_option_chain": "/option-chain-currency",
        "pre_open_market": "/market-data-pre-open",
        "holiday_list": "/holiday-master?type=trading",
        "master_quote": "/master-quote"
    }

    headers = {
        "Host": "www.nseindia.com",
        "Referer": "https://www.nseindia.com/get-quotes/equity?symbol=SBIN",
        "X-Requested-With": "XMLHttpRequest",
        "pragma": "no-cache",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }

    def __init__(self):
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(headers=self.headers)
        async with self.session.get(self.page_url) as response:
            await response.text()  # Making sure the session is established
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    async def get(self, route, payload={}):
        url = self.base_url + self._routes[route]
        async with self.session.get(url, params=payload) as response:
            return await response.json()

    async def stock_quote(self, symbol):
        data = {"symbol": symbol}
        return await self.get("stock_quote", data)

    async def stock_quote_fno(self, symbol):
        data = {"symbol": symbol}
        return await self.get("stock_derivative_quote", data)

    async def trade_info(self, symbol):
        data = {"symbol": symbol, "section": "trade_info"}
        return await self.get("stock_quote", data)

    async def market_status(self):
        return await self.get("market_status", {})

    async def chart_data(self, symbol, indices=False):
        data = {"index": symbol + "EQN"}
        if indices:
            data["index"] = symbol
            data["indices"] = "true"
        return await self.get("chart_data", data)

    async def tick_data(self, symbol, indices=False):
        return await self.chart_data(symbol, indices)

    async def market_turnover(self):
        return await self.get("market_turnover")

    async def eq_derivative_turnover(self, type="allcontracts"):
        data = {"index": type}
        return await self.get("equity_derivative_turnover", data)

    async def all_indices(self):
        return await self.get("all_indices")

    async def live_index(self, symbol="NIFTY 50"):
        data = {"index": symbol}
        return await self.get("live_index", data)

    async def index_option_chain(self, symbol="NIFTY"):
        data = {"symbol": symbol}
        return await self.get("index_option_chain", data)

    async def equities_option_chain(self, symbol):
        data = {"symbol": symbol}
        a = await self.get("equity_option_chain", data)
        import process.processdata as proc
        b=await proc.test(a)

        return b

    async def equities_unprocessed_option_chain(self, symbol):
        data = {"symbol": symbol}
        a = await self.get("equity_option_chain", data)
        import process.processdata as proc
        b=await proc.test_2(a)

        return b

    async def currency_option_chain(self, symbol="USDINR"):
        data = {"symbol": symbol}
        return await self.get("currency_option_chain", data)

    async def live_fno(self):
        return await self.live_index("SECURITIES IN F&O")

    async def pre_open_market(self, key="NIFTY"):
        data = {"key": key}
        return await self.get("pre_open_market", data)

    async def holiday_list(self):
        return await self.get("holiday_list", {})

    async def get_all_symbols(self):
        data = {"symbol": ""}
        return await self.get("master_quote", data)

    async def get_all_sybbols(self):
        data = {"symbol": ""}
        print("hehhe")
        return self.get("master-quote", data)


async def main():
    async with NSELive() as nse:
        symbol = "SBIN"
        option_chain = await nse.equities_option_chain(symbol)
        print(option_chain)
        all_symbols = await nse.get_all_symbols()
        print(all_symbols)

# Running the coroutine
# asyncio.run(main())
