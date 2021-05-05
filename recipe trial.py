import requests, json, sys, time
from pprint import pprint
import pandas


def recipeFunction():
    print(
        "please enter what food item you would like to cook, and we will provide the recipe"
    )
    recipe = input("recipe name or (q)uit>")
    # if recipe.lower() == "q":
    #             break

    url = f"https://api.edamam.com/search?q={recipe}&app_id=62fd6c39&app_key=5f0e27adae50eb576e4aebe320bbefe2"

    response = requests.get(url)
    response.raise_for_status()  # check for errors

    recipeData = json.loads(response.text)
    r = recipeData["hits"]

    for item in r:
        print(item["recipe"]["label"])
        for ingredient in item["recipe"]["ingredientLines"]:
            print(ingredient)


# main program
recipeFunction()
