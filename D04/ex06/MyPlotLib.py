from FileLoader import FileLoader
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class MyPlotLib:
    def histogram(self, data, features):



loader = FileLoader()
data = loader.load('../athlete_events.csv')
mpl = MyPlotLib()
