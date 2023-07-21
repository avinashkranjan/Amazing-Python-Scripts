from selenium import webdriver
from selenium.webdriver.common.by import By
import time
cookies_per_sec = 0


def cookie_click():
    buy_time = time.time()+5.0
    while (time.time() < buy_time):
        cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")
        cookie.click()
    purchase_item()


def purchase_item():
    global cookies_per_sec
    current_money = (driver.find_element(By.CSS_SELECTOR, "#cookies").text)
    current_money = (current_money.split(" "))
    cookies_per_sec = (current_money[1])
    current_money = int(current_money[0])
    purchase_list = driver.find_elements(
        By.CSS_SELECTOR, "#products .unlocked")
    for i in range(len(purchase_list)):
        last_item_price = int(driver.find_element(
            By.CSS_SELECTOR, f"#productPrice{len(purchase_list)-1}").text)
        if int(current_money) > last_item_price:
            purchase_list[-1].click()
            current_money -= last_item_price


chrome_driver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(7)
language_click = driver.find_element(By.CSS_SELECTOR, "#langSelect-EN")
language_click.click()

time.sleep(7)
end_time = time.time()+300.0
while (time.time() < end_time):
    cookie_click()

print("Cookie Clicker Ended")
print(f"Rate achieved is {cookies_per_sec} ")
