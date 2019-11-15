import numpy as np

class ColorFilter:
    def invert(array):
        return (1.0 - array)
    def to_blue(array):
        pass
    def to_green(array):
        return (array * [0.0, 1.0, 0.0])
    def to_red(array):
        return (np.array(list(map(lambda x: list(map(lambda y: [min(y[0] + 1.0, 1.0), y[1], y[2]], x)), array))))
    def celluloid(array):
        pass
    def to_grayscale(array, filter='w'):
        if (filter == 'weighted' or filter == 'w'):
            for y, row in enumerate(array):
                for x, pixel in enumerate(row):
                    value = np.sum((pixel * np.array([0.299, 0.587, 0.114])))
                    array[y, x] = [value, value, value]
        elif (filter == 'mean' or filter == 'm'):
            for y, row in enumerate(array):
                for x, pixel in enumerate(row):
                    value = np.sum(pixel) / 3.0
                    array[y, x] = [value, value, value]
        return (array)
