from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

"""
Example code :
    python_scraper = Courses("python",5)
    print(python_scraper.scrape_all())
"""


class Courses:
    def __init__(self, keyword, page_count):
        self.keyword = keyword
        self.page_count = page_count

    def __scrape_page(self):
        chromedriver_path = ''
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(
            chromedriver_path), options=options)
        wait = WebDriverWait(driver, 100)
        driver.get('https://www.coursera.org/search?query=' + self.keyword)
        return wait, driver

    def scrape_all(self):
        wait, driver = self.__scrape_page()
        courses_data = []
        try:
            j = 0
            for i in range(self.page_count):
                courses = wait.until(EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, 'main ul>li')))
                for course in courses:
                    title = driver.execute_script(
                        'return arguments[0].querySelector("h3")?.innerText', course)
                    description = driver.execute_script(
                        'return arguments[0].querySelector("p>span")?.innerText', course)
                    review = driver.execute_script(
                        'return arguments[0].querySelector("div:has(>svg)")?.innerText.replace("\\n\\n","⭐")', course)
                    url = driver.execute_script(
                        'return String(arguments[0].querySelector("a")?.href)', course)
                    data = {"id": j, "title": title,
                            "description": description, "review": review, "url": url}
                    courses_data += [data]
                    j += 1
                next_btn = driver.find_element(
                    By.CSS_SELECTOR, 'button[aria-label="Next Page"]')
                if 'disabled' in next_btn.get_attribute('class'):
                    print('There are no more pages')
                    break
                else:
                    next_btn.click()
            return {
                "data": courses_data,
                "message": f"Course Titles for {self.keyword}"
            }
        except:
            return {
                "data": None,
                "message": f"No courses found for {self.keyword}"
            }

    def course_titles(self):
        wait, driver = self.__scrape_page()
        titles = []
        try:
            for i in range(self.page_count):
                courses = wait.until(EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, 'main ul>li')))
                titles.extend([driver.execute_script(
                    'return arguments[0].querySelector("h3")?.innerText', course) for course in courses])
                next_btn = driver.find_element(
                    By.CSS_SELECTOR, 'button[aria-label="Next Page"]')
                if 'disabled' in next_btn.get_attribute('class'):
                    print('There are no more pages')
                    break
                else:
                    next_btn.click()
            return {
                "data": titles,
                "message": f"Course Titles for {self.keyword}"
            }
        except:
            return {
                "data": None,
                "message": f"No courses found for {self.keyword}"
            }

    def course_description(self):
        wait, driver = self.__scrape_page()
        descriptions = []
        try:
            for i in range(self.page_count):
                courses = wait.until(EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, 'main ul>li')))
                descriptions.extend([driver.execute_script(
                    'return arguments[0].querySelector("p>span")?.innerText', course) for course in courses])
                next_btn = driver.find_element(
                    By.CSS_SELECTOR, 'button[aria-label="Next Page"]')
                if 'disabled' in next_btn.get_attribute('class'):
                    print('There are no more pages')
                    break
                else:
                    next_btn.click()
            return {
                "data": descriptions,
                "message": f"Course Titles for {self.keyword}"
            }
        except:
            return {
                "data": None,
                "message": f"No courses found for {self.keyword}"
            }

    def course_reviews(self):
        wait, driver = self.__scrape_page()
        reviews = []
        try:
            for i in range(self.page_count):
                courses = wait.until(EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, 'main ul>li')))
                reviews.extend([driver.execute_script(
                    'return arguments[0].querySelector("div:has(>svg)")?.innerText.replace("\\n\\n","⭐")', course) for course in courses])
                next_btn = driver.find_element(
                    By.CSS_SELECTOR, 'button[aria-label="Next Page"]')
                if 'disabled' in next_btn.get_attribute('class'):
                    print('There are no more pages')
                    break
                else:
                    next_btn.click()
            return {
                "data": reviews,
                "message": f"Course Titles for {self.keyword}"
            }
        except:
            return {
                "data": None,
                "message": f"No courses found for {self.keyword}"
            }

    def course_urls(self):
        wait, driver = self.__scrape_page()
        urls = []
        try:
            for i in range(self.page_count):
                courses = wait.until(EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, 'main ul>li')))
                urls.extend([driver.execute_script(
                    'return String(arguments[0].querySelector("a")?.href)', course) for course in courses])
                next_btn = driver.find_element(
                    By.CSS_SELECTOR, 'button[aria-label="Next Page"]')
                if 'disabled' in next_btn.get_attribute('class'):
                    print('There are no more pages')
                    break
                else:
                    next_btn.click()
            return {
                "data": urls,
                "message": f"Course Titles for {self.keyword}"
            }
        except:
            return {
                "data": None,
                "message": f"No courses found for {self.keyword}"
            }


python_scraper = Courses("python", 5)
print(python_scraper.scrape_all())
