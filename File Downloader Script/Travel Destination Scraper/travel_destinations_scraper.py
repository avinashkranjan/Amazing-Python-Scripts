import requests
from bs4 import BeautifulSoup


def scrape_travel_destinations():
    # Replace with the actual URL of the travel destinations page
    url = "https://www.example.com/destinations"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    destinations = []

    # Find the HTML elements containing the destination information
    destination_elements = soup.find_all("div", class_="destination")

    for element in destination_elements:
        # Extract the desired information from each destination element
        name = element.find("h2").text.strip()
        description = element.find("p").text.strip()
        image_url = element.find("img")["src"]

        # Create a dictionary for each destination
        destination = {
            "name": name,
            "description": description,
            "image_url": image_url
        }

        # Append the destination dictionary to the list
        destinations.append(destination)

    return destinations


# Call the function to scrape travel destinations
travel_destinations = scrape_travel_destinations()

# Print the scraped destinations
for destination in travel_destinations:
    print("Destination: ", destination["name"])
    print("Description: ", destination["description"])
    print("Image URL: ", destination["image_url"])
    print("------------------------")
