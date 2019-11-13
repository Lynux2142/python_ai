def ft_map(function_to_apply, list_of_inputs):
    try: assert (callable(function_to_apply) and (type(list_of_inputs) == list or type(list_of_inputs) == range))
    except: print('function_to_apply must be a function')
    else:
        res = []
        for elem in list_of_inputs:
            res.append(function_to_apply(elem))
        return (res)
