# from apatel import function12
import requests, json, sys, time
from pprint import pprint
import pandas


# This function includes the introduction information for the API
def intro():
    print("Welcome to the Nutritionix API Service.")
    # time.sleep(1)  # time.sleep adds time before the next line of code is printed
    print("What is your name?")
    myName = input()
    print("Hi " + myName + "!")
    # time.sleep(1)
    # print(
    #     "With this program you can either choose recipes to cook at home and eat in, or find menu items from a restaurant and dine out. "
    # )
    # time.sleep(3)
    # print(
    #     " Once you have selected your dining option, you will either get a full recipe and related nutritional information with the dine in option, or the nutritional information from a menu item at a selected restaurant."
    # )
    # time.sleep(3)
    # print("          ")
    # print(
    #     "If you decide to dine in...\n You can search pizza, for example, and have an entire recipe of how to make pizza in your kitchen from scratch!"
    # )
    # time.sleep(3)
    # print("          ")
    # print(
    #     "Or if you decide to dine out...\n  You can search Mcdonald's, for example, and select McNuggets.\n Then, information including calories, fats, cholesterol, sugar and protein for McNuggets will be given to you."
    # )
    # print("          ")
    # time.sleep(3)
    print("Now, " + myName + ", would you like to eat in or dine out?")
    # dineInOrOut = input()
    print("---------------")
    # return dineInOrOut


# this function asks the player which restaurants data they want to look at and returns food items sold at the restaurant selected
def restaurant1():
    while (
        True
    ):  # this While loop will continue to run until the player quits out of the game, the game is ended by the break in line 16
        print("please enter a restaurant or food brand name")
        chosenRestaurant = input(
            "Restaurant/brand name or (q)uit>"
        )  # user will input a restaurant name and the API will search relevant information from the restaurant
        if chosenRestaurant.lower() == "q":
            break
    return chosenRestaurant


# API for Restaurant choice
def restaurant2(chosenRestaurant):
    # This URL calls the API with the search by 'restaurant' function and names it URL.
    # When a 'restaurant' is chosen, the adjusted url returns a dictionary within a list of food item names for that specific restaurant/brand
    url = f"https://api.nutritionix.com/v1_1/search/{chosenRestaurant}?results=0:20&fields=item_name,nf_calories,nf_calories_from_fat,nf_total_fat,nf_saturated_fat,nf_cholesterol,nf_sugars,nf_protein&appId=f3b374ec&appKey=988ab0bd10dc4a886738973eec0524d1"
    response = requests.get(url)
    response.raise_for_status()  # check for errors

    # Load json data into a python variable
    nutritionData = json.loads(response.text)
    # variable 'n' looks into
    n = nutritionData["hits"]
    return n


# This function asks for a food item that the restaurant selected has and outputs nutrition information
def restaurant3(foodList):
    # The while loop allows for people to select more than one food item at once
    while True:
        print(
            "please enter which item name you want to see nutrition information for from the list below or enter q(uit)"
        )
        foodItem = input()
        if (
            foodItem == "q"
        ):  # if the user enter q the program will quit out of the foodItem function
            break
        # selectedFood is a dictionary
        # selectedFood includes different pieces of information: item name, calories, calories from fat, total fat, saturated fat, cholesterol, sugars, protein
        selectedFood = {}
        for item in foodList:
            if foodItem == item["fields"]["item_name"]:
                selectedFood = {
                    "name": item["fields"]["item_name"],
                    "calories": str(item["fields"]["nf_calories"]) + " calories",
                    # "calories from fat": str(item["fields"]["nf_calories_from_fat"])
                    # + " calories from fat",
                    "total fat": str(item["fields"]["nf_total_fat"])
                    + " grams of total fat",
                    # "saturated fat": str(item["fields"]["nf_saturated_fat"])
                    # + " grams of saturated fat",
                    "cholesterol": str(item["fields"]["nf_cholesterol"])
                    + " grams of cholesterol",
                    "sugars": str(item["fields"]["nf_sugars"]) + " grams of sugar",
                    "protein": str(item["fields"]["nf_protein"]) + " grams of protein",
                }
                # this adds the information gathered from selectedFood to a list called myList
                # myList prints all of the food items selected with their corresponding nutritional information after the user quits out of the program
                myList.append(selectedFood)

        for field in selectedFood:
            print(
                selectedFood[field]
            )  # this print statement will print the nutritional information for the food item selected
    return foodItem


# print menu
def restaurant4(n, foodItem):
    for item in n:
        print(
            item["fields"]["item_name"],
        )
    foodItem(n)


# main function LETS GO
# userDineInOrOut = intro()
intro()
userChosenRestaurant = restaurant1()
userN = restaurant2(userChosenRestaurant)
myList = []
userFoodItem = restaurant3(userN)
restaurant4(userN, userFoodItem)
