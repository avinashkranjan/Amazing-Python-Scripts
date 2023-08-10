import nltk
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample database of recipes
recipes = {
    "Spaghetti Carbonara": {
        "ingredients": "pasta, eggs, bacon, parmesan cheese, black pepper",
        "source_link": "https://www.example.com/spaghetti-carbonara",
        "preferences": ["non-vegetarian"],
        "instructions": "1. Cook pasta according to package instructions.\n2. In a separate bowl, whisk together eggs, grated parmesan cheese, and black pepper.\n3. In a skillet, cook bacon until crispy, then remove from heat.\n4. Toss cooked pasta with the bacon and bacon fat.\n5. Add the egg mixture to the pasta, tossing quickly to avoid scrambling the eggs. The heat from the pasta will cook the eggs and create a creamy sauce. Serve immediately.",
    },
    "Chicken Stir-Fry": {
        "ingredients": "chicken, broccoli, carrots, soy sauce, garlic, ginger",
        "source_link": "https://www.example.com/chicken-stir-fry",
        "preferences": ["non-vegetarian"],
        "instructions": "1. Heat oil in a wok or large skillet over high heat.\n2. Add chopped chicken and cook until browned and cooked through.\n3. Add minced garlic and grated ginger, stir for a minute.\n4. Add chopped vegetables (broccoli, carrots) and stir-fry until tender-crisp.\n5. Pour in soy sauce and toss everything together. Serve hot.",
    },
    "Caprese Salad": {
        "ingredients": "tomatoes, mozzarella cheese, basil, olive oil, balsamic vinegar",
        "source_link": "https://www.example.com/caprese-salad",
        "preferences": ["vegetarian"],
        "instructions": "1. Slice tomatoes and mozzarella cheese.\n2. Arrange tomato and mozzarella slices on a plate, alternating them.\n3. Drizzle with olive oil and balsamic vinegar.\n4. Sprinkle fresh basil leaves over the top. Serve as a refreshing salad.",
    },
    "Chocolate Brownies": {
        "ingredients": "chocolate, butter, sugar, eggs, flour, vanilla extract",
        "source_link": "https://www.example.com/chocolate-brownies",
        "preferences": ["vegetarian"],
        "instructions": "1. Preheat oven to 350°F (175°C). Grease a baking pan.\n2. In a microwave-safe bowl, melt chocolate and butter together.\n3. Stir in sugar, eggs, flour, and vanilla extract until well combined.\n4. Pour the batter into the prepared pan.\n5. Bake for about 25 minutes or until a toothpick inserted in the center comes out with moist crumbs. Let it cool before cutting into squares.",
    },
    "Mushroom Risotto": {
        "ingredients": "arborio rice, mushrooms, vegetable broth, onion, garlic, parmesan cheese",
        "source_link": "https://www.example.com/mushroom-risotto",
        "preferences": ["vegetarian"],
        "instructions": "1. In a large skillet, sauté chopped onion and minced garlic in olive oil until translucent.\n2. Add arborio rice and stir until coated with oil.\n3. Gradually add vegetable broth, one ladleful at a time, stirring until the liquid is absorbed.\n4. Stir in sliced mushrooms and continue adding broth until the rice is creamy and cooked.\n5. Stir in grated parmesan cheese and serve hot.",
    },
    "Grilled Salmon": {
        "ingredients": "salmon fillet, lemon, olive oil, garlic, dill, salt, pepper",
        "source_link": "https://www.example.com/grilled-salmon",
        "preferences": ["non-vegetarian"],
        "instructions": "1. Preheat grill to medium-high heat.\n2. Rub salmon fillet with olive oil and season with salt, pepper, and minced garlic.\n3. Place the salmon on the grill and cook for a few minutes on each side until it flakes easily with a fork.\n4. Squeeze fresh lemon juice over the salmon and sprinkle with chopped dill before serving.",
    },
    "Vegetable Curry": {
        "ingredients": "mixed vegetables, coconut milk, curry paste, onion, garlic, ginger",
        "source_link": "https://www.example.com/vegetable-curry",
        "preferences": ["vegetarian", "vegan"],
        "instructions": "1. In a large pot, sauté chopped onion, minced garlic, and grated ginger in oil until fragrant.\n2. Add mixed vegetables and cook for a few minutes.\n3. Stir in curry paste and cook for another minute.\n4. Pour in coconut milk and bring to a simmer until the vegetables are tender.\n5. Serve the vegetable curry over cooked rice.",
    },
    "Apple Pie": {
        "ingredients": "apples, sugar, flour, butter, cinnamon, pie crust",
        "source_link": "https://www.example.com/apple-pie",
        "preferences": ["vegetarian"],
        "instructions": "1. Preheat oven to 375°F (190°C).\n2. Peel and slice apples, then mix with sugar, cinnamon, and flour.\n3. Roll out pie crust and place it in a pie dish.\n4. Fill the pie crust with the apple mixture.\n5. Add small pieces of butter on top of the apples.\n6. Roll out another pie crust for the top, seal the edges, and cut slits for venting.\n7. Bake for about 45 minutes or until the crust is golden brown and the apples are tender.",
    },
}
# Instructions for each recipe
recipe_instructions = {
    "Spaghetti Carbonara": "...",  # Instructions for Spaghetti Carbonara
    "Chicken Stir-Fry": "...",  # Instructions for Chicken Stir-Fry
    "Caprese Salad": "...",  # Instructions for Caprese Salad
    "Chocolate Brownies": "...",  # Instructions for Chocolate Brownies
    "Mushroom Risotto": "...",  # Instructions for Mushroom Risotto
    "Grilled Salmon": "...",  # Instructions for Grilled Salmon
    "Vegetable Curry": "...",  # Instructions for Vegetable Curry
    "Apple Pie": "...",  # Instructions for Apple Pie
}

