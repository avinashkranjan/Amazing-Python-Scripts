# Telegram Web Get-Group-Members Bot

Automate the process of retrieving member information from a Telegram group using this Python script. The script utilizes the Selenium library to interact with Telegram Web and extract member details.

## Installation

1. Ensure you have Python installed on your system.
2. Clone this repository or download the provided code:

    ```bash
    git clone [https://github.com/avinashkranjan/Amazing-Python-Scripts]
    ```

3. Navigate to the project directory:

    ```bash
    cd Telegram Get-Group-Members Bot/telegram.py
    ```
4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
5. Download the [ChromeDriver](https://chromedriver.chromium.org/downloads) suitable for your Chrome version and place it in the project directory.

## Usage

1. Make sure you have a compatible version of Chrome installed on your system.
2. Run the script:

    ```bash
    python telegram.py
    ```
3. A Chrome browser window will open, displaying Telegram Web.
4. Scan the QR code using your phone to log in to Telegram Web.
5. After successful login, the script will wait for 10 seconds to load the page.
6. Enter the name of the group you want to retrieve member information for when prompted.
7. The script will print the member names and images on the terminal.

## Notes

- This script uses the Chrome WebDriver for Selenium automation. Ensure that the `chromedriver` executable matches your Chrome browser version and is located in the project directory.
- The script waits for 10 seconds to ensure proper loading of the Telegram Web page before interaction. You can modify this delay if necessary.

## Contributor

- [Juhi Bhojani](https://github.com/Juhibhojani)

