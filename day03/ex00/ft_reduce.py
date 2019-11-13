def ft_reduce(function_to_apply, list_of_inputs):
    try: assert (callable(function_to_apply) and (type(list_of_inputs) == list or type(list_of_inputs) == range))
    except: print('function_to_apply must be a function')
    else:
        res = [list_of_inputs[0]]
        for i in range(0, len(list_of_inputs) - 1):
            res.append(function_to_apply(res[-1], list_of_inputs[i + 1]))
        return (res[-1])
