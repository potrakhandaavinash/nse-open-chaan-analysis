from connections import NSELive

nse = NSELive()
async def test(data):
    filtered_strike_data={}
    filtered_strike_data['data'] = []
    if data and 'records' in data and data['records'] and 'data' in data['records'] and data['records']['data']:
        count = 0
        if 'underlyingValue' in data['records'] and data['records']['underlyingValue']:
            filtered_strike_data['underlyingValue'] = data['records']['underlyingValue']
            # print(">>>>>>>>>>>iltered_strike_data['underlyingValue']",filtered_strike_data['underlyingValue'])
        for strike_data in data['records']['data']:
            # print(strike_data)

            temp_dic={}
            if 'PE' in strike_data and 'CE' in strike_data and strike_data['expiryDate']=="29-Aug-2024":
                #if strike_data['PE']['underlying'] or strike_data['CE']['underlying']:
                if round(strike_data['PE']['pchangeinOpenInterest'])>90 or round(strike_data['CE']['pchangeinOpenInterest'])>90:
                # if 20 < round(strike_data['PE']['pchangeinOpenInterest']) < 50 or 25 < round(
                #          strike_data['CE']['pchangeinOpenInterest']) < 50:
                    # Your code here

                    # print("strikePrice",strike_data['strikePrice'])
                    # print("Change in PE",round(strike_data['PE']['pchangeinOpenInterest']),'%',strike_data['PE']['totalBuyQuantity'],strike_data['PE']['totalSellQuantity'])
                    # print("Change in CE", round(strike_data['CE']['pchangeinOpenInterest']),'%',strike_data['CE']['totalBuyQuantity'],strike_data['CE']['totalSellQuantity'])
                    temp_dic['underlying'] = strike_data['PE']['underlying']
                    temp_dic['strikePrice'] = strike_data['strikePrice']
                    temp_dic['expiryDate'] = strike_data['expiryDate']

                    temp_dic['OI_change_PE'] = round(strike_data['PE']['pchangeinOpenInterest'])
                    temp_dic['total_OI_PE'] = strike_data['PE']['openInterest']
                    temp_dic['Buying_PE'] = strike_data['PE']['totalBuyQuantity']
                    temp_dic['Selling_PE'] = strike_data['PE']['totalSellQuantity']

                    temp_dic['OI_change_CE'] = round(strike_data['CE']['pchangeinOpenInterest'])
                    temp_dic['total_OI_CE'] = strike_data['CE']['openInterest']
                    temp_dic['Buying_CE'] = strike_data['CE']['totalBuyQuantity']
                    temp_dic['Selling_CE'] = strike_data['CE']['totalSellQuantity']

                    count=count+1

                    filtered_strike_data['data'].append(temp_dic)

        if filtered_strike_data and 'data' in filtered_strike_data and filtered_strike_data['data']:
            if len(filtered_strike_data['data'])>5:
                print("gagagag",filtered_strike_data['data'][0]['underlying'])
    return filtered_strike_data


async def test_2(data):
    filtered_strike_data={}
    filtered_strike_data['data'] = []
    if data and 'records' in data and data['records'] and 'data' in data['records'] and data['records']['data']:
        count = 0
        if 'underlyingValue' in data['records'] and data['records']['underlyingValue']:
            filtered_strike_data['underlyingValue'] = data['records']['underlyingValue']
        for strike_data in data['records']['data']:
            temp_dic={}
            if 'PE' in strike_data and 'CE' in strike_data and strike_data['expiryDate']=="29-Aug-2024":
                #if strike_data['PE']['underlying'] or strike_data['CE']['underlying']:
                # if round(strike_data['PE']['pchangeinOpenInterest'])>30 or round(strike_data['CE']['pchangeinOpenInterest'])>30:
                # if 20 < round(strike_data['PE']['pchangeinOpenInterest']) < 50 or 25 < round(
                #          strike_data['CE']['pchangeinOpenInterest']) < 50:
                    # Your code here

                    # print("strikePrice",strike_data['strikePrice'])
                    # print("Change in PE",round(strike_data['PE']['pchangeinOpenInterest']),'%',strike_data['PE']['totalBuyQuantity'],strike_data['PE']['totalSellQuantity'])
                    # print("Change in CE", round(strike_data['CE']['pchangeinOpenInterest']),'%',strike_data['CE']['totalBuyQuantity'],strike_data['CE']['totalSellQuantity'])
                temp_dic['underlying'] = strike_data['PE']['underlying']
                temp_dic['strikePrice'] = strike_data['strikePrice']
                temp_dic['expiryDate'] = strike_data['expiryDate']
                temp_dic['OI_change_PE'] = round(strike_data['PE']['pchangeinOpenInterest'])
                temp_dic['total_OI_PE'] = strike_data['PE']['openInterest']
                temp_dic['Buying_PE'] = strike_data['PE']['totalBuyQuantity']
                temp_dic['Selling_PE'] = strike_data['PE']['totalSellQuantity']
                temp_dic['OI_change_CE'] = round(strike_data['CE']['pchangeinOpenInterest'])
                temp_dic['total_OI_CE'] = strike_data['CE']['openInterest']
                temp_dic['Buying_CE'] = strike_data['CE']['totalBuyQuantity']
                temp_dic['Selling_CE'] = strike_data['CE']['totalSellQuantity']
                count=count+1
                filtered_strike_data['data'].append(temp_dic)

        if filtered_strike_data and 'data' in filtered_strike_data and filtered_strike_data['data']:
            if len(filtered_strike_data['data'])>5:
                print("gagagag",filtered_strike_data['data'][0]['underlying'])
    return filtered_strike_data

