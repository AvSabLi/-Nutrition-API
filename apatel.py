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
    chosenRecipeName = input()
    return chosenRecipeName


# print ingredients
def function6(chosenRecipeName, r):
    for item in r:
        # print(item["recipe"]["label"])
        for ingredient in item["recipe"]["ingredientLines"]:
            if chosenRecipeName == item["recipe"]["label"]:
                print("-" + ingredient)
                pass


# ask if user wants to see nutrition facts
def function7(chosenRecipeName):
    print(
        "Would you like to see the nutritional facts for "
        + chosenRecipeName
        + "? Type yes or no"
    )
    seeNutritionInfo = input()
    return seeNutritionInfo


# calories function
def function8(r, chosenRecipeName):
    for item in r:
        # print(item["recipe"]["label"])
        # for chosenFoodCalories in item["recipe"]["calories"]:
        if chosenRecipeName == item["recipe"]["label"]:
            recipeCalories = str(int(item["recipe"]["calories"]))
            # print(chosenFoodCalories + " calories")
        pass
    return recipeCalories


# total fat function
def function9(r, chosenRecipeName):
    for item in r:
        # print(item["recipe"]["label"])
        # for chosenFoodCalories in item["recipe"]["calories"]:
        if chosenRecipeName == item["recipe"]["label"]:
            recipeTotalFat = str(
                int(item["recipe"]["totalNutrients"]["FAT"]["quantity"])
            )
            # print(totalFat + " grams of Total Fat")
        pass
    return recipeTotalFat


# print nutrition info
def function12(seeNutritionInfo, chosenRecipeName, recipeCalories, recipeTotalFat):
    if seeNutritionInfo == "yes" or seeNutritionInfo == "y":
        recipeNutritionPandas = [
            ["Item Name:", chosenRecipeName],
            ["Calories:", recipeCalories],
            ["Total Fat:", recipeTotalFat],
            # ["Cholesterol:", item["cholesterol"]],
            # ["Sugar:", item["sugars"]],
            # ["Protein:", item["protein"]],
        ]
        # columns
        headerY = [
            "  ",
            "  ",
            # "  ",
            # "  ",
            # "  ",
            # "  ",
            # "  ",
            # "  ",
        ]
        # rows
        headerX = [
            "  ",
            "  ",
            "  ",
            # "  ",
            # "  ",
            # "  ",
            # "  ",
            # "  ",
        ]
        print(pandas.DataFrame(recipeNutritionPandas, headerX, headerY))
    elif seeNutritionInfo == "no" or seeNutritionInfo == "n":
        print("No problem!")
    pass


# main function
userChosenFoodItem = function1()
userRecipeData = function2(userChosenFoodItem)
userR = function3(userRecipeData)
userRecipeName = function4(userR)
userChosenRecipeName = function5(userChosenFoodItem)
function6(userChosenRecipeName, userR)
userSeeNutritionInfo = function7(userChosenRecipeName)
userRecipeCalories = function8(userR, userChosenRecipeName)
userRecipeTotalFat = function9(userR, userChosenRecipeName)
function12(
    userSeeNutritionInfo, userChosenRecipeName, userRecipeCalories, userRecipeTotalFat
)


# #creating new dictionary for ingredients
# recipeFacts = {}
# for item2 in recipeList:
#     if recipeList == item2["recipe"]["label"]:
#         recipeFacts = {
#             "name:" item2["recipe"]["label"],
#             "ingredients:" item2["recipe"]["ingredients"]
# #         }

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
