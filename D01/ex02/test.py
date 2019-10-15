from vector import *

vector1 = Vector(0, 3)
print(vector1)
vector2 = Vector(4)
print(vector2)
vector3 = Vector([1.0, 2.5, 6.0])
print(vector3)

print("Operations")
vector4 = vector1 * 5
print(vector4)
vector4 = vector1 + 5
print(vector4)
vector4 = vector1 - 5
print(vector4)
vector4 = vector1 / 2
print(vector4)
vector4 = vector1 / 0
print(vector4)

#vector1 = Vector("lol", 3)
#print(vector1.values)
#vector1 = Vector(0, "lol")
#print(vector1.values)
#vector2 = Vector(4.5)
#print(vector2.values)
#vector3 = Vector([1.0, "s", 6.0])
#print(vector3.values)