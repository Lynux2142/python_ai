import numpy as np

class ScrapBooker:
    def crop(array, dimensions, position=(0, 0)):
        try: assert (position[0] + dimensions[0] <= len(array[0]) and position[1] + dimensions[1] <= len(array))
        except: print('error: dimensions must be less or egal than array dimensions');
        else:
            array = np.delete(array, [i for i in range(0, position[0])], 1)
            array = np.delete(array, [i for i in range(0, position[1])], 0)
            array = np.delete(array, [i for i in range(dimensions[0], len(array[0]))], 1)
            array = np.delete(array, [i for i in range(dimensions[1], len(array))], 0)
            return (array)
    def thin(array, n, axis):
        return (np.delete(array, [(n * i) - 1 for i in range(1, len(array) if (axis == 0) else len(array[0]))], 1 - axis))
    def juxtapose(array, n, axis):
        return (np.concatenate([array for _ in range(n)], axis))
    def mosaic(array, dimensions):
        array = ScrapBooker.juxtapose(array, dimensions[0], 0)
        array = ScrapBooker.juxtapose(array, dimensions[1], 1)
        return (array)
