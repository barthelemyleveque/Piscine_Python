from FileLoader import FileLoader
import pandas as pd

class SpatioTemporalData:
    def __init__(self, data):
        self.df = data
    
    def when(self, location):
        places = []
        years = self.df[self.df.City == location]
        for index, row in years.iterrows():
            if row['Year'] not in places:
                places.append(row['Year'])
        return places
    
    def where(self, year):
        year = int(year)
        city = self.df[self.df.Year == year]
        return city['City'].iloc[0]
            
loader = FileLoader()
data = loader.load('../athlete_events.csv')
sp = SpatioTemporalData(data)
print(sp.when('Atlanta'))
print(sp.where('2016'))