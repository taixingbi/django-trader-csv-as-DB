from stock.module import *
import pandas as pd
from stock.csvSell import *
from stock.csvSellLog import *

cSVSellLog = CSVSellLog()
class TraderSellStock:
    def __init__(self):
        print("TraderSellStock")

    def updateCSV(self):
        df = CSVSell().read()
        print("df", df)
        if len(df)==0: 
            return [], []
        return df['name'].to_list(), df['stopPercentage'].to_list()

    def process(self):
        names, stopPercentages = self.updateCSV()
        print("\n" + getTimeNow() + " sell", "stock: ", names,  stopPercentages)

        cSVSellLog.add(getTimeNow(),  " sell stock: " + ' '.join(names) )

        if not names: return
        for i, name in enumerate(names):
            is_stock_have_share, share_hold = stock_have_share(name)
            print("share:",is_stock_have_share, " quatity:", share_hold)
            if is_stock_have_share:
                stockSelltrailingStop(name, share_hold, stopPercentages[i])
      