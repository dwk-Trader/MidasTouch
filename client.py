from ibapi.client import EClient
import time
import pandas as pd

TRADE_BAR_PROPERTIES = ["time", "open", "high", "low", "close", "volume"]

class IBClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)
        
    def get_historical_data(self, request_id, contract, duration, bar_size):
        self.reqHistoricalData(reqId=request_id,
                               contract=contract,
                               endDateTime="",
                               durationStr=duration,
                               barSizeSetting=bar_size,
                               whatToShow="MIDPOINT",
                               useRTH=1,
                               formatDate=1,
                               keepUpToDate=False,
                               chartOptions=[],
        )
        time.sleep(5)
        bar_sizes = ["day", "D", "week", "W", "month"]
        if any(x in bar_size for x in bar_sizes):
            fmt = "Y%Y%m%d"
        else:
            fmt = "%Y%m%d %H:%M:%S %Z"
        data = self.reqHistoricalData[request_id]
        df = pd.DataFrame(data, columns=TRADE_BAR_PROPERTIES)
        df.set_index(pd.to_datetime(df.time, format=fmt), inplace=True)
        df.drop("time", axis=1, inplace=True)
        

