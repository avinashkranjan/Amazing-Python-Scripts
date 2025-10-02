import requests

# Function to get the nutrition info of the food item
# Using the calorie ninja api

def get_nutrition_info(food: str):
    '''
    Retrieves nutritional information of food item, 
    Returns None if food item is invalid
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
    Takes in a dictionary of items 
    and prints the contents in a legible format
    '''

    # prints items in a hierarchical format.
    for fact in facts:
        # Do not indent name, indent everything else
        if fact == "name":
            print(f"{fact}: {facts[fact]}")
        else:
            print(f"\t{fact}: {facts[fact]}")



if __name__ == "__main__":
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