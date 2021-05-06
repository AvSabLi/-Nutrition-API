import requests, json, sys, time
from pprint import pprint
import pandas


# This function asks for a food item that the restaurant selected has and outputs nutrition information
def functionA(n):
    # The while loop allows for people to select more than one food item at once
    # while True:
    print(
        "please enter which item name you want to see nutrition information for from the list below or enter q(uit)"
    )
    foodItem = input()
    # if (
    #     foodItem == "q"
    # ):  # if the user enter q the program will quit out of the foodItem function
    # break
    return foodItem


def functionB(n, foodItem):
    for item in n:
        if foodItem == item["fields"]["item_name"]:
            selectedFood = {
                "name": item["fields"]["item_name"],
                "calories": str(item["fields"]["nf_calories"]) + " calories",
                "calories from fat": str(item["fields"]["nf_calories_from_fat"])
                + " calories from fat",
                # "calories from fat": str(item["fields"]["nf_calories_from_fat"])
                # + " calories from fat",
                "total fat": str(item["fields"]["nf_total_fat"])
                + " grams of total fat",
                "saturated fat": str(item["fields"]["nf_saturated_fat"])
                + " grams of saturated fat",
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
    return selectedFood


# need to ask if dine in or eat out with related code
# this function asks the player which restaurants data they want to look at and returns food items sold at the restaurant selected
def functionC():
    # while (
    #     True
    # ):  # this While loop will continue to run until the player quits out of the game, the game is ended by the break in line 16
    print("Please enter a restaurant name.")
    restaurant = input(
        "Restaurant/brand name or (q)uit>"
    )  # user will input a restaurant name and the API will search relevant information from the restaurant
    # if restaurant.lower() == "q":
    #     break
    return restaurant


def functionD(restaurant):
    # This URL calls the API with the search by 'restaurant' function and names it URL.
    # When a 'restaurant' is chosen, the adjusted url returns a dictionary within a list of food item names for that specific restaurant/brand
    url = f"https://api.nutritionix.com/v1_1/search/{restaurant}?results=0:20&fields=item_name,nf_calories,nf_calories_from_fat,nf_total_fat,nf_saturated_fat,nf_cholesterol,nf_sugars,nf_protein&appId=f3b374ec&appKey=988ab0bd10dc4a886738973eec0524d1"
    response = requests.get(url)
    response.raise_for_status()  # check for errors
    # Load json data into a python variable
    nutritionData = json.loads(response.text)
    # variable 'n' looks into
    n = nutritionData["hits"]
    return n


# printing restaurant menu
def functionE(n):
    for item in n:
        print(
            item["fields"]["item_name"],
        )


# print pandas table
def functionF(n, myList, selectedFood):
    print("Here are the nutrition facts for the food items you selected:\n")
    time.sleep(2)
    # print("---------------")
    # print(" ")
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
            "  ",
            "  ",
            "  ",
            # "  ",
            # "  ",
        ]
        print(pandas.DataFrame(foodData, headerX, headerY))


def functionG(restaurant):
    print("Do you want to find the nearest " + restaurant + "?")
    searchLocation = input()
    return searchLocation


# print URL if user says yes
def functionH(searchLocation, restaurant):
    if searchLocation == "yes" or searchLocation == "y":
        # Fetch the information of that restaurant
        map_url = f"https://www.google.com/maps/search/?api=1&query={restaurant}"
        # Print message
        print("To view " + searchLocation + " in Google Maps, go to " + map_url)
        print("-----------------------------------------")
        return map_url
    elif searchLocation == "no" or searchLocation == "n":
        pass


# maincode
userRestaurant = functionC()
userN = functionD(userRestaurant)
functionE(userN)
userFoodItem = functionA(userN)
myList = []
selectedFood = {}
functionB(userN, userFoodItem)
functionF(userN, myList, selectedFood)
# fix URL
userSearchLocation = functionG(userRestaurant)
functionH(userSearchLocation, userRestaurant)
