import requests
import json

data = {
    "amount": "",
    "authMaker": False,
    "canTrade": False,
    "currencyId": "RUB",
    "page": "1",
    "payment": [],
    "side": "1",
    "size": "10",
    "tokenId": "USDT",
    "userId": ""
}
result = requests.post("https://api2.bybit.com/fiat/otc/item/online", json=data)
result = json.loads(result.text)
print(result)
print("SELL:")
for data in result['result']['items']:
    price = data['price']
    currency = data['currencyId']
    minAmount = data['minAmount']
    maxAmount = data['maxAmount']
    initAmount = data['lastQuantity']
    tradeMethod = data['payments'][0] # только первый метод оплаты, надо фиксить, чтобы были все
    makerOrdersNum = data['recentOrderNum']
    makerOrdersRate = data['recentExecuteRate']
    print(price, currency, minAmount, 'RUB -', maxAmount, 'RUB', initAmount, 'USDT', tradeMethod, makerOrdersNum, 'сделок', makerOrdersRate, 'рейтинг успешных', sep=" ")

data = {
    "amount": "",
    "authMaker": False,
    "canTrade": False,
    "currencyId": "RUB",
    "page": "1",
    "payment": [],
    "side": "0",
    "size": "10",
    "tokenId": "USDT",
    "userId": ""
}
result = requests.post("https://api2.bybit.com/fiat/otc/item/online", json=data)
result = json.loads(result.text)
print(result)
print("BUY:")
for data in result['result']['items']:
    price = data['price']
    currency = data['currencyId']
    minAmount = data['minAmount']
    maxAmount = data['maxAmount']
    initAmount = data['lastQuantity']
    tradeMethod = data['payments'][0] # только первый метод оплаты, надо фиксить, чтобы были все
    makerOrdersNum = data['recentOrderNum']
    makerOrdersRate = data['recentExecuteRate']
    print(price, currency, minAmount, 'RUB -', maxAmount, 'RUB', initAmount, 'USDT', tradeMethod, makerOrdersNum, 'сделок', makerOrdersRate, 'рейтинг успешных', sep=" ")
