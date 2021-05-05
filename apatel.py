# def recipe():
#     while True:

import requests, json, sys, time
from pprint import pprint
import pandas

# ask which food item user wants to cook
def function1():
    print(
        "please enter what food item you would like to cook, and we will provide the recipe"
    )
    chosenfoodItem = input("recipe name or (q)uit>")
    # if recipe.lower() == "q":
    #     break
    return chosenfoodItem


# search recipes based on user input
def function2(chosenfoodItem):
    url = f"https://api.edamam.com/search?q={chosenfoodItem}&app_id=62fd6c39&app_key=5f0e27adae50eb576e4aebe320bbefe2"

    response = requests.get(url)
    response.raise_for_status()  # check for errors

    recipeData = json.loads(response.text)
    return recipeData


def function3(recipeData):
    r = recipeData["hits"]
    return r


# print options based on what user searched
def function4(r):
    for item in r:
        # print recipe name
        recipeName = item["recipe"]["label"]
        print(str(recipeName))
    return recipeName


# ask user to select a specific recipe based on results
def function5(chosenfoodItem):
    print(
        "Please select which "
        + chosenfoodItem
        + " you are interested in cooking, and we will show you the ingredients."
    )
    basicPizza = input()
    return basicPizza


# redefine URL for specific food item
def function6(basicPizza):

    url2 = f"https://api.edamam.com/search?q={basicPizza}&app_id=62fd6c39&app_key=5f0e27adae50eb576e4aebe320bbefe2"

    response = requests.get(url2)
    response.raise_for_status()  # check for errors

    specificData = json.loads(response.text)

    specificR = specificData["hits"][1]["recipe"]["ingredientLines"]
    return specificR


# print ingredients
def function7(basicPizza, specificR):
    for item2 in specificR:
        print(item2["recipe"]["label"])
        for ingredient in item2["recipe"]["ingredientLines"]:
            print(ingredient)

    # recipeName = str(basicPizza)
    # # # recipeIngredients = basicPizza["recipe"]["ingredients"]
    # print(recipeName)
    # # print = str("recipeIngredients")
    # for ingredient in basicPizza["recipe"]["ingredientLines"]:
    #     print(ingredient)

    # for item2 in basicPizza:
    # print(item2["recipe"]["ingredientLines"])
    # for ingredient in basicPizza:
    #     print(basicPizza["recipe"]["ingredientLines"])


# ["recipe"]["ingredientLines"]
# for basicPizza in r:
#     # ingredients = basicPizza["recipe"]["ingredients"]
#     # print(ingredients)
#     for ingredient in basicPizza["recipe"]["ingredients"]:
#         print(ingredient)


# main function
userChosenFoodItem = function1()
userRecipeData = function2(userChosenFoodItem)
userR = function3(userRecipeData)
userRecipeName = function4(userR)
userBasicPizza = function5(userChosenFoodItem)
userSpecificR = function6(userBasicPizza)
function7(userBasicPizza, userSpecificR)


# #creating new dictionary for ingredients
# recipeFacts = {}
# for item2 in recipeList:
#     if recipeList == item2["recipe"]["label"]:
#         recipeFacts = {
#             "name:" item2["recipe"]["label"],
#             "ingredients:" item2["recipe"]["ingredients"]
#         }

# print ingredients
# recipeIngredients = item["recipe"]["ingredientLines"]
# print = str("recipeName")
# for ingredient in recipeIngredients:
#     print(ingredient)


# for item in r:
#     # print(item["recipe"]["label"])
#     # chosenfoodItem2 = str(item["recipe"]["label"])
#     # recipeIngredients = item["recipe"]["ingredientLines"]
#     # print(chosenfoodItem2)

#     # print name
#     chosenfoodItem2 = str(item["recipe"]["label"])
#     print(chosenfoodItem2)

#     #
#     # print calories
#     chosenfoodCalories = str(int(item["recipe"]["calories"]))
#     # This converts kcals into calories
#     print(chosenfoodCalories + " calories")

#     # print total fat
#     totalFat = str(int(item["recipe"]["totalNutrients"]["FAT"]["quantity"]))
#     print(totalFat + " grams of Total Fat")

#     # print cholesterol
#     totalCHOLE = str(int(item["recipe"]["totalNutrients"]["CHOLE"]["quantity"]))
#     print(totalCHOLE + " mg of Cholesterol")

#     # print sugars
#     totalSugar = str(int(item["recipe"]["totalNutrients"]["SUGAR"]["quantity"]))
#     print(totalSugar + " grams of Sugar")

#     # print protein
#     totalProtein = str(int(item["recipe"]["totalNutrients"]["PROCNT"]["quantity"]))
#     print(totalProtein + " grams of Protein")


# # for ingredient in item["recipe"]["ingredientLines"]:
# #     print(ingredient)

# # foodItem(r)

# print(
#     "Which of the following recipes would you like to use? We will provide ingredients for that recipe."
# )
# chosenRecipe = input()
# chosenfoodItem3 = chosenRecipe

# for ingredient in item["recipe"]["ingredientLines"]:
#     print(ingredient)
