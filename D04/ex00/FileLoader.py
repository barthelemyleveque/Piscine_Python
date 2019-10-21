import pandas as pd

class FileLoader:
    def load(self, path):
        data = pd.read_csv(path)
        print("Loading dataset of dimensions " + str(data.shape[0]) + " x "+str(data.shape[1]))
        return (data)

    def display(self, df, n):
        if n >= 0:
            print(df.head(n))
        else:
            print(df.tail(-n))

fl = FileLoader()
data = fl.load("../athlete_events.csv")
fl.display(data, 10)
fl.display(data, -10)