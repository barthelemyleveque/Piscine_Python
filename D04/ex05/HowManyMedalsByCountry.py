from FileLoader import FileLoader
import pandas as pd

def howManyMedalsByCountry(data, name):
    athlete = data[(data.Team == name) & (data.Medal.isna() == False)]
    athlete = athlete.sort_values(by='Year')
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
medals = howManyMedalsByCountry(data, "Nigeria")
print(medals)