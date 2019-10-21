from matplotlib.image import imread
from matplotlib import pyplot as PLT
import numpy as np

class ImageProcessor:
    def load(self, path):
        img = imread(path)
        x = np.shape(img)[0]
        y = np.shape(img)[1]
        print("Loading image of dimensions " + str(x) + " x "+str(y))
        return img

    def display(self, arr):
        PLT.imshow(arr)
        PLT.show()

