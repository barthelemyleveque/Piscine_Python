import sys

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, r_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.type = r_type

    def __setattr__(self, name, value):
        if name == 'name' and not isinstance(value, str):
            sys.exit('recipe.name must be a string')
        elif name == 'name' and len(value) < 1 :
            sys.exit('recipe.name must not be empty')
        elif name =="name":
            super().__setattr__(name, value)

        if name == 'cooking_lvl' and not isinstance(value, int):
            sys.exit('recipe.cooking_lvl must be an int')
        elif name == 'cooking_lvl' and not (1 <= value <= 5):
            sys.exit('recipe.cooking_lvl must be in range one to five')
        elif name =="cooking_lvl":
            super().__setattr__(name, value)

        if name == 'cooking_time' and not isinstance(value, int):
            sys.exit('recipe.cooking_time must be an int')
        elif name == 'cooking_time' and value < 0:
            sys.exit('recipe.cooking_time must be positive')
        elif name =="cooking_time":
            super().__setattr__(name, value)

        if name == 'ingredients' and not isinstance(value, list):
            sys.exit('recipe.ingredients must be a list')
        elif name == 'ingredients' and not all(isinstance(item, str) for item in value):
            sys.exit('recipe.ingredients values must all be strings')
        elif name =="ingredients":
            super().__setattr__(name, value)

        if name == 'description' and not isinstance(value, str):
            sys.exit('recipe.description must be a string')
        elif name =="description":
            super().__setattr__(name, value)

        if name == 'type' and not isinstance(value, str):
            sys.exit('recipe.type must be a string')
        elif name == 'type' and (value != 'starter' and value != 'main_course' and value != 'dessert'):
            sys.exit('recipe.type must be equal to starter or main_course or dessert')
        elif name =="type":
            super().__setattr__(name, value)

    def __str__(self):
        """Return the string to print with the recipe info"""
        text = "Recipe for: " + self.name + "\nIt's a level "+str(self.cooking_lvl)+" recipe that takes "+str(self.cooking_time)+"min to prepare.\n"
        text = text + "The ingredient list is :" + str(self.ingredients) + "\nRecipe Description:\n" + self.description + "\nIt's a " + self.type
        return text
       
        