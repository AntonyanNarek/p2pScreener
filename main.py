from fastapi import FastAPI
from parser import ParseP2P
import uvicorn

app = FastAPI()

parser = ParseP2P()

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
