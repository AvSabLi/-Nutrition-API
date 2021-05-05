# def recipe():
#     while True:

import requests, json, sys, time
from pprint import pprint
import pandas
import pycurl


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
    chosenfoodItem2 = str(item["recipe"]["label"])
    # recipeIngredients = item["recipe"]["ingredientLines"]
    print(chosenfoodItem2)
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

url = f"https://api.edamam.com/api/nutrition-details?app_id=2ac3e688&app_key=5f0e27adae50eb576e4aebe320bbefe2"
curl -d @chosenfoodItem3.json -H "Content-Type: application/json" "https://api.edamam.com/api/nutrition-details?app_id=2ac3e688&app_key=2ac8a94c3c3bd1be3dbed7d629136176"


response = requests.get(url)
response.raise_for_status()  # check for errors

jsonData = json.loads(response.text)
# r = recipeData["hits"]
pprint(jsonData)