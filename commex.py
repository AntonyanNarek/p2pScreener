import requests
import json

data = {
    "proMerchantAds": False,
    "page": 1,
    "rows": 20,
    "payTypes": [],
    "countries": [],
    "publisherType": None,
    "asset": "USDT",
    "fiat": "RUB",
    "tradeType": "SELL"
}
result = requests.post("https://www.commex.com/bapi/c2c/v1/friendly/c2c/ad/search", json=data)
result = json.loads(result.text)
print("SELL:")
for data in result['data']:
    price = data['adDetailResp']['price']
    currency = data['adDetailResp']['fiatCurrency']
    minAmount = data['adDetailResp']['minSingleTransAmount']
    maxAmount = data['adDetailResp']['maxSingleTransAmount']
    initAmount = data['adDetailResp']['remainingAmount']
    tradeMethod = data['adDetailResp']['tradeMethods'][0]['tradeMethodName'] # только первый метод оплаты, надо фиксить, чтобы были все
    makerOrdersNum = data['advertiserVo']['userStatsRet']['completedOrderNum']
    makerOrdersRate = round(data['advertiserVo']['userStatsRet']['finishRate'], 2)
    print(price, currency, minAmount, 'RUB -', maxAmount, 'RUB', initAmount, 'USDT', tradeMethod, makerOrdersNum, 'сделок', makerOrdersRate, 'рейтинг успешных', sep=" ")


data = {
    "proMerchantAds": False,
    "page": 1,
    "rows": 20,
    "payTypes": [],
    "countries": [],
    "publisherType": None,
    "asset": "USDT",
    "fiat": "RUB",
    "tradeType": "BUY"
}
result = requests.post("https://www.commex.com/bapi/c2c/v1/friendly/c2c/ad/search", json=data)
result = json.loads(result.text)
print("BUY:")
for data in result['data']:
    price = data['adDetailResp']['price']
    currency = data['adDetailResp']['fiatCurrency']
    minAmount = data['adDetailResp']['minSingleTransAmount']
    maxAmount = data['adDetailResp']['maxSingleTransAmount']
    initAmount = data['adDetailResp']['remainingAmount']
    tradeMethod = data['adDetailResp']['tradeMethods'][0]['tradeMethodName'] # только первый метод оплаты, надо фиксить, чтобы были все
    makerOrdersNum = data['advertiserVo']['userStatsRet']['completedOrderNum']
    makerOrdersRate = round(data['advertiserVo']['userStatsRet']['finishRate'], 2)
    print(price, currency, minAmount, 'RUB -', maxAmount, 'RUB', initAmount, 'USDT', tradeMethod, makerOrdersNum, 'сделок', makerOrdersRate, 'рейтинг успешных', sep=" ")
