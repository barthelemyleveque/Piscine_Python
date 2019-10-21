import numpy as np
from scipy.ndimage import median_filter

class AdvancedFilter:
    def mean_blur(self, arr):
        new = []
        window_size = 10
        for d in range(3):
            im_conv_d = median_filter(arr[:, :, d], size=(window_size, window_size))
            new.append(im_conv_d)

        im_conv = np.stack(new, axis=2)
        return im_conv

    def gaussian_blur(self, arr, kernel=6):
        nn = int((kernel - 1) / 2)
        a = np.asarray([[x ** 2 + y ** 2 for x in range(-nn,nn+1)] for y in range(-nn, nn+1)])
        return np.exp(-a/(4))

