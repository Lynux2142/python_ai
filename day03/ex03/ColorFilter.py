import numpy as np
from loading import ft_progress

class ColorFilter:
    def invert(array):
        return (1.0 - array)
    def to_blue(array):
        pass
    def to_green(array):
        return (array * [0.0, 1.0, 0.0])
    def to_red(array):
        new_array = np.zeros(array.shape)
        for y in ft_progress(range(array.shape[0])):
            for x, pixel in enumerate(array[y]):
                new_array[y, x] = [min(pixel[0] + 1.0, 1.0), pixel[1], pixel[2]]
        return (new_array)
    def celluloid(array):
        pass
    def to_grayscale(array, filter='w'):
        new_array = np.zeros(array.shape)
        for y in ft_progress(range(array.shape[0])):
            for x, pixel in enumerate(array[y]):
                if (filter == 'weighted' or filter == 'w'):
                    value = np.sum((pixel * np.array([0.299, 0.587, 0.114])))
                elif (filter == 'mean' or filter == 'm'):
                    value = np.sum(pixel) / 3.0
                new_array[y, x] = [value, value, value]
        print()
        return (new_array)
