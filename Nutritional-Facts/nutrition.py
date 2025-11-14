import requests
'''
Nutritional Info Script

The script will be able to retrieve the nutrional facts about foods 
using the CalorieNinjas API. Users can enter a food query and receive detailed
nutrional facts like calories, protein, fat etc.
'''


# Function to get the nutrition info of the food item
# Using the calorie ninja api

def get_nutrition_info(food: str):
    '''
    Retrieves nutritional information of food item, 
    Args:
        food (str): Name of food (apple, chucken)
    Returns:
        list[dict] | None: A list of nutritional fact dictionaries if found otherwise None
    '''

    # API Call URL
    api_url = f"https://api.calorieninjas.com/v1/nutrition?query={food}"

    # Request call to send to API,
    # Takes in the api url, headers with api-key and a timeout 
    # so the request doesn't run forever
    response = requests.get(api_url, headers={"X-API-key": "YOUR-API-KEY"}, timeout=30)

    # Checking if the request was a 200 or an error.
    if response.status_code == requests.codes.ok:
        data = response.json()
        return data["items"]
    
    # Prints error if response was bad
    print("Error:", response.status_code, response.text )
    return None


def print_info(facts : dict):
    '''
    Prints the nutritional information in a legible format

    Args:
        facts (dict): A dictionary of nutrition facts for a single food item
    '''

    # prints items in a hierarchical format.
    for fact in facts:
        # Do not indent name, indent everything else
        if fact == "name":
            print(f"{fact}: {facts[fact]}")
        else:
            print(f"\t{fact}: {facts[fact]}")



def main():
    '''
        Main loop, for the nutrition script
        Infintely prompts user for food queries
        until user quits
    '''

    # main loop
    while True:
        # Print opening message
        print("Enter food query: ", end="")
        query = input()

        # Lower casing the query to normalize the checks
        if query.lower() == "q" or query.lower() == "quit":
            print("Thank you for using the Nutrition script!")
            break
        
        # same thing here
        items = get_nutrition_info(query.lower())
        # Checks if the query entered was invalid or valid
        if not items:
            print("Please try another query!\n")
        else:
            # Looping through each item to print them out in neat format
            for item in items:
                print_info(item)
                print("\n")

if __name__ == "__main__":
    main()