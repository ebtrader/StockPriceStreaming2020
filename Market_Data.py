from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def error(self, reqId, errorCode, errorString):
        print('Error:', reqId, " ", errorCode, " ", errorString)

    def TickPrice(self, reqId, tickType, price, attrib):
        print("Tick Price. Ticker Id:", reqId, "tickType: ", TickTypeEnum.to_str(tickType), "Price:", price, end='')

    def TickSize(self, reqId, tickType, size):
        print("Tick Size. Ticker Id:", reqId, "tickType: ", TickTypeEnum.to_str(tickType), "Size:", size)

def main():
    app = TestApp()

    app.connect("127.0.0.1", 7497, 0)

    contract = Contract()
    contract.symbol = "ES"
    contract.secType = "FUT"
    contract.exchange = "GLOBEX"
    contract.currency = "USD"
    contract.lastTradeDateOrContractMonth = "202012"

    #app.reqMarketDataType(1)
    app.reqMktData(1001, contract, "", False, False, [])

    app.run()

if __name__ == "__main__":
    main()


