import requests, json, sys, time
from pprint import pprint
import pandas as pd
import xlsxwriter
import xlrd
from openpyxl import load_workbook


# This function includes the introduction information for the API
def intro1():
    print("Welcome to the Nutritionix API Service.")
    time.sleep(1)  # time.sleep adds time before the next line of code is printed
    print("What is your name?")
    myName = input()
    print("Hi " + myName + "!")
    time.sleep(1)
    print("          ")
    print(
        "With this program you can either choose recipes to cook at home and eat in, or find menu items from a restaurant and dine out. "
    )
    time.sleep(3)
    print("          ")
    print(
        "Once you have selected your dining option, you will either get a full recipe and related nutritional information with the dine in option, or the nutritional information from a menu item at a selected restaurant."
    )
    time.sleep(3)
    print("          ")
    print(
        "If you decide to dine in...\nYou can search pizza, for example, and have an entire recipe of how to make pizza in your kitchen from scratch!\nThen, information including calories, fats, cholesterol, sugar and protein for your pizza recipe will be given to you."
    )
    time.sleep(3)
    print("          ")
    print(
        "Or if you decide to dine out...\nYou can search Mcdonald's, for example, and select McNuggets.\nThen, information including calories, fats, cholesterol, sugar and protein for McNuggets will be given to you."
    )
    print("          ")
    time.sleep(3)
    return myName


# saving preference to eat in or dine out
def intro2(myName):
    print("Now, " + myName + ", would you like to eat in or dine out?")
    dineInOrOut = input()
    print("          ")
    return dineInOrOut


# print empty excel called nutritionalDatabase
def intro3():
    writer = pd.ExcelWriter(  # https://github.com/PyCQA/pylint/issues/3060 pylint: disable=abstract-class-instantiated
        "nutritionalDatabase.xlsx", engine="xlsxwriter"
    )
    writer.save()


# This function asks user to select menu item they want to explore
def functionA(n):
    print(
        "Please enter which item name you want to see nutrition information for from the list below."
    )
    foodItem = input()
    return foodItem


# saving nutrition info for indicated menu item into dictionary & list
def functionB(n, foodItem, myList):
    for item in n:
        if foodItem == item["fields"]["item_name"]:
            selectedFood = {
                "name": item["fields"]["item_name"],
                "calories": str(item["fields"]["nf_calories"]) + " kcals",
                "total fat": str(item["fields"]["nf_total_fat"]) + " grams",
                "cholesterol": str(item["fields"]["nf_cholesterol"]) + " grams",
                "sugars": str(item["fields"]["nf_sugars"]) + " grams",
                "protein": str(item["fields"]["nf_protein"]) + " grams",
            }
            # this adds the information gathered from selectedFood to a list called myList
            myList.append(selectedFood)
    return selectedFood, myList


# this function asks the user which restaurants data they want to look at and returns food items sold at the restaurant selected
def functionC():
    print("Please enter a restaurant name.")
    restaurant = input()
    return restaurant


# use API to call data for restaurant indicated
def functionD(restaurant):
    # This URL calls the API with the search by 'restaurant' function and names it URL.
    # When a 'restaurant' is chosen, the adjusted url returns a dictionary within a list of food item names for that specific restaurant
    url = f"https://api.nutritionix.com/v1_1/search/{restaurant}?results=0:20&fields=item_name,nf_calories,nf_calories_from_fat,nf_total_fat,nf_saturated_fat,nf_cholesterol,nf_sugars,nf_protein&appId=f3b374ec&appKey=988ab0bd10dc4a886738973eec0524d1"
    response = requests.get(url)
    response.raise_for_status()  # check for errors
    # Load json data into a python variable
    nutritionData = json.loads(response.text)
    n = nutritionData["hits"]
    return n


# printing restaurant menu
def functionE(n):
    for item in n:
        print(
            item["fields"]["item_name"],
        )


# print pandas table with nutritional data + save into excel created in intro3 function
def functionF(n, myList, selectedFood, foodItem):
    print("Here are the nutrition facts for the food items you selected:\n")
    time.sleep(2)
    print("     ")
    for item in myList:

        foodData = [
            ["Item Name:", item["name"]],
            ["Calories:", item["calories"]],
            # ["Calories from Fat:", item["calories from fat"]],
            ["Total Fat:", item["total fat"]],
            # ["Saturated Fat:", item["saturated fat"]],
            ["Cholesterol:", item["cholesterol"]],
            ["Sugar:", item["sugars"]],
            ["Protein:", item["protein"]],
        ]
        # columns
        headerY = [
            "  ",
            "  ",
        ]
        # rows
        headerX = [
            "  ",
            "  ",
            "  ",
            "  ",
            "  ",
            "  ",
        ]
        df = pd.DataFrame(foodData, headerX, headerY)
        print(df)

        # next note is for pylint to stop giving error for pd
        with pd.ExcelWriter(  # https://github.com/PyCQA/pylint/issues/3060 pylint: disable=abstract-class-instantiated
            "nutritionalDatabase.xlsx", engine="openpyxl", mode="a"
        ) as f:
            df.to_excel(f, sheet_name=foodItem, index=False, header=False)


