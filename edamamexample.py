import requests, json, sys, time


class Edamam(object):
    """ low level api returning raw json data"""

    def __init__(
        self,
        # keys scrapped from web demos
        nutrition_appid="62fd6c39",
        nutrition_appkey="5f0e27adae50eb576e4aebe320bbefe2",
        recipes_appid=None,
        recipes_appkey=None,
        #  food_appid="07d50733",
        #  food_appkey="80fcb49b500737827a9a23f7049653b9"
    ):
        self.nutrition_appid = nutrition_appid
        self.nutrition_appkey = nutrition_appkey
        self.recipes_appid = recipes_appid
        self.recipes_appkey = recipes_appkey
        # self.food_appid = food_appid
        # self.food_appkey = food_appkey

    def search_recipe(self, query="chicken"):
        url = (
            "https://api.edamam.com/search?q="
            + query
            + "&app_id="
            + self.recipes_appid
            + "&app_key="
            + self.recipes_appkey
        )

        r = requests.get(url)
        if r.status_code == 401:
            logger.error("invalid recipe api key")
            raise InvalidRecipeApiKey
        return r.json()

    def search_nutrient(self, ingredients=None):
        ingredients = ingredients or []
        if isinstance(ingredients, str):
            ingredients = [ingredients]

        url = (
            "https://api.edamam.com/api/nutrition-details?app_id={id}"
            "&app_key={key}".format(id=self.nutrition_appid, key=self.nutrition_appkey)
        )

        data = {"ingr": ingredients}
        r = requests.post(
            url, headers={"Content-Type": "application/json"}, data=json.dumps(data)
        )

        if r.status_code == 401:
            logger.error("invalid nutrients api key")
            raise InvalidNutrientsApiKey

        data = r.json()
        if data.get("error"):
            if data["error"] == "low_quality":
                logger.error("could not understand query")
                raise LowQualityQuery
            else:
                raise APIError
        return data