from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

import pandas as pd


class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        #self.df = pd.DataFrame(columns=['date', 'open', 'high', 'low', 'close', 'volume'])
        self.reqMktData(1013, contract, "", False, False, [])

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    #def historicalData(self, reqId, bar):
    #    print("HistoricalData. ", reqId, " Date:", bar.date, "Open:", bar.open,
    #         "High:", bar.high, "Low:", bar.low, "Close:", bar.close, "Volume:", bar.volume,
    #            "Count:", bar.barCount, "WAP:", bar.average)

    #def historicalData(self, reqId, bar):
    #    self.df.loc[len(self.df)] = [bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume]
    #    self.df.to_csv('stock.csv')

    def tickOptionComputation(self, reqId: TickerId, tickType: TickType, tickAttrib: int,
                              impliedVol: float, delta: float, optPrice: float, pvDividend: float,
                              gamma: float, vega: float, theta: float, undPrice: float):
                              super().tickOptionComputation(reqId, tickType, tickAttrib, impliedVol, delta,
                                      5
        optPrice, pvDividend, gamma, vega, theta, undPrice)

    def start(self):
        contract = Contract()
        contract.symbol = "TQQQ"
        contract.secType = "OPT"
        contract.exchange = "SMART"
        contract.currency = "USD"
        contract.lastTradeDateOrContractMonth = "20201204"
        contract.strike = 150
        contract.right = "C"
        contract.multiplier = "100"


    def main():
        app = TestApp()
        #app.connect("127.0.0.1", 7497, 0)
        app.connect("127.0.0.1", 4002, 0)
        #app.reqHistoricalData(1, contract, "", "1 D", "5 mins", "MIDPOINT", 0, 1, False, [])
        app.run()




if __name__ == "__main__":
    main()