# ask user if they want to find the restaurant near them on googlemaps
def functionG(restaurant):
    print("Do you want to find the nearest " + restaurant + "?")
    searchLocation = input()
    return searchLocation


# print google maps URL to restaurant if user says yes
def functionH(searchLocation, restaurant):
    if searchLocation == "yes" or searchLocation == "y":
        # Fetch the information of that restaurant
        restaurantNew = restaurant.replace(" ", "")
        map_url = f"https://www.google.com/maps/search/?api=1&query={restaurantNew}"
        # Print message
        print("To view " + restaurant + " in Google Maps, go to " + map_url)
        print("-----------------------------------------")
        return map_url

    elif searchLocation == "no" or searchLocation == "n":
        pass


# ask which food item user wants to cook
def function1():
    print(
        "Please enter what food item you would like to cook, and we will provide the recipe."
    )
    chosenfoodItem = input()
    return chosenfoodItem


# search recipes based on user input in API
def function2(chosenfoodItem):
    url = f"https://api.edamam.com/search?q={chosenfoodItem}&app_id=62fd6c39&app_key=5f0e27adae50eb576e4aebe320bbefe2"

    response = requests.get(url)
    response.raise_for_status()  # check for errors

    recipeData = json.loads(response.text)
    return recipeData


# returning list of recipes that comes up from chosenFoodItem
def function3(recipeData):
    r = recipeData["hits"]
    return r


# print recipe options based on what user searched
def function4(r):
    for item in r:
        # print recipe name
        recipeName = item["recipe"]["label"]
        print(str(recipeName))


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
        for ingredient in item["recipe"]["ingredientLines"]:
            if chosenRecipeName == item["recipe"]["label"]:
                print("-" + ingredient)
                pass


# ask if user wants to see nutrition facts
def function7(chosenRecipeName):
    print(
        "Would you like to see the nutritional facts for "
        + chosenRecipeName
        + "? Type yes or no."
    )
    seeNutritionInfo = input()
    return seeNutritionInfo


# calories function
def function8(r, chosenRecipeName):
    for item in r:
        if chosenRecipeName == item["recipe"]["label"]:
            recipeCalories = str(int(item["recipe"]["calories"]))
        pass
    return recipeCalories


# total fat function
def function9(r, chosenRecipeName):
    for item in r:
        if chosenRecipeName == item["recipe"]["label"]:
            recipeTotalFat = str(
                int(item["recipe"]["totalNutrients"]["FAT"]["quantity"])
            )
        pass
    return recipeTotalFat


# cholesterol function
def function10(r, chosenRecipeName):
    for item in r:
        if chosenRecipeName == item["recipe"]["label"]:
            recipeCholesterol = str(
                int(item["recipe"]["totalNutrients"]["CHOLE"]["quantity"])
            )
        pass
    return recipeCholesterol


# sugar function
def function11(r, chosenRecipeName):
    for item in r:
        if chosenRecipeName == item["recipe"]["label"]:
            recipeSugar = str(
                int(item["recipe"]["totalNutrients"]["SUGAR"]["quantity"])
            )
        pass
    return recipeSugar


# protein function
def function12(r, chosenRecipeName):
    for item in r:
        if chosenRecipeName == item["recipe"]["label"]:
            recipeProtein = str(
                int(item["recipe"]["totalNutrients"]["PROCNT"]["quantity"])
            )
        pass
    return recipeProtein


# creating dictionary for recipe nutrition info
def functionRecipeDictionary(
    chosenRecipeName,
    recipeCalories,
    recipeTotalFat,
    recipeCholesterol,
    recipeSugar,
    recipeProtein,
    recipeNutritionDictionary,
    r,
):
    for item in r:
        if chosenRecipeName == item["recipe"]["label"]:
            recipeNutritionDictionary = {
                "Item Name: ": chosenRecipeName,
                "Calories: ": recipeCalories,
                "Total Fat: ": recipeTotalFat,
                "Cholesterol: ": recipeCholesterol,
                "Sugar: ": recipeSugar,
                "Protein: ": item["recipe"]["totalNutrients"]["PROCNT"]["quantity"],
            }
            myList.append(recipeNutritionDictionary)
            return myList, recipeNutritionDictionary


