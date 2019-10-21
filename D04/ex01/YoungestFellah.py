import pandas as pd
from FileLoader import FileLoader

def youngestFellah(df, year):
    medals_y = df[df.Year == year].reset_index(drop=True)
    medals_f = medals_y[medals_y.Sex == "F"].reset_index(drop=True)
    medals_m = medals_y[medals_y.Sex == "M"].reset_index(drop=True)
    yf = medals_f['Age'].min()
    ym = medals_m['Age'].min()
    return {'f' : yf, 'm' : ym}
    
    
loader = FileLoader()
data = loader.load('../athlete_events.csv')
yp = youngestFellah(data, 2004)
print (yp)