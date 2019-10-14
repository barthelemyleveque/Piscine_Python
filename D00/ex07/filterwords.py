import sys

try:
    string = sys.argv[1]
except IndexError:
    string = None
try:
    integer = sys.argv[2]
except IndexError:
    integer = None
try:
    check = sys.argv[3]
except IndexError:
    check = None

if (string.isdigit() == 1 or integer.isdigit() == 0):
    sys.exit("ERROR")

arg = string.split(" ")
arg.append(None)
i = 0
arr = []
while (arg[i] != None):
    sub = list(arg[i])
    toprint = ''
    len_sub = 0
    for x in sub:
        if x  in [',', '.', '!', ';', '?', ':']:
            sub.remove(x)
        else:
            len_sub += 1
    if len_sub > int(integer):
        arr.append(''.join(sub))
    i += 1
print(arr)