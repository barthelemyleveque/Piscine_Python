from ImageProcesor import ImageProcessor
from ScrapBooker import ScrapBooker
from ColorFilter import ColorFilter

pic = ImageProcessor()
arr = pic.load("42AI.png")
pic.display(arr)

cf = ColorFilter
"""
sb = ScrapBooker()
data = arr
X = sb.crop(data, (100,100), (50, 50))
pic.display(X)

X = sb.thin(data, 10, 0)
pic.display(X)
X = sb.thin(data, 3, 1)
pic.display(X)

X = sb.juxtapose(data, 2, 0)
pic.display(X)
X = sb.juxtapose(data, 2, 1)
pic.display(X)

X = sb.mosaic(data, (4,4))
pic.display(X)
"""