# Function to preprocess the recipes


def preprocess_recipe(recipe):
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(recipe.lower())
    return [word for word in tokens if word.isalpha() and word not in stop_words]

# Function to generate a unique recipe


def generate_recipe(ingredients, preferences=None):
    processed_ingredients = preprocess_recipe(ingredients)

    matching_recipes = []
    for name, recipe_info in recipes.items():
        if all(ingredient in recipe_info["ingredients"] for ingredient in processed_ingredients):
            if not preferences or any(pref in preferences for pref in recipe_info["preferences"]):
                matching_recipes.append(name)

    if not matching_recipes:
        return "Sorry, no recipe found with those ingredients and preferences. Try something else."

    generated_recipe_name = random.choice(matching_recipes)
    return generated_recipe_name, recipes[generated_recipe_name]["source_link"]

# Function to get user ingredient substitutions

# Function to suggest similar recipes


def suggest_similar_recipes(generated_recipe_name):
    similar_recipes = random.sample(
        [name for name in recipes.keys() if name != generated_recipe_name], 2)
    return similar_recipes

# Main function


def main():
    print("AI-Powered Recipe Generator")
    print("Available Recipes:")
    for idx, recipe_name in enumerate(recipes.keys(), start=1):
        print(f"{idx}. {recipe_name}")

    user_ingredients = input(
        "Enter the list of ingredients you have (comma-separated): ")
    user_preferences = input(
        "Enter your dietary preferences (comma-separated, or press Enter to skip): ").split(",")

    generated_recipe_name, source_link = generate_recipe(
        user_ingredients, user_preferences)

    print("\nGenerated Recipe:")
    print(f"Recipe: {generated_recipe_name}")
    print("Ingredients:", recipes[generated_recipe_name]["ingredients"])
    print("Instructions:")
    print(recipe_instructions[generated_recipe_name])
    print("Source Link:", source_link)

    similar_recipes = suggest_similar_recipes(generated_recipe_name)
    print("\nYou may also like these recipes:")
    for idx, recipe_name in enumerate(similar_recipes, start=1):
        print(f"{idx}. {recipe_name}")


if __name__ == "__main__":
    nltk.download("punkt")
    nltk.download("stopwords")
    main()
