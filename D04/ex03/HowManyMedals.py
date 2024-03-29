from FileLoader import FileLoader
import pandas as pd

def howManyMedals(data, name):
    athlete = data[(data.Name == name) & (data.Medal.isna() == False)]
    medals = {}
    year = 0
    for index, row in athlete.iterrows():
        if (year != row['Year']):
            year = row['Year']
            g = 0
            s = 0 
            b = 0
        if (row["Medal"] == "Gold"):
            g += 1
        elif (row["Medal"] == "Silver"):
            s += 1
        elif (row["Medal"] == "Bronze"):
            b += 1
        medals.update({row['Year'] : {"G" : g, "S" : s, "B" : b}})
    return medals

loader = FileLoader()
data = loader.load('../athlete_events.csv')
medals = howManyMedals(data, "Michael Fred Phelps, II")
print(medals)