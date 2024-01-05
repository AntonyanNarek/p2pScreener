import requests
import json


class p2pParse():

    def getBybitPrices(self, type="buy", size="20", token="USDT", currency="RUB"):
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

    def getCommexPrices(self, type="buy", size=20, token="USDT", currency="RUB"):
        dataRequest = {
            "proMerchantAds": False,
            "page": 1,
            "rows": size,
            "payTypes": [],
            "countries": [],
            "publisherType": None,
            "asset": token,
            "fiat": currency,
            "tradeType": "BUY"
        }

        if type == "sell":
            dataRequest['tradeType'] = "SELL"

        result = requests.post("https://www.commex.com/bapi/c2c/v1/friendly/c2c/ad/search", json=dataRequest)
        result = json.loads(result.text)
        currSellData = {}
        resultData = []
        for data in result['data']:
            currSellData['price'] = data['adDetailResp']['price']
            currSellData['currency'] = data['adDetailResp']['fiatCurrency']
            currSellData['minAmount'] = data['adDetailResp']['minSingleTransAmount']
            currSellData['maxAmount'] = data['adDetailResp']['maxSingleTransAmount']
            currSellData['initAmount'] = data['adDetailResp']['remainingAmount']
            currSellData['payments'] = data['adDetailResp']['tradeMethods'][0][
                'tradeMethodName']  # только первый метод оплаты, надо фиксить, чтобы были все
            currSellData['makerOrdersNum'] = data['advertiserVo']['userStatsRet']['completedOrderNum']
            currSellData['makerOrdersRate'] = round(data['advertiserVo']['userStatsRet']['finishRate'], 2)
            resultData.append(currSellData.copy())
        return resultData

    def getKucoinPrices(self, type="buy", size=20, token="USDT", currency="RUB"):
        dataRequest = {
            "status": "PUTUP",
            "currency": token,
            "legal": currency,
            "page": 1,
            "pageSize": size,
            "side": "BUY",
        }

        if type == "sell":
            dataRequest['side'] = "SELL"

        result = requests.get("https://www.kucoin.com/_api/otc/ad/list", params=dataRequest)
        result = json.loads(result.text)
        currSellData = {}
        resultData = []
        for data in result['items']:
            currSellData['price'] = data['premium']
            currSellData['currency'] = data['legal']
            currSellData['minAmount'] = data['limitMinQuote']
            currSellData['maxAmount'] = data['limitMaxQuote']
            currSellData['initAmount'] = data['currencyBalanceQuantity']
            currSellData['payments'] = data['adPayTypes'][0][
                'payTypeCode']  # только первый метод оплаты, надо фиксить, чтобы были все
            currSellData['makerOrdersNum'] = data['dealOrderNum']
            currSellData['makerOrdersRate'] = data['dealOrderRate']
            resultData.append(currSellData.copy())
        return resultData

    def printData(self, resultData):
        for data in resultData:
            print(data['price'], data['currency'], data['minAmount'], 'RUB -', data['maxAmount'], 'RUB', data['initAmount'], 'USDT', data['payments'],
                  data['makerOrdersNum'], 'сделок', data['makerOrdersRate'], 'рейтинг успешных', sep=" ")
