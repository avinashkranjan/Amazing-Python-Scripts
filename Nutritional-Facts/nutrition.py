import requests
import json

# Function to get the nutrition info of the food item
# Using the calorie ninja api
def get_nutrition_info (food: str):
    '''
    Retrieves nutritional information of food item, 
    Returns None if food item is invalid
    '''

    api_url = f"https://api.calorieninjas.com/v1/nutrition?query={food}"

    response = requests.get(api_url, headers={"X-API-key": "YOUR-API-KEY"})

    # Checking if the request was a 200 or an error.
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        return data["items"]
    else:
        print("Error:". response.status_code, response.text )
        return None


def print_info(items : dict):
    '''
    Takes in a dictionary of items 
    and prints the contents in a legible format
    '''

    # prints items in a hierarchical format.
    for item in items:
        if item == "name":
            print(f"{item}: {items[item]}")
        else:
            print(f"\t{item}: {items[item]}")



if __name__ == "__main__":
    
    # main loop
    while True:
        print("Enter food query: ", end="")
        query = input()

        if query.lower() == "q" or query.lower() == "quit":
            print("Thank you for using the Nutrition script!")
            break

        items = get_nutrition_info(query)
        # Checks if the query entered was invalid or valid
        if not items:
            print("Please try another query!\n")
        else:
            for item in items:
                print_info(item)
                print("\n")
        