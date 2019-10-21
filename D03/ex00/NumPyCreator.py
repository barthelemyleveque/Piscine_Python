import numpy as np

class NumPyCreator:
    def from_list(self, liste):
        return np.asarray(liste)
    def from_tuple(self, liste):
        return np.asarray(liste)
    def from_iterable(self, iterable):
        return np.fromiter(iterable, float)
    def from_shape(self, shape, value=0):
        return np.full(shape, value)
    def random(self, shape):
        return np.random.random_sample(shape)
    def identity(self, n):
        return np.identity(n)


npc = NumPyCreator()
print(npc.from_list([[1,2,3],[6,3,4]]))
print(npc.from_tuple(("a", "b", "c")))
print(npc.from_iterable(range(5)))
shape = (3,5)
print(npc.from_shape(shape))
print(npc.random(shape))
print(npc.identity(8))