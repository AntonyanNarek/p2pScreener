import requests
import json


class BybitParse():

    def getPrices(self, type="buy", size="20", token="USDT", currency="RUB"):
        dataRequest = {
            "amount": "",
            "authMaker": False,
            "canTrade": False,
            "currencyId": currency,
            "page": "1",
            "payment": [],
            "side": "1",
            "size": size,
            "tokenId": token,
            "userId": ""
        }
        if type == "sell":
            dataRequest['side'] = "0"

        result = requests.post("https://api2.bybit.com/fiat/otc/item/online", json=dataRequest)
        result = json.loads(result.text)
        currSellData = {}
        resultData = []
        for data in result['result']['items']:
            currSellData['price'] = data['price']
            currSellData['currency'] = data['currencyId']
            currSellData['minAmount'] = data['minAmount']
            currSellData['maxAmount'] = data['maxAmount']
            currSellData['initAmount'] = data['lastQuantity']
            currSellData['payments'] = data['payments'][0] # только первый метод оплаты, надо фиксить, чтобы были все
            currSellData['makerOrdersNum'] = data['recentOrderNum']
            currSellData['makerOrdersRate'] = data['recentExecuteRate']
            resultData.append(currSellData.copy())
        return resultData

    def printData(self, resultData):
        for data in resultData:
            print(data['price'], data['currency'], data['minAmount'], 'RUB -', data['maxAmount'], 'RUB', data['initAmount'], 'USDT', data['payments'],
                  data['makerOrdersNum'], 'сделок', data['makerOrdersRate'], 'рейтинг успешных', sep=" ")
