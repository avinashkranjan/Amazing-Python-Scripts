import random

# some common food predefined instruction  
recipe_database = {
    "spaghetti bolognese": {
        "ingredients": ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic", "olive oil"],
        "instructions": [
            "Cook spaghetti according to package instructions.",
            "In a large skillet, heat olive oil over medium heat.",
            "Add chopped onion and minced garlic to the skillet. Cook until softened.",
            "Add ground beef and cook until browned.",
            "Stir in tomato sauce and simmer for 10 minutes.",
            "Serve the bolognese sauce over cooked spaghetti."
        ]
    },
    "chicken stir-fry": {
        "ingredients": ["chicken breast", "soy sauce", "ginger", "garlic", "vegetables", "vegetable oil"],
        "instructions": [
            "Cut chicken breast into small pieces.",
            "In a wok or skillet, heat vegetable oil over high heat.",
            "Add minced ginger and garlic. Stir-fry for a minute.",
            "Add chicken and cook until no longer pink.",
            "Add vegetables and cook until tender-crisp.",
            "Pour soy sauce over the mixture and stir-fry for an additional minute.",
            "Serve the chicken stir-fry with rice or noodles."
        ]
    },
    # to  Add more recipes here
}
# this function generates a formatted content containing the ingredients and instructions for the recipe.
def get_recipe(dish_name):
    recipe = recipe_database.get(dish_name.lower())
    if recipe:
        return recipe
    else:
        return None

def generate_recipe_response(recipe):
    if recipe:
        response = f"Here's the recipe for {recipe}: \n\n"
        response += "Ingredients:\n"
        for ingredient in recipe["ingredients"]:
            response += "- " + ingredient + "\n"
        response += "\nInstructions:\n"
        for step, instruction in enumerate(recipe["instructions"], start=1):
            response += str(step) + ". " + instruction + "\n"
        return response
    else:
         return "Sorry, We don't have the recipe for that dish\nPlease!look for another one."


dish = input("Enter the name of a dish: ")
recipe = get_recipe(dish)
response = generate_recipe_response(recipe)
print(response)
