import numpy as np
from loading import ft_progress

def calc_blur(array, kernel):
    tmp_array = array * kernel
    rsum = np.sum(tmp_array[:,:,0]) / (np.sum(kernel) / 3.0)
    gsum = np.sum(tmp_array[:,:,1]) / (np.sum(kernel) / 3.0)
    bsum = np.sum(tmp_array[:,:,2]) / (np.sum(kernel) / 3.0)
    return ([rsum, gsum, bsum])

def browse_pixels(array, kernel, size):
    new_array = np.zeros(np.shape(array))
    for y in ft_progress(range(len(array))):
        for x in range(len(array[0])):
            gapx = [0, 0]
            gapy = [0, 0]
            if (y - size < 0):
                gapy[0] = np.abs(y - size)
            if (y + size >= len(array) - 1):
                gapy[1] = -(y + size - len(array) + 1)
            if (x - size < 0):
                gapx[0] = np.abs(x - size)
            if (x + size >= len(array[0]) - 1):
                gapx[1] = -(x + size - len(array[0]) + 1)
            resize_kernel = kernel[gapy[0] if (gapy[0]) else None:gapy[1] if (gapy[1]) else None,gapx[0] if (gapx[0]) else None:gapx[1] if (gapx[1]) else None]
            new_array[y, x] = calc_blur(array[y-size+gapy[0]:y+size+1+gapy[1], x-size+gapx[0]:x+size+1+gapx[1]], resize_kernel)
    return (new_array)

class AdvancedFilter:
    def mean_blur(array, size=1):
        kernel = np.ones((1 + 2 * size, 1 + 2 * size, 3))
        return (browse_pixels(array, kernel, size))
    def gaussian_blur(array, size=1, sigma=2.0):
        kernel = np.ones((1 + 2 * size, 1 + 2 * size, 3))
        for i in range(size + 1):
            kernel[i:-i,:] *= sigma
            kernel[:,i:-i] *= sigma
        return (browse_pixels(array, kernel, size))

