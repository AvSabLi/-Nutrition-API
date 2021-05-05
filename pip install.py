from py_edamam import Edamam

e = Edamam(
    nutrition_appid="2ac3e688",
    nutrition_appkey="2ac8a94c3c3bd1be3dbed7d629136176",
    recipes_appid="62fd6c39",
    recipes_appkey="5f0e27adae50eb576e4aebe320bbefe2",
    food_appid="36a390d9",
    food_appkey="cbaf379c5caa6f97d2a0ed6c11bc09f6",
)

# print(e.search_nutrient("1 large apple"))
# print(e.search_recipe("onion and chicken"))
# print(e.search_food("coke"))

# for recipe in e.search_recipe("salt"):
#     # ingredient = recipe
#     # print(recipe)
#     # print(recipe.calories)
#     # print(recipe.cautions, recipe.dietLabels, recipe.healthLabels)
#     # print(recipe.url)
#     print(recipe.ingredient_quantities)
#     break

for nutrient_data in e.search_nutrient("1 large apple"):
    # print(nutrient_data)
    print(nutrient_data.calories)
    # print(nutrient_data.cautions, nutrient_data.dietLabels, nutrient_data.healthLabels)
    # print(nutrient_data.totalNutrients)
    # print(nutrient_data.totalDaily)

# for food in e.search_food("coffee and pizza"):
#     print(food)
#     print(food.category)