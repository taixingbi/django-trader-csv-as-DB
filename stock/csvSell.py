import pandas as pd

class CSVSell:
    def __init__(self):
        self.PATH_CSV = 'csv/sellStock.csv'
        # self.clean()
        
    def clean(self):
        d = {'name': [], 'stopPercentage':[]}
        df = pd.DataFrame(data=d)
        df.to_csv(self.PATH_CSV, index=False)

    def add(self, name, stopPercentage):
        df = pd.read_csv(self.PATH_CSV)
        newRow = {'name': name, 'stopPercentage': stopPercentage}
        df = df.append(newRow, ignore_index = True)
        df.to_csv(self.PATH_CSV, index=False)

    def read(self):
        df = pd.read_csv(self.PATH_CSV)
        return df

if __name__ == "__main__":
    print("csvSell")
    cSVSell = CSVSell()
    cSVSell.add("QQQ", 3)