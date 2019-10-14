import sys


def reverse(str):
    return str[::-1]


i = len(sys.argv)
if (i <= 1):
    sys.exit()
i -= 1
array = []
while i >= 1:
    array += reverse(sys.argv[i])
    i -= 1
string = ''
for word in array:
    for letter in word:
        if (letter.isupper()):
            string  += (letter.lower())
        else:
            string += (letter.upper())

print (string)