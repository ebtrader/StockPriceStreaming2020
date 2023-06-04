from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

import pandas as pd

stock_symbol = 'IBM'
class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.df = pd.DataFrame(columns=['ticker','date', 'open', 'high', 'low', 'close', 'volume'])

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    #def historicalData(self, reqId, bar):
    #    print("HistoricalData. ", reqId, " Date:", bar.date, "Open:", bar.open,
    #         "High:", bar.high, "Low:", bar.low, "Close:", bar.close, "Volume:", bar.volume,
    #            "Count:", bar.barCount, "WAP:", bar.average)

    def historicalData(self, reqId, bar):
        self.df.loc[len(self.df)] = [stock_symbol, bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume]
        self.df.to_csv('ticker.csv')

def main():
    app = TestApp()
    #app.connect("127.0.0.1", 7497, 0)
    app.connect("127.0.0.1", 4002, 0)
    contract = Contract()
    contract.symbol = stock_symbol
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"

    app.reqHistoricalData(1, contract, "", "1 D", "5 mins", "MIDPOINT", 0, 1, False, [])
    app.run()




if __name__ == "__main__":
    main()

