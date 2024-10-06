from datetime import datetime
import aiohttp
import asyncio
from aiohttp.client_exceptions import ContentTypeError

class NSELive:
    time_out = 5
    base_url = "https://www.nseindia.com/api"
    page_url = "https://www.nseindia.com/get-quotes/equity?symbol=LT"
    all_symbols = "https://www.nseindia.com/api/master-quote"
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
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }

    def __init__(self):
        self.session = None

    async def initialize(self):
        self.session = aiohttp.ClientSession(headers=self.headers)
        await self.session.get(self.page_url)

    async def close(self):
        await self.session.close()

    async def get(self, route, payload={}):
        url = self.base_url + self._routes[route]
        try:
            async with self.session.get(url, params=payload) as response:
                response.raise_for_status()
                return await response.json()
        except ContentTypeError as e:
            print(f"Failed to decode JSON for URL {url}: {e}")
            return None
        except Exception as e:
            print(f"Request failed: {e}")
            return None

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
        return await self.get("equity_option_chain", data)

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
        return await self.get("master_quote")

# Usage Example
async def main():
    nse = NSELive()
    await nse.initialize()
    symbols = await nse.get_all_symbols()
    print(symbols)
    await nse.close()

if __name__ == "__main__":
    asyncio.run(main())
