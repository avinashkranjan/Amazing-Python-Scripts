from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from fpdf import FPDF


capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

driver = webdriver.Chrome(desired_capabilities=capa,options=options)
baseurl="https://www.codechef.com/problems"
wait = WebDriverWait(driver, 20)

# map to get url from its problem difficulty
problem_difficulty = {"Beginner": "school", "Easy": "easy", "Medium": "medium", "Hard": "hard", "Challenge": "challenge"}

# get_problems returns the name and links of the problems
def get_problems(category, no_of_problems):

# A map to store problem name and problem url
    problem_info = {}
    driver.get(baseurl + '/' + category)
    # wait till the  first element is loaded
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='primary-content']/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/a/b")))
    
    for problem_index in range(1, no_of_problems + 1):
        problem_name = driver.find_element_by_xpath("//*[@id='primary-content']/div/div[2]/div/div[2]/table/tbody/tr[{}]/td[1]/div/a/b".format(problem_index)).text
        problem_url = driver.find_element_by_xpath("//*[@id='primary-content']/div/div[2]/div/div[2]/table/tbody/tr[{}]/td[1]/div/a".format(problem_index)).get_attribute('href')
        print(problem_name," ",problem_url)
        problem_info[problem_name] = problem_url
    return problem_info
    
# get_problem_desciption returns content of the problem
def get_problem_description(problem_url,problem_name):
    try:
        driver.get(problem_url)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='problem-statement']/p[1]")))
        problem_title= problem_name
        problem_statement = driver.find_element_by_xpath("//*[@id='problem-statement']/p[1]").text
        problem_test_cases = driver.find_element_by_xpath("//*[@id='problem-statement']/pre[1]").text

    
        if (problem_test_cases.find("Output") == -1):
            problem_test_cases = "Input\n" + problem_test_cases
            problem_test_cases+="\nOutput\n"
            problem_test_cases +=  driver.find_element_by_xpath("//*[@id='problem-statement']/pre[2]").text
            
        
        else:
            
            
            driver.execute_script("window.stop();")
        problem={'title':problem_title,'statement':problem_statement,'test_case':problem_test_cases}
        return problem
    
    #Handling exceptions
    except NoSuchElementException as e:
        print("Couldn't scrap the element, Unable to locate it",e)
        problem=None




#storing the information in the pdf
def convert_to_pdf(problem):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt = problem["title"], ln = 1, align = 'C')
    pdf.multi_cell(200, 10, txt =problem["statement"], align = 'L')
    pdf.multi_cell(200, 10, txt =problem["test_case"], align = 'L')
    pdf.output(problem["title"]+".pdf")   
    
    
#main function
def main():
    category=input("Enter the difficulty level from the following \n Beginner \n Easy \n Medium \n Hard \n Challenge  \n\n")
    no_of_problems=int(input("\n Enter the number of problems to be scrapped: \n"))
    info = get_problems(problem_difficulty[category],no_of_problems)
    for name, url in info.items():
        problem=get_problem_description(url,name)
        if(problem is not None ):
            convert_to_pdf(problem)
        else:
            pass
            
if __name__ == '__main__':
    main()

driver.close()