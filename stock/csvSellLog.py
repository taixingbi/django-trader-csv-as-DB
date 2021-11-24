import pandas as pd

class CSVSellLog:
    def __init__(self):
        self.PATH_CSV = 'csv/sellLog.csv'
        # self.clean()
        
    def clean(self):
        d = {'time': [], 'log':[]}
        df = pd.DataFrame(data=d)
        df.to_csv(self.PATH_CSV, index=False)

    def add(self, time, log):
        df = pd.read_csv(self.PATH_CSV)
        newRow = {'time': time, 'log': log}
        df = df.append(newRow, ignore_index = True)
        df.to_csv(self.PATH_CSV, index=False)

    def read(self):
        df = pd.read_csv(self.PATH_CSV)
        # if len(df) > 10 :
        df = df[-20:]
        df.to_csv(self.PATH_CSV, index=False)

        log_list = []
        for i in df.index:
            log_list =  [df['time'][i] + " " + df['log'][i] ] + log_list

        return log_list

if __name__ == "__main__":
    # cSVSellLog = CSVSellLog()
    # cSVSellLog.clean()
    # cSVSellLog.add("2021-11-21 18:34:35", "sell stock: QQQ SPY")
    # print(cSVSellLog.read())

    df = pd.read_csv('csv/sellLog.csv')
    print( type( df.time.to_string(index=False)) )
