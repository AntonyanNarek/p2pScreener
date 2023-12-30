import requests
import json

data = {
    "status": "PUTUP",
    "currency": "USDT",
    "legal": "RUB",
    "page": 1,
    "pageSize": 10,
    "side": "SELL",
}
result = requests.get("https://www.kucoin.com/_api/otc/ad/list", params=data)
result = json.loads(result.text)
print("BUY:")
for data in result['items']:
    price = data['premium']
    currency = data['legal']
    minAmount = data['limitMinQuote']
    maxAmount = data['limitMaxQuote']
    initAmount = data['currencyBalanceQuantity']
    tradeMethod = data['adPayTypes'][0]['payTypeCode'] # только первый метод оплаты, надо фиксить, чтобы были все
    makerOrdersNum = data['dealOrderNum']
    makerOrdersRate = data['dealOrderRate']
    print(price, currency, minAmount, 'RUB -', maxAmount, 'RUB', initAmount, 'USDT', tradeMethod, makerOrdersNum, 'сделок', makerOrdersRate, 'рейтинг успешных', sep=" ")

data = {
    "status": "PUTUP",
    "currency": "USDT",
    "legal": "RUB",
    "page": 1,
    "pageSize": 10,
    "side": "BUY",
}
result = requests.get("https://www.kucoin.com/_api/otc/ad/list", params=data)
result = json.loads(result.text)
print("SELL:")
for data in result['items']:
    price = data['premium']
    currency = data['legal']
    minAmount = data['limitMinQuote']
    maxAmount = data['limitMaxQuote']
    initAmount = data['currencyBalanceQuantity']
    tradeMethod = data['adPayTypes'][0]['payTypeCode'] # только первый метод оплаты, надо фиксить, чтобы были все
    makerOrdersNum = data['dealOrderNum']
    makerOrdersRate = data['dealOrderRate']
    print(price, currency, minAmount, 'RUB -', maxAmount, 'RUB', initAmount, 'USDT', tradeMethod, makerOrdersNum, 'сделок', makerOrdersRate, 'рейтинг успешных', sep=" ")

