from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import os
from fpdf import FPDF

options = webdriver.ChromeOptions()
options.add_argument("--headless")


capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

print("Enter Chrome Driver path: ")
input_driver_path = input()
driver = webdriver.Chrome(input_driver_path)
# the base url of leetcode problem set page
baseurl = "https://leetcode.com/problemset/all"
wait = WebDriverWait(driver, 15)

# the difficulty level of all the of all the problems
problem_difficulty = {"Easy": "?difficulty=Easy",
                      "Medium": "?difficulty=Medium", "Hard": "?difficulty=hard"}


def get_problem(category, no_of_problems):

    prblm_info = {}
    try:
        # checking if there is no network or any other iisue
        driver.get(baseurl + '/' + category)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='question-app']/div/div[2]/div[2]/div[2]/table/tbody[1]/tr[1]")))
    except TimeoutException as exception:
        print("Couldn't fetch problem. Network issue or page slow to render. Try again")
        os._exit(-1)

    for problem_index in range(1, no_of_problems + 1):
        # set problem name
        problem_name = driver.find_element_by_xpath(
            "//*[@id='question-app']/div/div[2]/div[2]/div[2]/table/tbody[1]/tr[{}]/td[3]".format(problem_index)).text
        # set problem url
        problem_url = driver.find_element_by_xpath(
            "//*[@id='question-app']/div/div[2]/div[2]/div[2]/table/tbody[1]/tr[{}]/td[3]/div/a".format(problem_index)).get_attribute('href')
        print(problem_name, " ", problem_url)
        prblm_info[problem_name] = problem_url
    return prblm_info


def get_description(problem_url, problem_name):
    try:
        # check if the element is founded, and located in the correct format
        driver.get(problem_url)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='app']/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/div/p[1]")))
        problem_title = problem_name
        problem_statement = driver.find_element_by_xpath(
            "//*[@id='app']/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/div/p[1]").text
        problem_test_cases = driver.find_element_by_xpath(
            "//*[@id='app']/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/div/pre[1]").text

        if (problem_test_cases.find("Output") == -1):
            problem_test_cases = "Input\n" + problem_test_cases
            problem_test_cases += "\nOutput\n"
            problem_test_cases += driver.find_element_by_xpath(
                "//*[@id='problem-statement']/pre[2]").text

        else:
            driver.execute_script("window.stop();")
        problem = {'title': problem_title, 'statement': problem_statement,
                   'test_case': problem_test_cases, 'url': problem_url}
        return problem

    except NoSuchElementException as e:
        print("Couldn't scrap the element, Unable to locate it")
        problem = None
    except TimeoutException as exception:
        print("Couldn't scrap the element, Unable to locate it")
        problem = None


def to_pdf(problem):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    # set title
    title = problem["title"].encode('latin-1', 'replace').decode('latin-1')
    # set statement
    statement = problem["statement"].encode(
        'latin-1', 'replace').decode('latin-1')
    # set test cases
    test_case = problem["test_case"].encode(
        'latin-1', 'replace').decode('latin-1')
    # set url
    url = problem["url"]
    pdf.cell(200, 10, txt=title, ln=1, align='C')
    pdf.multi_cell(200, 10, txt=statement, align='L')
    pdf.multi_cell(200, 10, txt=test_case, align='L')
    pdf.write(5, 'Problem_Link: ')
    pdf.write(5, url, url)
    title = title.rstrip()
    pdf.output("./LeetCode-Scrapper/"+title+".pdf")


def main():
    category = input(
        "Choose difficulty level from \n Easy \n Medium \n Hard \n\n : ")
    no_of_problems = int(
        input("Enter the number of problems to be scrapped : "))
    info = get_problem(problem_difficulty[category], no_of_problems)
    for name, url in info.items():
        problem = get_description(url, name)
        if (problem is not None):
            to_pdf(problem)
        else:
            pass


if __name__ == '__main__':
    main()

# Close the driver path
driver.close()
