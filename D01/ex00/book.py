import datetime
from recipe import *
import sys

class Book:
    def __init__(self):
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.recipes_list = {
            "starter":{},
            "main_course":{},
            "dessert":{}
        }

    def get_recipe_by_name(self, name):
        i = 0
        for types in self.recipes_list:
            for value in self.recipes_list[types]:
                if (value == name):
                    print(self.recipes_list[types][value])
                    i = 1
        if (i == 0):
            print("This recipe '"+str(name)+"'does not exists in this book")

    def get_recipes_by_type(self, type):
        i = 0
        print("Let's check thhe recipes for "+str(type)+":\n")
        for types in self.recipes_list:
            if types == type:
                for value in self.recipes_list[types]:
                    print(self.recipes_list[types][value])
                    i = 1
        if (i == 0):
            print("This type '"+type+"'does not exists in this book")
       
    def add_recipe(self, recipe):
        if (not isinstance(recipe, Recipe)):
            sys.exit("The recipe must be from a Recipe class")
        if (recipe.type == 'starter'):
            self.recipes_list["starter"][recipe.name] = recipe
        elif (recipe.type == 'main_course'):
            self.recipes_list["main_course"][recipe.name] = recipe
        elif (recipe.type == 'dessert'):
            self.recipes_list["dessert"][recipe.name] = recipe
        self.last_update = datetime.datetime.now() 
        print (recipe.name + " has been added to the Book !")
