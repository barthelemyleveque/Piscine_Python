import numpy as np

class ColorFilter:
    def invert(self, array):
        return (1 - array)
    
    def to_green(self, array):
        X = np.zeros(np.shape(array))
        #collection of arrays
        for x, a in zip(X, array):
            #individual arrays
            for xx, aa in zip(x, a):
                aa[2] = xx[2]
        return array
    
    def to_red(self, array):
        return (array * [1, 0, 1])
    
    def to_blue(self, array):
        array[:, :, 0] = 0
        return array

    def to_grayscale(self, array, filter, weight=(0.299, 0.587, 0.114)):
        if (filter == "m" or filter == "mean"):
            for a in array:
                for aa in a:
                    mean = np.mean(aa)
                    aa[:] = mean
            return array
        elif (filter == "w" or filter == "weighted"):
            array[:, :, 0] = array[:, :, 0] * weight[0]
            array[:, :, 1] = array[:, :, 1] * weight[1]
            array[:, :, 2] = array[:, :, 2] * weight[2]
            return array