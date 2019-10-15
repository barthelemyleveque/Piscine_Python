import sys

class Vector:
    def __init__(self, values, len_v=None):
        if (isinstance(values, int) and values == 0):
            if (isinstance(len_v, int) and len_v > 0):
                for x in range(0, len_v):
                    values.app
                print(values)
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


vector1 = Vector(0, 3)