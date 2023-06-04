from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from ibapi.utils import iswrapper
from ibapi.common import *
from ibapi.contract import *
from ibapi.ticktype import *
# Request IB Data in less than 50 lines of code
class BasicApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def error(self, reqId: TickerId, errorCode:int, errorString:str):
        print('Error:', reqId, " ", errorCode, " ", errorString)

    @iswrapper
    def tickPrice(self, reqId: TickerId, tickType: TickType, price: float, attrib: TickAttrib):
        super().tickPrice(reqId, tickType, price, attrib)
        print("Tick Price. Ticker Id:", reqId, "tickType:", tickType, "Price:", price, "CanAutoExecute:", attrib.canAutoExecute, "PastLimit", attrib.pastLimit)

def main():
  app = BasicApp()
  app.connect("127.0.0.1", 4002, 0)
  contract = Contract()
  contract.symbol = "TQQQ"
  contract.secType = "OPT"
  contract.exchange = "SMART"
  contract.currency = "USD"
  contract.lastTradeDateOrContractMonth = "20201211"
  contract.strike = 169
  contract.right = "C"
  contract.multiplier = "100"
  app.reqMktData(1, contract, "", True, False, [])
  app.run()

if __name__ == '__main__':
  main()
