import requests, json, sys, time
from pprint import pprint
<<<<<<< HEAD
import pandas

# from axios import axios
=======
>>>>>>> 4651e08bbe9b6214684fec60f591570a813d5d5f


# This function includes the introduction information for the API
def intro():
    print("Welcome to the Nutritionix API Service.")
    time.sleep(1)  # time.sleep adds time before the next line of code is printed
    print("What is your name?")
    myName = input()
    print("Hi " + myName + "!")
    time.sleep(1)
    print(
        "With this API service you can search food item's nutritional information from a selected restaurant or food brand. "
    )
    time.sleep(3)
    print(
        "For example:\n You can search Mcdonald's and select McNuggets.\n Then, information including calories, fats, cholesterol, sugar and protein  for McNuggets will be given to you."
    )
    time.sleep(3)
    print("---------------")


# this function asks the player which restaurants data they want to look at and returns food items sold at the restaurant selected
def restaurant():
    while (
        True
    ):  # this While loop will continue to run until the player quits out of the game, the game is ended by the break in line 16
        print("please enter a restaurant or food brand name")
        restaurant = input(
            "Restaurant/brand name or (q)uit>"
        )  # user will input a restaurant name and the API will search relevant information from the restaurant
        if restaurant.lower() == "q":
            break

        # This URL calls the API with the search by 'restaurant' function and names it URL.
        # When a 'restaurant' is chosen, the adjusted url returns a dictionary within a list of food item names for that specific restaurant/brand
        url = f"https://api.nutritionix.com/v1_1/search/{restaurant}?results=0:20&fields=item_name,nf_calories,nf_calories_from_fat,nf_total_fat,nf_saturated_fat,nf_cholesterol,nf_sugars,nf_protein&appId=f3b374ec&appKey=988ab0bd10dc4a886738973eec0524d1"
        response = requests.get(url)
        response.raise_for_status()  # check for errors

        # Load json data into a python variable
        nutritionData = json.loads(response.text)
        # variable 'n' looks into
        n = nutritionData["hits"]
        for item in n:
            print(
                item["fields"]["item_name"],
            )

        foodItem(n)


def recipe():
    while True:
        print(
            "please enter what food item you would like to cook, and we will provide the recipe"
        )
        recipe = input("recipe name or (q)uit>")
        if recipe.lower() == "q":
            break

        url = f"https://api.edamam.com/search?q={recipe}&app_id=62fd6c39&app_key=5f0e27adae50eb576e4aebe320bbefe2"

        response = requests.get(url)
        response.raise_for_status()  # check for errors

        recipeData = json.loads(response.text)
        r = recipeData["hits"]
        for item in r:
            print(item["recipe"]["label"])
            for ingredient in item["recipe"]["ingredientLines"]:
                print(ingredient)

            break

        foodItem(r)


# This function asks for a food item that the restaurant selected has and outputs nutrition information
def foodItem(foodList):
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
                    "calories from fat": str(item["fields"]["nf_calories_from_fat"])
                    + " calories from fat",
                    "total fat": str(item["fields"]["nf_total_fat"])
                    + " grams of total fat",
                    "saturated fat": str(item["fields"]["nf_saturated_fat"])
                    + " grams of saturated fat",
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


# this is the main program
intro()
myList = []
time.sleep(1)
restaurant()
recipe()
run()
print("Here are the nutrition facts for the food items you selected:\n")
time.sleep(2)
print("---------------")
print(" ")
#'with open' exports items in my list to a separate file and prints the output in the file
with open("Nutrition List2.txt", "w") as f:
    # This for loops prints all of the food items and their nutritional information at once, once the user quits out of the program
    for item in myList:
        # details = {"Item Name": [item["item_name"]]}
        # data = {"name": ["muffin", "burger"], "calories": [100, 200]}
        # dframe = pd.DataFrame(data)

        # dframe = pd.DataFrame(
        #     myList,
        #     columns=[
        #         "Item Name",
        #         "Calories",
        #         "Calories from Fat",
        #         "Total Fat",
        #         "Saturated Fat",
        #         "Cholesterol",
        #         "Sugar",
        #         "Protein",
        #     ],
        #     facts=["item_name", "nf_calories"],
        # )

        # print(dframe)

        # avani
        foodData = [
            [
                "Item Name",
                "Calories",
                "Calories from Fat",
                "Total Fat",
                "Saturated Fat",
                "Cholesterol",
                "Sugar",
                "Protein",
            ],
            [
                item["name"],
                item["calories"],
                item["calories from fat"],
                item["total fat"],
                item["saturated fat"],
                item["cholesterol"],
                item["sugars"],
                item["protein"],
            ],
        ]
        headerY = [
            "  ",
            "  ",
            "  ",
            "  ",
            "  ",
            "  ",
            "  ",
            "  ",
        ]
        headerX = [
            "  ",
            "  ",
            "  ",
            "  ",
            "  ",
            "  ",
            "  ",
            "  ",
        ]
        print(pandas.DataFrame(foodData, headerY, headerX))
        # print(_________________)

        # df.describe()

        # data = [
        # item["name"],
        # item["calories"],
        # item["calories from fat"],
        # item["total fat"],
        # item["saturated fat"],
        # item["cholesterol"],
        # item["sugars"],
        # item["protein"],
        # ]
        # headers = [
        # "calories",
        # "calories from fat",
        # "total fat",
        # "saturated fat",
        # "cholesterol",
        # "sugars",
        # "protein",
        # ]
        # print(pandas.DataFrame(data, headers, headers))

        print(item["name"])
        print(item["calories"])
        print(item["calories from fat"])
        print(item["total fat"])
        print(item["saturated fat"])
        print(item["cholesterol"])
        print(item["sugars"])
        print(item["protein"])
        print("---------------")

        f.write(str(item["name"]) + "\n")
        f.write(str(item["calories"]) + "\n")
        f.write(str(item["calories from fat"] + "\n"))
        f.write(str(item["total fat"] + "\n"))
        f.write(str(item["saturated fat"] + "\n"))
        f.write(str(item["cholesterol"] + "\n"))
        f.write(str(item["sugars"]) + "\n")
        f.write(str(item["protein"] + "\n"))
        f.write("---------------\n")
print("Your list has been printed to a file. Thanks for using the Nutritionix API!")

# google URL code
def function1():
    print("Which location would you like to search?")
    searchLocation = input()
    return searchLocation


def function2(searchLocation):
    # Fetch the information of that restaurant
    map_url = "https://www.google.com/maps/search/?api=1&query=" + searchLocation

    # Print message
    print("To view " + searchLocation + " in Google Maps, go to " + map_url)
    print("-----------------------------------------")
    return map_url


# main program
userSearchLocation = function1()
userMapsUrl = function2(userSearchLocation)
