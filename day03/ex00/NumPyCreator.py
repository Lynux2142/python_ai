import numpy as np

class NumPyCreator:
    def from_list(param, dtype=None):
        return (np.array(param, dtype=dtype))
    def from_tuple(param, dtype=None):
        return (np.array(param, dtype=dtype))
    def from_iterable(param, dtype=None):
        return (np.array(param, dtype=dtype))
    def from_shape(param, value=0, dtype=None):
        return (np.full(param, value, dtype=dtype))
    def random(param):
        return (np.random.random(param))
    def identity(param, dtype=None):
        return (np.identity(param, dtype=dtype))
