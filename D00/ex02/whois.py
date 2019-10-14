import sys

if (len(sys.argv) == 1):
    sys.exit()
elif (len(sys.argv) > 2):
    sys.exit('ERROR')

arg = sys.argv[1]
if (arg.lstrip('-').isdigit() == 0):
    sys.exit('ERROR')
number = int(arg)
if (number == 0):
    sys.exit("I'm Zero.")
elif (number % 2 == 0):
    sys.exit("I'm Even.")
elif (number % 2 == 1):
    sys.exit("I'm Odd.")
