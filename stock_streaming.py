from ibapi import contract
from ibapi.client import EClient
from ibapi.common import *
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ContractSamples import ContractSamples


class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.started = False
        self.done = False
        print("You have initialized the client")

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)



    # ! [tickbytickalllast]

    def tickByTickAllLast(self, reqId: int, tickType: int, time: int, price: float,
                          size: int, tickAtrribLast: TickAttribLast, exchange: str,
                          specialConditions: str):
        super().tickByTickAllLast(reqId, tickType, time, price, size, tickAtrribLast,
                                  exchange, specialConditions)

        if tickType == 1:
            print("Last.", end='')
        else:
            print("AllLast.", end='')
        print(" ReqId:", reqId,
              "Time:", datetime.datetime.fromtimestamp(time).strftime("%Y%m%d %H:%M:%S"),
              "Price:", price, "Size:", size, "Exch:", exchange,
              "Spec Cond:", specialConditions, "PastLimit:", tickAtrribLast.pastLimit, "Unreported:",
              tickAtrribLast.unreported)

    # ! [tickbytickalllast]

    def start(self):
        contract = Contract()
        contract.symbol = "ES"
        contract.secType = "FUT"
        contract.exchange = "GLOBEX"
        contract.currency = "USD"
        contract.lastTradeDateOrContractMonth = "202101"
        self.reqTickByTickData(19004, ContractSamples.EurGbpFx(), "MidPoint", 0, False)



def main():
    app = TestApp()
    app.connect("127.0.0.1", 7497, 0)
    # app.connect("127.0.0.1", 4002, 0)

    app.run()


if __name__ == "__main__":
    main()
