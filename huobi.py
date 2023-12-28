import requests
import json

data = {
    "coinId": 2,
    "currency": 11,
    "tradeType": "sell",
    "currPage": 1,
    "payMethod": 0,
    "acceptOrder": 0,
    "blockType": "general",
    "online": 1,
    "onlyTradable": "false",
    "isFollowed": "false"
}
result = requests.get("https://www.htx.com/-/x/otc/v1/data/trade-market", params=data)
result = json.loads(result.text)
print("BUY:")
for data in result['data']:
    price = data['price']
    currency = "RUB"
    minAmount = data['minTradeLimit']
    maxAmount = data['maxTradeLimit']
    initAmount = data['tradeCount']
    tradeMethod = data['payMethods'][0]['name'] # только первый метод оплаты, надо фиксить, чтобы были все
    makerOrdersNum = data['tradeMonthTimes']
    makerOrdersRate = data['orderCompleteRate']
    print(price, currency, minAmount, 'RUB -', maxAmount, 'RUB', initAmount, 'USDT', tradeMethod, makerOrdersNum, 'сделок', makerOrdersRate, 'рейтинг успешных', sep=" ")


data = {
    "coinId": 2,
    "currency": 11,
    "tradeType": "buy",
    "currPage": 1,
    "payMethod": 0,
    "acceptOrder": 0,
    "blockType": "general",
    "online": 1,
    "onlyTradable": "false",
    "isFollowed": "false"
}
result = requests.get("https://www.htx.com/-/x/otc/v1/data/trade-market", params=data)
result = json.loads(result.text)
print("SELL:")
for data in result['data']:
    price = data['price']
    currency = "RUB"
    minAmount = data['minTradeLimit']
    maxAmount = data['maxTradeLimit']
    initAmount = data['tradeCount']
    tradeMethod = data['payMethods'][0]['name'] # только первый метод оплаты, надо фиксить, чтобы были все
    makerOrdersNum = data['tradeMonthTimes']
    makerOrdersRate = data['orderCompleteRate']
    print(price, currency, minAmount, 'RUB -', maxAmount, 'RUB', initAmount, 'USDT', tradeMethod, makerOrdersNum, 'сделок', makerOrdersRate, 'рейтинг успешных', sep=" ")
