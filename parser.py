import requests
import json

class ParseP2P():
    session = requests.Session()
    session.headers.update({
        "User-Agent": "PostmanRuntime/7.28.2",
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "Cache-Control": "no-cache"
    })

    def getBybitPrices(self, type="buy", size="20", token="USDT", currency="RUB", session=session):
        dataRequest = {
            "currencyId": currency,
            "page": "1",
            "side": "1",
            "size": size,
            "tokenId": token
        }
        if type == "sell":
            dataRequest['side'] = "0"

        with open('payListBybit.json') as f:
            payList = json.load(f)


        result = session.post("https://api2.bybit.com/fiat/otc/item/online", json=dataRequest, )
        result = json.loads(result.text)
        currSellData = {}
        resultData = []
        for data in result['result']['items']:
            currSellData['name'] = "Bybit"
            currSellData['nickName'] = data['nickName']
            currSellData['price'] = data['price']
            currSellData['currency'] = data['currencyId']
            currSellData['minAmount'] = data['minAmount']
            currSellData['maxAmount'] = data['maxAmount']
            currSellData['initAmount'] = data['lastQuantity']
            currSellData['payments'] = [payList[i] for i in data['payments']]
            currSellData['makerOrdersNum'] = data['recentOrderNum']
            currSellData['makerOrdersRate'] = data['recentExecuteRate']
            resultData.append(currSellData.copy())
        return resultData

    def getCommexPrices(self, type="buy", size=20, token="USDT", currency="RUB", session=session):
        dataRequest = {
            "page": 1,
            "rows": size,
            "payTypes": [],
            "countries": [],
            "asset": token,
            "fiat": currency,
            "tradeType": type
        }

        if type == "sell":
            dataRequest['tradeType'] = "SELL"

        result = session.post("https://www.commex.com/bapi/c2c/v1/friendly/c2c/ad/search", json=dataRequest)
        result = json.loads(result.text)
        currSellData = {}
        resultData = []
        for data in result['data']:
            currSellData['name'] = "Commex"
            currSellData['nickName'] = data['advertiserVo']['nickName']
            currSellData['price'] = data['adDetailResp']['price']
            currSellData['currency'] = data['adDetailResp']['fiatCurrency']
            currSellData['minAmount'] = data['adDetailResp']['minSingleTransAmount']
            currSellData['maxAmount'] = data['adDetailResp']['maxSingleTransAmount']
            currSellData['initAmount'] = data['adDetailResp']['remainingAmount']
            currSellData['payments'] = [i['tradeMethodName'] for i in data['adDetailResp']['tradeMethods']]
            currSellData['makerOrdersNum'] = data['advertiserVo']['userStatsRet']['completedOrderNum']
            currSellData['makerOrdersRate'] = round(data['advertiserVo']['userStatsRet']['finishRate'], 2)
            resultData.append(currSellData.copy())
        return resultData

    def getKucoinPrices(self, type="buy", size=20, token="USDT", currency="RUB", session=session):
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
            currSellData['name'] = "Kucoin"
            currSellData['nickName'] = data['nickName']
            currSellData['price'] = data['floatPrice']
            currSellData['currency'] = data['legal']
            currSellData['minAmount'] = data['limitMinQuote']
            currSellData['maxAmount'] = data['limitMaxQuote']
            currSellData['initAmount'] = data['currencyBalanceQuantity']
            currSellData['payments'] = [i['payTypeCode'] for i in data['adPayTypes']]
            currSellData['makerOrdersNum'] = data['dealOrderNum']
            currSellData['makerOrdersRate'] = data['dealOrderRate']
            resultData.append(currSellData.copy())
        return resultData

    def getHuobiPrices(self, type="buy", token="USDT", currency="RUB", session=session): # buy и sell реверсивные, тут для мейкера указывается
        if type == "buy":
            type = "sell"
        elif type == "sell":
            type = "buy"
        # Нужен список монет и валют
        coinId = 2
        if token == "BTC":
            coinId = 1
        elif token == "ETH":
            coinId = 3
        data = {
            "coinId": coinId,
            "currency": 11,
            "tradeType": type,
            "currPage": 1,
            "payMethod": 0,
            "acceptOrder": 0,
            "blockType": "general",
            "online": 1,
            "onlyTradable": "false",
            "isFollowed": "false"
        }
        result = session.get("https://www.htx.com/-/x/otc/v1/data/trade-market", params=data)
        result = json.loads(result.text)
        currSellData = {}
        resultData = []
        for data in result['data']:
            currSellData['name'] = "Huobi"
            currSellData['nickName'] = data['userName']
            currSellData['price'] = data['price']
            currSellData['currency'] = "RUB"
            currSellData['minAmount'] = data['minTradeLimit']
            currSellData['maxAmount'] = data['maxTradeLimit']
            currSellData['initAmount'] = data['tradeCount']
            currSellData['payments'] = [i['name'] for i in data['payMethods']]
            currSellData['makerOrdersNum'] = data['tradeMonthTimes']
            currSellData['makerOrdersRate'] = data['orderCompleteRate']
            resultData.append(currSellData.copy())
        return resultData


    def findArbitrage(self):
        def get_data(data):
            return data['price']

        bybitBuy = self.getBybitPrices(type="buy")
        bybitSell = self.getBybitPrices(type="sell")
        commexBuy = self.getCommexPrices(type="buy")
        commexSell = self.getCommexPrices(type="sell")
        kucoinBuy = self.getKucoinPrices(type="sell")
        kucoinSell = self.getKucoinPrices(type="buy")
        huobiBuy = self.getHuobiPrices(type="sell")
        huobiSell = self.getHuobiPrices(type="buy")
        listBuy = list(bybitBuy + commexBuy + kucoinBuy + huobiBuy)
        listSell = list(bybitSell + commexSell + kucoinSell + huobiSell)
        print("BUY")
        self.printData([min(listBuy, key=get_data)])
        print("SELL")
        self.printData([max(listSell, key=get_data)])

    def printData(self, resultData):
        for data in resultData:
            print(data['price'], data['currency'], data['minAmount'], 'RUB -', data['maxAmount'], 'RUB', data['initAmount'], 'USDT', data['payments'],
                  data['makerOrdersNum'], 'сделок', data['makerOrdersRate'], 'рейтинг успешных', sep=" ")
