def ft_mult(a, b):
    return a *b

def ft_reduce(function, list_of_inputs):
    reduce = 1
    for i in list_of_inputs:
        reduce = function(reduce, i)
    return (reduce)

reduced = ft_reduce(ft_mult, [1, 2, 4, 5])
print(reduced)