def ft_square(x):
    return x*x

def ft_map(function, list_of_inputs):
    res = []
    for i in list_of_inputs:
        res.append(function(i))
    return res


squared = ft_map(ft_square, [1, 2, 4, 8])
print(squared)