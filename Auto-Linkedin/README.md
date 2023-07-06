## Auto Linkedin

- It imports the necessary modules: 
    - webdriver from Selenium to control the web browser, 
    - Keys from Selenium to handle keyboard keys, and pyautogui as pag to simulate mouse clicks.

- The main() function sets up the Selenium WebDriver with the Chrome browser and opens the LinkedIn website.

- The login() function finds the login elements on the LinkedIn page and enters the provided username and password. 

- It also clicks the submit button to log in.

- The goto_network() function clicks on the "My Network" tab on the LinkedIn page.

- The send_requests() function prompts the user to enter the number of connection requests they want to send. 

- It then uses the PyAutoGUI library to simulate mouse clicks on the connection button (at the specified position) the specified number of times.

- Install this before running : 
    1. pip install selenium
    2. pip install pyautogui

Once you have installed the necessary libraries and downloaded the Chrome WebDriver, you should be able to run the code successfully.

**Thanks for using this program**

