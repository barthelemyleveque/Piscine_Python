import random
import sys

print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")
i = random.randint(1, 99)
user_input = 0
count = 0
while (user_input != i):
    count += 1
    user_input = input("What's your guess between 1 and 99?\n >> ")
    if (user_input == "exit"):
        sys.exit("Thank you for playing !")
    if (user_input.isdigit() == 0):
        print("That's not a number")
        continue
    user_input = int(user_input)
    if (user_input > i):
        print("Too high !")
    elif (user_input < i):
        print("Too low !")

if (user_input == i and i == 42):
    print("The answer to the ultimate question of life, the universe and everything is 42.")
if (count == 1):
    print("Congratulations! You got it at the first try!")
else:
    print("Congratulation, you've got it!\nYou won in " + str(count) + " attempts!")