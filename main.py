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

    # Объединяем результаты в один словарь
    # Создаем словари для "buy" и "sell"
    buy_data = await get_market_data("buy", request.currency, request.coin)
    sell_data = await get_market_data("sell", request.currency, request.coin)

    # Объединяем результаты в один словарь
    market_data = {
        "buy": buy_data,
        "sell": sell_data
    }

    return market_data

# Функция для асинхронного получения данных с биржи
async def get_market_data(type, currency, coin):
    data = {}
    data['Huobi'] = parser.getHuobiPrices(type=type, currency=currency, token=coin)
    data['Bybit'] = parser.getBybitPrices(type=type, currency=currency, token=coin)
    data['Kucoin'] = parser.getKucoinPrices(type=type, currency=currency, token=coin)
    data['Commex'] = parser.getCommexPrices(type=type, currency=currency, token=coin)
    return data
