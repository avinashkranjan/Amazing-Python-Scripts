# Facebook-AutoLogin

## About This Project
This is a python script that automates the facebook login process

## How To Run

To run the script use following commands

1. Get the required modules
    ```bash
    pip install -r requirements.txt
    ```

2. Add your email/username in place of username@email.com
    ```python
    driver.find_element_by_id("email").send_keys("username@email.com")
    ```
3. Add your password in the following line
    ```python
    driver.find_element_by_id("pass").send_keys("password")
    ```
4. Run chromedriver.exe , located in
    ```bash
    Facebook-AutoLogin/chromedriver.exe
    ```

5. Run the python script
    ```python
    python facebookAuto.py
    ```

