from book import *
from recipe import *

print("lol" + None)
tourte = Recipe("t", +3, 30, 5, "une grosse tourte", "starter") #good
gateau = Recipe("gateau", 2, 10, ["sucre", "faribne", "chocolat"], "un beau gateau", "dessert") #good
meringue = Recipe("meringue", 1, 10, ["sucre", "du sucre", "et encore du sucre"], "une meringue avec beaucoup de sucre", "dessert") #good
omelette = Recipe("omelette", 5, 50, ["eggs", "cream", "chocolat"], "une omelette bien cremeuse", "main_course") #good

recipe_book = Book()
print(recipe_book.creation_date)
recipe_book.add_recipe(tourte)
recipe_book.add_recipe(gateau)
recipe_book.add_recipe(meringue)
recipe_book.add_recipe(omelette)
print(recipe_book.last_update)
print("\n")
recipe_book.get_recipe_by_name("tourte")
print("\n")
recipe_book.get_recipe_by_name("omelette")
recipe_book.get_recipe_by_name("tourtelette")
print("\n")
recipe_book.get_recipes_by_type("dessert")
print("\n")
recipe_book.get_recipes_by_type("caca")
recipe_book.add_recipe("caca")
print(type(("lol", "lol")))