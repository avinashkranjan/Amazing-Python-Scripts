# Weather App

This is a simple application that allows you to check the temperature of a city using web scraping from Google search results.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- Tkinter library (usually included with Python)

## Usage

1. Run the `weatherapp.py` script.
2. Enter the name of the city for which you want to check the temperature.
3. Click the "Get Temperature" button.
4. The temperature will be displayed below the button.

## Notes

- The application fetches the temperature information by performing a Google search for "weather in <city>". It then extracts the temperature details from the search results using web scraping techniques.
- The temperature displayed might vary depending on the structure and layout of Google's search results page.
- This application is for educational and demonstration purposes only and is not intended for commercial or production use.

## License

This project is licensed under the [MIT License](LICENSE).
