from FileLoader import FileLoader
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class MyPlotLib:
    def histogram(self, data, features):
        for feature in features:
            temp = data[feature]
            temp = temp.dropna()
            plt.hist(temp)
            plt.title("Histogram for : " + feature)
            plt.show()

    def density(self, data, features):
        for feature in features:
            temp = data[feature]
            temp = temp.dropna()
            sns.distplot(temp)
            plt.title("Histogram for : " + feature)
            plt.show()

    def pair_plot(self, data, features):
        temp = data[features]
        temp = temp.dropna()
        sns.pairplot(temp, hue="Sex")
        plt.show()

    def box_plot(self, data, features):
        for feature in features:
            temp = data[feature]
            temp = temp.dropna()
            plt.boxplot(temp)
            plt.title("Boxplot for : " + feature)
            plt.show()
