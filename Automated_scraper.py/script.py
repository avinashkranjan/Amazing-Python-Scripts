import sys
import requests
from bs4 import BeautifulSoup
import time


def display_content(url, selector):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Create a BeautifulSoup object with the page content
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find all elements that match the CSS selector
            elements = soup.select(selector)
            # Return the content of the matched elements
            return [element.text for element in elements]
        else:
            print("Failed to fetch the webpage.")
    except requests.exceptions.RequestException as e:
        print("Error occurred while making the request:", e)
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    # Check if URL, selector, and interval are provided as arguments
    if len(sys.argv) < 4:
        print(
            "Usage: python script.py [URL] [CSS selector] [Interval in minutes]")
        sys.exit(1)

    # Get the URL, selector, and interval from command-line arguments
    url = sys.argv[1]
    selector = sys.argv[2]
    interval_minutes = int(sys.argv[3])

    # Store the initial contents
    initial_contents = display_content(url, selector)
    if initial_contents:
        print("Initial contents:")
        for content in initial_contents:
            print(content)
    else:
        print("No matching elements found.")

    while True:
        # Wait for the specified interval
        time.sleep(interval_minutes * 60)

        # Check for content changes
        current_contents = display_content(url, selector)
        if current_contents:
            # Compare with the initial contents
            if current_contents != initial_contents:
                print("Content has changed!")
                for content in current_contents:
                    print(content)
                # Update the initial contents with the current contents
                initial_contents = current_contents
            else:
                print("Content has not changed.")
        else:
            print("No matching elements found.")
