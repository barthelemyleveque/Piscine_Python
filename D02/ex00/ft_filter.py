def ft_modulo(x):
    if (x % 2 == 0):
        return True
    return False

def ft_filter(function, list_of_inputs):
    res = []
    for i in list_of_inputs:
        if (function(i)):
            res.append(i)
    return(i)

filtered = ft_filter(ft_modulo, [1, 3, 0, 2])
print(filtered)