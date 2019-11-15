import numpy as np

def calc_mean(array, x, y, kernel):
    shape = np.shape(array)
    newpixel = np.zeros(3)
    newarray = np.zeros((3, 3, 3))
    for i in range(-1, 1, 1):
        for j in range(-1, 1, 1):
            if (i >= 0 and i < shape[0] and j >= 0 and j < shape[1]):
                newarray[i + 1, j + 1] = (array[y-i, x-j] * kernel[i + 1, j + 1])
    rsum = np.sum([value[0] for value in np.ndindex(newarray.shape[:2])]) / np.sum(kernel)
    gsum = np.sum([value[1] for value in np.ndindex(newarray.shape[:2])]) / np.sum(kernel)
    bsum = np.sum([value[2] for value in np.ndindex(newarray.shape[:2])]) / np.sum(kernel)
    return ([rsum, gsum, bsum])

class AdvancedFilter:
    def mean_blur(array):
        kernel = np.ones((3, 3))
        kernel2 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
        for y, row in enumerate(array):
            for x, pixel in enumerate(row):
                array[y, x] = calc_mean(array, x, y, kernel2)
        return (array)
    def gaussian_blur(array):
        pass
