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
    chosenfoodCalories = str(int(item["recipe"]["calories"]))
    # This converts kcals into calories
    print(chosenfoodCalories + " calories")

    # print total fat
    totalFat = str(int(item["recipe"]["totalNutrients"]["FAT"]["quantity"]))
    print(totalFat + " grams of Total Fat")

    # print cholesterol
    totalCHOLE = str(int(item["recipe"]["totalNutrients"]["CHOLE"]["quantity"]))
    print(totalCHOLE + " mg of Cholesterol")

    # print sugars
    totalSugar = str(int(item["recipe"]["totalNutrients"]["SUGAR"]["quantity"]))
    print(totalSugar + " grams of Sugar")

    # print protein
    totalProtein = str(int(item["recipe"]["totalNutrients"]["PROCNT"]["quantity"]))
    print(totalProtein + " grams of Protein")


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