# print nutrition info as dataframe + save to excel file created in intro3 function
def function13(
    seeNutritionInfo,
    chosenRecipeName,
    recipeCalories,
    recipeTotalFat,
    recipeCholesterol,
    recipeSugar,
    recipeProtein,
):
    if seeNutritionInfo == "yes" or seeNutritionInfo == "y":
        recipeNutritionPandas = [
            ["Item Name:", chosenRecipeName],
            ["Calories:", recipeCalories + " kcals"],
            ["Total Fat:", recipeTotalFat + " grams"],
            ["Cholesterol:", recipeCholesterol + " grams"],
            ["Sugar:", recipeSugar + " grams"],
            ["Protein:", recipeProtein + " grams"],
        ]
        # columns
        headerY = [
            "  ",
            "  ",
        ]
        # rows
        headerX = [
            "  ",
            "  ",
            "  ",
            "  ",
            "  ",
            "  ",
        ]

        df = pd.DataFrame(recipeNutritionPandas, headerX, headerY)
        print(df)

        # next note is to stop pylint from giving wrong error for pd
        with pd.ExcelWriter(  # https://github.com/PyCQA/pylint/issues/3060 pylint: disable=abstract-class-instantiated
            "nutritionalDatabase.xlsx", engine="openpyxl", mode="a"
        ) as f:
            df.to_excel(f, sheet_name=chosenRecipeName, index=False, header=False)

    elif seeNutritionInfo == "no" or seeNutritionInfo == "n":
        print("No problem!")


# closing message
def closing():
    print("Thank you for using our program. Stay healthy!")
    print(
        "Be sure to view the excel sheet titled 'compareSearches' to see all the nutrition data for your searches!"
    )


# main function
userMyName = intro1()
intro3()
exploreAgain = "yes" or "y"
while exploreAgain == "yes" or exploreAgain == "y":
    userDineInorOut = intro2(userMyName)
    if (
        userDineInorOut == "out"
        or userDineInorOut == "dine out"
        or userDineInorOut == "Dine out"
    ):
        exploreRestaurant = "yes" or "y"
        while exploreRestaurant == "yes" or exploreRestaurant == "y":
            userRestaurant = functionC()
            userN = functionD(userRestaurant)
            functionE(userN)
            userFoodItem = functionA(userN)
            myList = []
            selectedFood = {}
            functionB(userN, userFoodItem, myList)
            functionF(userN, myList, selectedFood, userFoodItem)
            userSearchLocation = functionG(userRestaurant)
            functionH(userSearchLocation, userRestaurant)
            print("Do you want to explore another restaurant?")
            exploreRestaurant = input()
    elif (
        userDineInorOut == "in"
        or userDineInorOut == "eat in"
        or userDineInorOut == "eat in"
    ):
        exploreRecipe = "yes" or "y"
        while exploreRecipe == "yes" or exploreRecipe == "y":
            userChosenFoodItem = function1()
            userRecipeData = function2(userChosenFoodItem)
            userR = function3(userRecipeData)
            function4(userR)
            userChosenRecipeName = function5(userChosenFoodItem)
            function6(userChosenRecipeName, userR)
            recipeNutritionDictionary = {}
            userSeeNutritionInfo = function7(userChosenRecipeName)
            userRecipeCalories = function8(userR, userChosenRecipeName)
            userRecipeTotalFat = function9(userR, userChosenRecipeName)
            userRecipeCholesterol = function10(userR, userChosenRecipeName)
            userRecipeSugar = function11(userR, userChosenRecipeName)
            userRecipeProtein = function12(userR, userChosenRecipeName)
            functionRecipeDictionary(
                recipeNutritionDictionary,
                userRecipeProtein,
                userRecipeCalories,
                userRecipeTotalFat,
                userRecipeCholesterol,
                userRecipeSugar,
                userChosenRecipeName,
                userR,
            )
            function13(
                userSeeNutritionInfo,
                userChosenRecipeName,
                userRecipeCalories,
                userRecipeTotalFat,
                userRecipeCholesterol,
                userRecipeSugar,
                userRecipeProtein,
            )
            print("Do you want to explore another recipe to cook?")
            exploreRecipe = input()
    print("Do you want to explore more dining options?")
    exploreAgain = input()
closing()
