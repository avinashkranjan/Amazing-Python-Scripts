# Imports
# for soup find
from bs4 import BeautifulSoup as bs
# uses a automated web browser for automations
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Chrome options for selenium server
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


def get_Zomato_menu(zlink):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(zlink)
    current_zomato_data = {}
    for i in range(2, 20):
        try:
            category_name = driver.find_element(
                by=By.XPATH, value=f"/html/body/div[1]/div/main/div/section[4]/section/section[2]/section[{i}]/h4").get_attribute("innerHTML")
            if category_name != "" and category_name != "Recommended":
                items = []
                for j in range(1, 25):
                    try:
                        item_name = driver.find_element(
                            by=By.XPATH, value=f"/html/body/div[1]/div/main/div/section[4]/section/section[2]/section[{i}]/div[2]/div[{j}]/div/div/div[2]/div/div/h4").get_attribute("innerHTML")
                        try:
                            item_price = driver.find_element(
                                by=By.XPATH, value=f"/html/body/div[1]/div/main/div/section[4]/section/section[2]/section[{i}]/div[2]/div[{j}]/div/div/div[2]/div/div/div[2]/span").get_attribute("innerHTML")
                        except:
                            item_price = driver.find_element(
                                by=By.XPATH, value=f"/html/body/div[1]/div/main/div/section[4]/section/section[2]/section[{i}]/div[2]/div[{j}]/div/div/div[2]/div/div/div/span").get_attribute("innerHTML")
                        item_price = item_price[1:]
                        listing = [item_name, item_price]
                        items.append(listing)
                    except:
                        pass
                category_name_data = {}
                for i in items:
                    item_name = i[0]
                    item_price = i[1]
                    category_name_data[item_name] = item_price
                current_zomato_data[category_name] = category_name_data
        except:
            pass
    return current_zomato_data


print()

if __name__ == "__main__":
    print("Enter the URL of Zomato's restraunt: ")
    zlink = str(input())
    data = get_Zomato_menu(zlink)
    for i in data:
        category_name = i
        print("## ", category_name)
        print()
        items = data.get(i)
        for j in items:
            print(j, "  : ", items.get(j))
        print()
