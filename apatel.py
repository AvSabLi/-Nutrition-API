# def recipe():
#     while True:

import requests, json, sys, time
from pprint import pprint
import pandas


print(
    "please enter what food item you would like to cook, and we will provide the recipe"
)
chosenfoodItem = input("recipe name or (q)uit>")
# if recipe.lower() == "q":
#     break

url = f"https://api.edamam.com/search?q={chosenfoodItem}&app_id=62fd6c39&app_key=5f0e27adae50eb576e4aebe320bbefe2"

response = requests.get(url)
response.raise_for_status()  # check for errors

recipeData = json.loads(response.text)
r = recipeData["hits"]
for item in r:
    # print(item["recipe"]["label"])
    # chosenfoodItem2 = str(item["recipe"]["label"])
    # recipeIngredients = item["recipe"]["ingredientLines"]
    # print(chosenfoodItem2)

    # print name
    chosenfoodItem2 = str(item["recipe"]["label"])
    print(chosenfoodItem2)

    # print calories
    chosenfoodCalories = str(item["recipe"]["calories"])
    print(chosenfoodCalories)

    # print total fat
    totalFat = str(item["recipe"]["totalNutrients"]["FAT"]["quantity"])
    print(totalFat)

    # print cholesterol
    totalCHOLE = str(item["recipe"]["totalNutrients"]["CHOLE"]["quantity"])
    print(totalCHOLE)

    # print sugars
    totalSugar = str(item["recipe"]["totalNutrients"]["SUGAR"]["quantity"])
    print(totalSugar)

    # print protein
    totalProtein = str(item["recipe"]["totalNutrients"]["PROCNT"]["quantity"])
    print(totalProtein)


# for ingredient in item["recipe"]["ingredientLines"]:
#     print(ingredient)

# foodItem(r)

print(
    "Which of the following recipes would you like to use? We will provide ingredients for that recipe."
)
chosenRecipe = input()
chosenfoodItem3 = chosenRecipe

for ingredient in item["recipe"]["ingredientLines"]:
    print(ingredient)

# Calories
# Total fat
# Cholesterol
# Sugars
# Protein