# async def test(data):
#     filtered_strike_data = {'data': []}
#     records = data.get('records', {})
#
#     if 'underlyingValue' in records:
#         filtered_strike_data['underlyingValue'] = records['underlyingValue']
#
#     for strike_data in records.get('data', []):
#         if strike_data.get('expiryDate') == "25-Jul-2024":
#             pe = strike_data.get('PE', {})
#             ce = strike_data.get('CE', {})
#
#             if round(pe.get('pchangeinOpenInterest', 0)) >= 50 or round(ce.get('pchangeinOpenInterest', 0)) >= 50:
#                 temp_dic = {
#                     'strikePrice': strike_data.get('strikePrice'),
#                     'expiryDate': strike_data.get('expiryDate'),
#                     'PE': round(pe.get('pchangeinOpenInterest', 0)),
#                     'Buying_PE': pe.get('totalBuyQuantity'),
#                     'Selling_PE': pe.get('totalSellQuantity'),
#                     'CE': round(ce.get('pchangeinOpenInterest', 0)),
#                     'Buying_CE': ce.get('totalBuyQuantity'),
#                     'Selling_CE': ce.get('totalSellQuantity')
#                 }
#                 filtered_strike_data['data'].append(temp_dic)
#
#     return filtered_strike_data

#
#Original All_options
async def all_options():
    empty_dic={}
    all_options_list = symbols = [
"AARTIIND",
"ABB",
"ABBOTINDIA",
"ABCAPITAL",
"ABFRL",
"ACC",
"ADANIENT",
"ADANIPORTS",
"ALKEM",
"AMBUJACEM",
"APOLLOHOSP",
"APOLLOTYRE",
"ASHOKLEY",
"ASIANPAINT",
"ASTRAL",
"ATUL",
"AUBANK",
"AUROPHARMA",
"AXISBANK",
"BAJAJ-AUTO",
"BAJAJFINSV",
"BAJFINANCE",
"BALKRISIND",
"BALRAMCHIN",
"BANDHANBNK",
"BANKBARODA",
"BATAINDIA",
"BEL",
"BERGEPAINT",
"BHARATFORG",
"BHARTIARTL",
"BHEL",
"BIOCON",
"BOSCHLTD",
"BPCL",
"BRITANNIA",
"BSOFT",
"CANBK",
"CANFINHOME",
"CHAMBLFERT",
"CHOLAFIN",
"CIPLA",
"COALINDIA",
"COFORGE",
"COLPAL",
"CONCOR",
"COROMANDEL",
"CROMPTON",
"CUB",
"CUMMINSIND",
"DABUR",
"DALBHARAT",
"DEEPAKNTR",
"DIVISLAB",
"DIXON",
"DLF",
"DRREDDY",
"EICHERMOT",
"ESCORTS",
"EXIDEIND",
"FEDERALBNK",
"GAIL",
"GLENMARK",
"GMRINFRA",
"GNFC",
"GODREJCP",
"GODREJPROP",
"GRANULES",
"GRASIM",
"GUJGASLTD",
"HAL",
"HAVELLS",
"HCLTECH",
"HDFCAMC",
"HDFCBANK",
"HDFCLIFE",
"HEROMOTOCO",
"HINDALCO",
"HINDCOPPER",
"HINDPETRO",
"HINDUNILVR",
"ICICIBANK",
"ICICIGI",
"ICICIPRULI",
"IDEA",
"IDFC",
"IDFCFIRSTB",
"IEX",
"IGL",
"INDHOTEL",
"INDIACEM",
"INDIAMART",
"INDIGO",
"INDUSINDBK",
"INDUSTOWER",
"INFY",
"IOC",
"IPCALAB",
"IRCTC",
"ITC",
"JINDALSTEL",
"JKCEMENT",
"JSWSTEEL",
"JUBLFOOD",
"KOTAKBANK",
"LALPATHLAB",
"LAURUSLABS",
"LICHSGFIN",
"LT",
"LTF",
"LTIM",
"LTTS",
"LUPIN",
"M&M",
"M&MFIN",
"MANAPPURAM",
"MARICO",
"MARUTI",
"MCDOWELL-N",
"MCX",
"METROPOLIS",
"MFSL",
"MGL",
"MOTHERSON",
"MPHASIS",
"MRF",
"MUTHOOTFIN",
"NATIONALUM",
"NAUKRI",
"NAVINFLUOR",
"NESTLEIND",
"NMDC",
"NTPC",
"OBEROIRLTY",
"OFSS",
"ONGC",
"PAGEIND",
"PEL",
"PERSISTENT",
"PETRONET",
"PFC",
"PIDILITIND",
"PIIND",
"PNB",
"POLYCAB",
"POWERGRID",
"PVRINOX",
"RAMCOCEM",
"RBLBANK",
"RECLTD",
"RELIANCE",
"SAIL",
"SBICARD",
"SBILIFE",
"SBIN",
"SHREECEM",
"SHRIRAMFIN",
"SIEMENS",
"SRF",
"SUNPHARMA",
"SUNTV",
"SYNGENE",
"TATACHEM",
"TATACOMM",
"TATACONSUM",
"TATAMOTORS",
"TATAPOWER",
"TATASTEEL",
"TCS",
"TECHM",
"TITAN",
"TORNTPHARM",
"TRENT",
"TVSMOTOR",
"UBL",
"ULTRACEMCO",
"UNITDSPR",
"UPL",
"VEDL",
"VOLTAS",
"WIPRO",
"ZYDUSLIFE"
]
    #print("all",all_options_list)
    for item in all_options_list:
        data = nse.equities_option_chain(symbol=item)
        filtered_data = await test(data)
        if filtered_data and 'data' in filtered_data and filtered_data['data']:
            if len(filtered_data['data'])>5:
                empty_dic[item]=filtered_data
    return empty_dic
