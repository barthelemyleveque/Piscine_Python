import sys
import time

cookbook= {
    'sandwich': {
        'ingredients':['ham', 'bread', 'cheese', 'tomatoes'],
        'meal':'lunch',
        'prep_time':10,
    },
    'cake' : {
        'ingredients':['flour', 'sugar', 'eggs'],
        'meal':'dessert',
        'prep_time':60
    },
    'salad':{
        'ingredients':['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal':'lunch',
        'prep_time':15,
    }
}

def print_recipe(name):
    if name in cookbook:
        recipe = cookbook[name]
        print("Recipe for "+name+":")
        print("Ingredients list:" + str(recipe['ingredients']))
        print("To be eaten for: "+str(recipe["meal"]+"."))
        print("Takes "+str(recipe["prep_time"])+" minutes of cooking.")
    else: 
        print("Recipe doesn't exist")

def delete_recipe(name):
    if name in cookbook:
        del cookbook[name]
        print(name + " recipe has been deleted\n")
    else: 
        print("Cannot delete a recipe that doesn't exist")

def add_recipe(name, ingredients, meal, prep_time):
    if name in cookbook:
        print("Recipe already exists")
    else:
        cookbook[name] = {
            'ingredients': ingredients,
            'meal': meal,
            'prep_time': prep_time,
        }
        print("\nRecipe has been added :\n")
        print_recipe(name)

def print_all():
    for key in cookbook:
        print_recipe(key)
        print("----")

i = input('Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n')
while (i.isdigit() != 0 or int(i) > 5 or int(i) == 0):
    if (int(i) == 1):
        recipe = input('Please enter the recipe name to add:\n')
        str_ingredients = input('Please enter the ingredients of the recipe, separated by commas and no spaces:\n')
        ingredients = str_ingredients.split(",")
        meal = input('Please enter which meal it is best for :\n')
        prep_time = input('Please enter which prep time :\n')
        add_recipe(recipe, ingredients, meal, prep_time)
    if (int(i) == 2):
        delete_recipe(input('Please enter the recipe name to delete:\n'))
    if (int(i) == 3):
        print_recipe(input('Please enter the recipe name to get details:\n'))
    if (int(i) == 4):
        print_all()
    if (int(i) == 5):
        sys.exit("Goodbye !\n")
    time.sleep(4)
    i = input('Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n')


