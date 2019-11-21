import numpy as np
from loading import ft_progress

def calc_blur(array, kernel):
    tmp_array = array * kernel
    return (np.sum(np.sum(tmp_array, axis = 1), axis = 0) / (np.sum(kernel) / 3 + 0.00001))

def browse_pixels(array, kernel, size):
    new_array = np.zeros(np.shape(array))
    length = array.shape[0]
    width = array.shape[1]
    for y in ft_progress(range(length)):
        for x in range(width):

            gapx = [np.abs(x - size) if (x - size < 0) else 0, -(x + size - width + 1) if (x + size >= width - 1) else 0]
            gapy = [np.abs(y - size) if (y - size < 0) else 0, -(y + size - length + 1) if (y + size >= length - 1) else 0]

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
        for y in range(size * 2 + 1):
            for x in range(size * 2 + 1):
                kernel[y, x] = ((kernel.shape[0] * kernel.shape[1]) / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(((x - size) ** 2) + ((y - size) ** 2)) / (2 * sigma ** 2))
        return (browse_pixels(array, kernel, size))
