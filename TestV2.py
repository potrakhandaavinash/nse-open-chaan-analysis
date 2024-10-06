# import aiohttp
# import asyncio
# from aiohttp.client_exceptions import ContentTypeError
# from process.processdata import test
# from process.connections_V2 import NSELive
#
# url = "https://www.nseindia.com/api/option-chain-equities"
# results = []
#
# headers = {
#     "Host": "www.nseindia.com",
#     "Referer": "https://www.nseindia.com/get-quotes/equity?symbol=SBIN",
#     "X-Requested-With": "XMLHttpRequest",
#     "Pragma": "no-cache",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate, br,zstd",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
#     "Cache-Control": "no-cache",
#     "Connection": "keep-alive",
# }
#
#
# async def get_all_symbols(nse):
#     return await nse.get_all_symbols()
#
#
# def chunk_symbols(symbols, chunk_size):
#     for i in range(0, len(symbols), chunk_size):
#         yield symbols[i:i + chunk_size]
#
#
# def get_tasks(session, symbols_chunk):
#     tasks = []
#     for symbol in symbols_chunk:
#         params = {"symbol": symbol}
#         tasks.append(session.get(url=url, params=params))
#     return tasks
#
#
# async def get_all_options():
#     nse = NSELive()
#     await nse.initialize()
#     symbols = await get_all_symbols(nse)
#
#     async with nse.session as session:
#         for symbols_chunk in chunk_symbols(symbols, 100):
#             tasks = get_tasks(session, symbols_chunk)
#             responses = await asyncio.gather(*tasks, return_exceptions=True)
#
#             for response in responses:
#                 if isinstance(response, Exception):
#                     print(f"Error fetching data: {response}")
#                 else:
#                     try:
#                         a = await response.json()
#                         if 'records' in a and \
#                                 'data' in a['records'] and \
#                                 len(a['records']['data']) > 0 and \
#                                 'PE' in a['records']['data'][0] and \
#                                 'underlying' in a['records']['data'][0]['PE']:
#                             print(a['records']['data'][0]['PE']['underlying'])
#                         elif 'records' in a and \
#                                 'data' in a['records'] and \
#                                 len(a['records']['data']) > 0 and \
#                                 'CE' in a['records']['data'][0] and \
#                                 'underlying' in a['records']['data'][0]['CE']:
#                             print(a['records']['data'][0]['CE']['underlying'])
#                         results.append(a)
#                     except ContentTypeError as e:
#                         print(f"Failed to decode JSON for URL {response.url}: {e}")
#
#     await nse.close()
#
#     return results
#
#
# if __name__ == "__main__":
#     asyncio.run(get_all_options())
#
# async def all():
#     a=get_all_options()
#     return a


# process/connections_V2.py

import aiohttp
import asyncio
from aiohttp.client_exceptions import ContentTypeError
from process.processdata import test
from process.connections_V2 import NSELive

# url = "https://www.nseindia.com/api/option-chain-equities"
# results = []
#
# headers = {
#     "Host": "www.nseindia.com",
#     "Referer": "https://www.nseindia.com/get-quotes/equity?symbol=SBIN",
#     "X-Requested-With": "XMLHttpRequest",
#     "Pragma": "no-cache",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate, br,zstd",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
#     "Cache-Control": "no-cache",
#     "Connection": "keep-alive",
# }
#
#
# async def get_all_symbols(nse):
#     return await nse.get_all_symbols()
#
#
# def chunk_symbols(symbols, chunk_size):
#     for i in range(0, len(symbols), chunk_size):
#         yield symbols[i:i + chunk_size]
#
#
# def get_tasks(session, symbols_chunk):
#     tasks = []
#     for symbol in symbols_chunk:
#         params = {"symbol": symbol}
#         tasks.append(session.get(url=url, params=params))
#     return tasks
#

