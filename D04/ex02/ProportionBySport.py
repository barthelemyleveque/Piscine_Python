from FileLoader import FileLoader
import pandas as pd

def ProportionBySport(df, year, sport, gender):
    df.drop_duplicates(['Name'], inplace = True)
    df = df[df.Year == year]
    df_gen = df[df.Sex == gender]
    total_gen = len(df_gen)
    df_sport = df_gen[df_gen.Sport == sport]
    sport_gen = len(df_sport)
    return (float(sport_gen) / float(total_gen))

loader = FileLoader()
data = loader.load('../athlete_events.csv')
percent = ProportionBySport(data, 2004, 'Tennis', 'F')
print(percent)