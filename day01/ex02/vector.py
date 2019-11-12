class Vector:
    def __init__(self, param):
        try: assert (type(param) == list or type(param) == int or type(param) == tuple)
        except: print('param must be a list or int or tuple.')
        else:
            if (type(param) == list):
                self.values = [float(elem) for elem in param]
                self.length = len(param)
            elif (type(param) == int):
                self.values = []
                for i in range(0, param, 1):
                    self.values.append(float(i))
                self.length = param
            elif (type(param) == tuple):
                self.values = []
                for i in range(param[0], param[1]):
                    self.values.append(float(i))
                self.length = len(self.values)
    def __add__(self, param):
        try:
            assert (type(param) == int or type(param) == Vector)
            if (type(param) == Vector):
                assert (len(param.values) == len(self.values))
        except: print('param must be a scalar or instance of Vector as the same length')
        else:
            if (type(param) == int):
                return (Vector([value + param for value in self.values]))
            else:
                return (Vector([value1 + value2 for value1, value2 in zip(self.values, param.values)]))
    def __radd__(self, param):
        return (self.__add__(param))
    def __sub__(self, param):
        try:
            assert (type(param) == int or type(param) == Vector)
            if (type(param) == Vector):
                assert (len(param.values) == len(self.values))
        except: print('param must be a scalar or instance of Vector as the same length')
        else:
            if (type(param) == int):
                return (Vector([value - param for value in self.values]))
            else:
                return (Vector([value1 - value2 for value1, value2 in zip(self.values, param.values)]))
    def __rsub__(self, param):
        try:
            assert (type(param) == int or type(param) == Vector)
            if (type(param) == Vector):
                assert (len(param.values) == len(self.values))
        except: print('param must be a scalar or instance of Vector as the same length')
        else:
            if (type(param) == int):
                return (Vector([param - value for value in self.values]))
            else:
                return (Vector([value2 - value1 for value1, value2 in zip(self.values, param.values)]))
    def __mul__(self, param):
        try:
            assert (type(param) == int or type(param) == Vector)
            if (type(param) == Vector):
                assert (len(param.values) == len(self.values))
        except: print('param must be a scalar or instance of Vector as the same length')
        else:
            if (type(param) == int):
                return (Vector([value * param for value in self.values]))
            else:
                return (sum([value1 * value2 for value1, value2 in zip(self.values, param.values)]))
    def __rmul__(self, param):
        return (self.__mul__(param))
    def __truediv__(self, param):
        try:
            assert (type(param) == int and param != 0)
        except: print('param must be a scalar different than 0')
        else:
            return (Vector([value / param for value in self.values]))
    def __rtruediv__(self, param):
        try:
            assert (type(param) == int and not 0 in self.values)
        except: print('param must be a scalar and no vector value must be 0')
        else:
            return (Vector([param / value for value in self.values]))
    def __str__(self): return (f'(Vector {self.values})')
    def __repr__(self): return (f'{self.values}')