# async def get_all_options():
#     nse = NSELive()
#     await nse.initialize()
#     symbols = [
# "AARTIIND",
# "ABB",
# "ABBOTINDIA",
# "ABCAPITAL",
# "ABFRL",
# "ACC",
# "ADANIENT",
# "ADANIPORTS",
# "ALKEM",
# "AMBUJACEM",
# "APOLLOHOSP",
# "APOLLOTYRE",
# "ASHOKLEY",
# "ASIANPAINT",
# "ASTRAL",
# "ATUL",
# "AUBANK",
# "AUROPHARMA",
# "AXISBANK",
# "BAJAJ-AUTO",
# "BAJAJFINSV",
# "BAJFINANCE",
# "BALKRISIND",
# "BALRAMCHIN",
# "BANDHANBNK",
# "BANKBARODA",
# "BATAINDIA",
# "BEL",
# "BERGEPAINT",
# "BHARATFORG",
# "BHARTIARTL",
# "BHEL",
# "BIOCON",
# "BOSCHLTD",
# "BPCL",
# "BRITANNIA",
# "BSOFT",
# "CANBK",
# "CANFINHOME",
# "CHAMBLFERT",
# "CHOLAFIN",
# "CIPLA",
# "COALINDIA",
# "COFORGE",
# "COLPAL",
# "CONCOR",
# "COROMANDEL",
# "CROMPTON",
# "CUB",
# "CUMMINSIND",
# "DABUR",
# "DALBHARAT",
# "DEEPAKNTR",
# "DIVISLAB",
# "DIXON",
# "DLF",
# "DRREDDY",
# "EICHERMOT",
# "ESCORTS",
# "EXIDEIND",
# "FEDERALBNK",
# "GAIL",
# "GLENMARK",
# "GMRINFRA",
# "GNFC",
# "GODREJCP",
# "GODREJPROP",
# "GRANULES",
# "GRASIM",
# "GUJGASLTD",
# "HAL",
# "HAVELLS",
# "HCLTECH",
# "HDFCAMC",
# "HDFCBANK",
# "HDFCLIFE",
# "HEROMOTOCO",
# "HINDALCO",
# "HINDCOPPER",
# "HINDPETRO",
# "HINDUNILVR",
# "ICICIBANK",
# "ICICIGI",
# "ICICIPRULI",
# "IDEA",
# "IDFC",
# "IDFCFIRSTB",
# "IEX",
# "IGL",
# "INDHOTEL",
# "INDIACEM",
# "INDIAMART",
# "INDIGO",
# "INDUSINDBK",
# "INDUSTOWER",
# "INFY",
# "IOC",
# "IPCALAB",
# "IRCTC",
# "ITC",
# "JINDALSTEL",
# "JKCEMENT",
# "JSWSTEEL",
# "JUBLFOOD",
# "KOTAKBANK",
# "LALPATHLAB",
# "LAURUSLABS",
# "LICHSGFIN",
# "LT",
# "LTF",
# "LTIM",
# "LTTS",
# "LUPIN",
# "M&M",
# "M&MFIN",
# "MANAPPURAM",
# "MARICO",
# "MARUTI",
# "MCDOWELL-N",
# "MCX",
# "METROPOLIS",
# "MFSL",
# "MGL",
# "MOTHERSON",
# "MPHASIS",
# "MRF",
# "MUTHOOTFIN",
# "NATIONALUM",
# "NAUKRI",
# "NAVINFLUOR",
# "NESTLEIND",
# "NMDC",
# "NTPC",
# "OBEROIRLTY",
# "OFSS",
# "ONGC",
# "PAGEIND",
# "PEL",
# "PERSISTENT",
# "PETRONET",
# "PFC",
# "PIDILITIND",
# "PIIND",
# "PNB",
# "POLYCAB",
# "POWERGRID",
# "PVRINOX",
# "RAMCOCEM",
# "RBLBANK",
# "RECLTD",
# "RELIANCE",
# "SAIL",
# "SBICARD",
# "SBILIFE",
# "SBIN",
# "SHREECEM",
# "SHRIRAMFIN",
# "SIEMENS",
# "SRF",
# "SUNPHARMA",
# "SUNTV",
# "SYNGENE",
# "TATACHEM",
# "TATACOMM",
# "TATACONSUM",
# "TATAMOTORS",
# "TATAPOWER",
# "TATASTEEL",
# "TCS",
# "TECHM",
# "TITAN",
# "TORNTPHARM",
# "TRENT",
# "TVSMOTOR",
# "UBL",
# "ULTRACEMCO",
# "UNITDSPR",
# "UPL",
# "VEDL",
# "VOLTAS",
# "WIPRO",
# "ZYDUSLIFE"
# ]#await get_all_symbols(nse)
#     print("Symbols",symbols)
#
#     async with nse.session as session:
#         for symbols_chunk in chunk_symbols(symbols, 100):
#             tasks = get_tasks(session, symbols_chunk)
#             responses = await asyncio.gather(*tasks, return_exceptions=True)
#
#             for response in responses:
#                 if isinstance(response, Exception):
#                     print(f"Error fetching data: {response}")
#                 else:
#                     try:
#                         a = await response.json()
#                         if 'records' in a and \
#                                 'data' in a['records'] and \
#                                 len(a['records']['data']) > 0 and \
#                                 'PE' in a['records']['data'][0] and \
#                                 'underlying' in a['records']['data'][0]['PE']:
#                             pass
#                             #print(a['records']['data'][0]['PE']['underlying'])
#                         elif 'records' in a and \
#                                 'data' in a['records'] and \
#                                 len(a['records']['data']) > 0 and \
#                                 'CE' in a['records']['data'][0] and \
#                                 'underlying' in a['records']['data'][0]['CE']:
#                             pass
#                             #print(a['records']['data'][0]['CE']['underlying'])
#                         results.append(a)
#                     except ContentTypeError as e:
#                         print(f"Failed to decode JSON for URL {response.url}: {e}")
#
#     await nse.close()
#     return results
#
#
# if __name__ == "__main__":
#     asyncio.run(get_all_options())
#     print(len(results))
#



import asyncio
from aiohttp import web
from concurrent.futures import ThreadPoolExecutor

class App1(object):
    def __init__(self, app):
        self.app = app
        self.executor = ThreadPoolExecutor(max_workers=100)
    def hello(self,request):

        dic={"hello":1}
        return web.json_response(dic)


if __name__ == '__main__':
    app = web.Application()
    web_app = App1(app)
    app.router.add_get('/', web_app.hello)
    web.run_app(app, port=8082)