# async def all_options():
#     nse = NSELive()
#     empty_dic={}
#     all_options_list = nse.get_all_sybbols()
#     print(all_options_list)
#     tasks = {}
#     async with aiohttp.ClientSession() as session:
#         headers1 = {'User-Agent': 'my-app/0.0.1'}
#         session.headers.update(headers1)
#         #await session.get(nse.page_url)
#         for symbol in all_options_list[1:10]:
#             url=nse.base_url+'/option-chain-equities'
#             data = {'symbol': symbol}
#             tasks[symbol] = fetch(session, url,params=data)
#         responses = await asyncio.gather(*tasks)
#     return responses
#
# async def fetch(session, url,params):
#     async with session.get(url, params=params) as response:
#         return await response.json()
#
# async def second_method(symbol):
#     #call the api
#     nse=NSELive()
#     data = nse.equities_option_chain(symbol=symbol)
#     print(data)
#     return 1
    #process the api request


# import asyncio
# import random
# async def all_options():
#     empty_dic = {}
#     all_options_list = nse.get_all_sybbols()
#
#     async def process_symbol(symbol):
#         # Wrap synchronous call in run_in_executor to ensure it doesn't block
#         loop = asyncio.get_event_loop()
#         #symbol=symbol+"&a="+str(random.choice(1,2,3,4))
#         data = await loop.run_in_executor(None, nse.equities_option_chain, symbol)
#         filtered_data = await test(data)
#         if filtered_data and 'data' in filtered_data and filtered_data['data']:
#             if len(filtered_data['data']) > 5:
#                 return symbol, filtered_data
#         return symbol, None
#
#     # Run all symbol processing concurrently with a larger thread pool
#     results = await asyncio.gather(*[process_symbol(symbol) for symbol in all_options_list])
#
#     # Collect results into the dictionary
#     for symbol, filtered_data in results:
#         if filtered_data is not None:
#             empty_dic[symbol] = filtered_data
#
#     return empty_dic

import asyncio
import aiohttp

# url=nse.base_url
# headers1=nse.headers
# routes=nse._routes['equity_option_chain']
# async def fetch_data(session, url,payload={}):
#     async with session.get(url,params=payload) as response:
#         return await response.json()



# async def all_options():
#     result_list = []
#
#     all_options_list = nse.get_all_sybbols()
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for symbol in all_options_list:
#             url=url+routes
#             session.headers.update(headers1)
#             task = fetch_data(session, url,payload={"symbol": symbol})
#             tasks.append(task)
#
#             for task in asyncio.as_completed(tasks):
#                 data = await task
#                 process_and_append_data(data, result_list)


import asyncio
import aiohttp


#
# async def fetch_data(session, url,payload={}):
#     print("url",url)
#     async with session.get(url,params=payload) as response:
#         return await response.json()





# async def all_options():
#     async with aiohttp.ClientSession() as session:
#         headers1 = nse.headers
#         session.headers.update(headers1)
#         await session.get(nse.page_url)
#         url = nse.base_url
#
#         routes = nse._routes['equity_option_chain']
#         results = {}
#         tasks = []
#         all_options_list = nse.get_all_sybbols()
#         url = url + routes
#         session.headers.update(headers1)
#         for symbol in all_options_list[1:10]:
#             task = fetch_data(session, url,payload={'symbol': symbol})
#
#             tasks.append(task)
#
#         # Fetch all data concurrently
#         responses = await asyncio.gather(*tasks)
#
#         # Process and append data
#         for response in responses:
#             print(response)
#             a=await test(response)
#             results[a['data']]=a
#         return results


# Example usage
urls = [
    'https://api.example.com/data1',
    'https://api.example.com/data2',
    # Add more URLs
]


