import sys

class Vector:
    def __init__(self, values, len_v=None):
        if (isinstance(values, int) and values == 0):
            if (isinstance(len_v, int) and len_v > 0):
                i = 0
                values = [None] * len_v
                for x in range(0, len_v):
                    values[i] = float(x)
                    i += 1
        elif (isinstance(values, int) and len_v == None):
            if values > 0:
                i = 0
                length = values
                values = [None] * length
                for x in range(0, length):
                    values[i] = float(x)
                    i += 1

        self.values = values
        self.len = len(values)

    def __setattr__(self, name, value):
        if (name == 'values' and not isinstance(value, list)):
            sys.exit('vector.values must be an array')
        elif(name == 'values' and not all(isinstance(item, float) for item in value)):
            sys.exit('items in vector.values must be floats')
        elif (name == 'values'):
            super().__setattr__(name, value)
        if (name == "len" and value <= 0):
            sys.exit('len must be positive')
    
    def __add__(self, value):
        return Vector([i + value for i in self.values])

    def __sub__(self, value):
        return Vector([i - value for i in self.values])

    def __mul__(self, value):
        return Vector([i * value for i in self.values])

    def __truediv__(self, value):
        if (value == 0):
            sys.exit("Cannot divide by 0")
        return Vector([i / value for i in self.values])
    
    def __str__(self):
        """Return the string to print with the recipe info"""
        text = "Vector " + str(self.values)
        return (text)
    
    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

