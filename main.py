import asyncio
from typing import List

from fastapi import FastAPI
from parser import ParseP2P
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

parser = ParseP2P()

class Request(BaseModel):
    currency: str
    coin: str
    market: List[str]

@app.get("/orderbook/huobi")
async def huobi():
    return parser.getHuobiPrices()

@app.get("/orderbook/bybit")
async def bybit():
    return parser.getBybitPrices()

@app.get("/orderbook/kucoin")
async def kucoin():
    return parser.getKucoinPrices()

@app.get("/orderbook/commex")
async def commex():
    return parser.getCommexPrices()

@app.post("/orders/filter")
async def filter(request: Request):
    markets = request.market

    if not markets or not isinstance(markets, list):
        raise HTTPException(status_code=400, detail="Market should be a list")

    # Создаем асинхронные задачи для "buy" и "sell"
    buy_tasks = [get_market_data(market, "buy", request.currency, request.coin) for market in markets]
    sell_tasks = [get_market_data(market, "sell", request.currency, request.coin) for market in markets]

    # Выполняем задачи асинхронно
    buy_results = await asyncio.gather(*buy_tasks)
    sell_results = await asyncio.gather(*sell_tasks)

    # Объединяем результаты в один словарь
    # Создаем словари для "buy" и "sell"
    buy_data = {market.lower(): result for market, result in zip(markets, buy_results)}
    sell_data = {market.lower(): result for market, result in zip(markets, sell_results)}

    # Объединяем результаты в один словарь
    market_data = {
        "buy": buy_data,
        "sell": sell_data
    }

    return market_data

# Функция для асинхронного получения данных с биржи
async def get_market_data(market_name, type, currency, coin):
    if market_name.lower() == 'huobi':
        return  parser.getHuobiPrices(type=type, currency=currency, token=coin)
    elif market_name.lower() == 'bybit':
        return  parser.getBybitPrices(type=type, currency=currency, token=coin)
    elif market_name.lower() == 'kucoin':
        return  parser.getKucoinPrices(type=type, currency=currency, token=coin)
    elif market_name.lower() == 'commex':
        return  parser.getCommexPrices(type=type, currency=currency, token=coin)
    else:
        return f"Market '{market_name}' not found"