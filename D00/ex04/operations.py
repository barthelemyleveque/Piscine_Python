import sys

if (len(sys.argv) != 3):
    sys.exit("Usage: python operations.py <number1> <number2> \nExample: python operations.py 10 3")
num1 = sys.argv[1]
num2 = sys.argv[2]

if (num1.lstrip('-').isdigit() == 0 or num2.lstrip('-').isdigit() == 0):
    sys.exit("Usage: python operations.py <number1> <number2> \nExample: python operations.py 10 3")

num1 = int(num1)
num2 = int(num2)

print("Sum :            "+str(num1 + num2))
print("Difference :     "+str(num1 - num2))
print("Product :        "+str(num1 * num2))
if (num2 != 0):
    print("Quotient :       "+str(num1 / num2))
    print("Remainder :      "+str(num1 % num2))
else:
    print("Quotient :       "+ "Error -> cannot divide by 0")
    print("Remainder :      "+ "Error -> cannot modulo by 0")