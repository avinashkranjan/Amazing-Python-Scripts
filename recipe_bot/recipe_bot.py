import requests

def get_recipe(dish):
    api_key = "3433d479b6b54fcd90552b35da3f3a63" 
    endpoint = f"https://api.spoonacular.com/recipes/716429/information?includeNutrition=false"

    response = requests.get(endpoint)
    data = response.json()


    if "results" in data and len(data["results"]) > 0:
        recipe = data["results"][0]  # Get the first recipe
        return recipe
    else:
        return None

def generate_recipe_response(recipe):
    if recipe:
        response = f"Here's the recipe for {recipe['title']}: \n\n"
        response += "Ingredients:\n"
        for ingredient in recipe['ingredients']:
            response += "- " + ingredient + "\n"
        response += "\nInstructions:\n"
        response += recipe['instructions']
        return response
    else:
        return "Sorry, I couldn't find a recipe for that dish."

dish = input("Enter the name of a dish: ")
recipe = get_recipe(dish)
response = generate_recipe_response(recipe)
print(response)


