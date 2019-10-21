import numpy as np

class ScrapBooker:
    def crop(self, array, dimensions, pos=(0, 0)):
        #X = array [rows, columns]
        X = array[pos[0] : pos[0] + dimensions[0], pos[1] : pos[1] + dimensions[1]]
        return X
    
    #not sure
    def thin(self, array, n, axis):
        if (axis == 0):
            return array[::n, :]
        else:
            return array[:, ::n]

    def juxtapose(self, array, n, axis):
        Y = array
        for n in range(n):
            X = np.concatenate((array, Y), axis)
        return (X)

    def mosaic(self, array, dimensions):
        return np.tile(array, dimensions)


