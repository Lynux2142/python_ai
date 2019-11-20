import numpy as np
from loading import ft_progress

def calc_blur(array, kernel):
    tmp_array = array * kernel
    return (np.sum(np.sum(tmp_array, axis = 1), axis = 0) / (np.sum(kernel) / 3 + 0.00001))

def browse_pixels(array, kernel, size):
    new_array = np.zeros(np.shape(array))
    for y in ft_progress(range(len(array))):
        for x in range(len(array[0])):

            gapy = [np.abs(y - size) if (y - size < 0) else 0, -(y + size - len(array) + 1) if (y + size >= len(array) - 1) else 0]
            gapx = [np.abs(x - size) if (x - size < 0) else 0, -(x + size - len(array[0]) + 1) if (x + size >= len(array[0]) - 1) else 0]

            resize_kernel = kernel[gapy[0] if (gapy[0]) else None:gapy[1] if (gapy[1]) else None, gapx[0] if (gapx[0]) else None:gapx[1] if (gapx[1]) else None]
            new_array[y, x] = calc_blur(array[y - size + gapy[0]:y + size + 1 + gapy[1], x - size + gapx[0] : x + size + 1 + gapx[1]], resize_kernel)
    print()
    return (new_array)

class AdvancedFilter:
    def mean_blur(array, size = 1):
        kernel = np.ones((1 + 2 * size, 1 + 2 * size, 3))
        return (browse_pixels(array, kernel, size))
    def gaussian_blur(array, size = 1, sigma = 1):
        kernel = np.ones((1 + 2 * size, 1 + 2 * size, 3))
        maxi = 2 * size ** 2
        for y in range(-size, size + 1):
            for x in range(-size, size + 1):
                kernel[y + size, x + size] = np.exp(-(((x ** 2) / (2 * sigma ** 2)) + ((y ** 2) / (2 * sigma ** 2))))
        return (browse_pixels(array, kernel, size))

