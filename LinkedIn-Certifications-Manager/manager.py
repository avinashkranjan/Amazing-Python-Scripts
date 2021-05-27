import getpass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

# Xpaths
xLinkedin = {
    'xEmail': '//input[@name="session_key"]',
    'xPass': '//input[@name="session_password"]',
    'xLogin': '//button[contains(.,"Sign in")]',
    'xProfile': '//div[@data-control-name="identity_welcome_message"]',
    'xCertName': '//input[@placeholder="Ex: Microsoft certified network associate security"]',
    'xCertOrg': '//input[@placeholder="Ex: Microsoft"]',
    'xCredId': '//input[@id="single-line-text-form-component-profileEditFormElement-CERTIFICATION-profileCertification-ACoAADI-i-oBZzsiExXBGep7oC4p5cgLkd4v7kE-1-licenseNumber"]',
    'xCredUrl': '//input[@id="single-line-text-form-component-profileEditFormElement-CERTIFICATION-profileCertification-ACoAADI-i-oBZzsiExXBGep7oC4p5cgLkd4v7kE-1-url"]',
    'xSave': '//button[contains(.,"Save")]'
}


class LinkedIn:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        emailField = driver.find_element_by_xpath(xLinkedin['xEmail'])
        emailField.send_keys(self.email)
        passwordField = driver.find_element_by_xpath(xLinkedin['xPass'])
        passwordField.send_keys(self.password)

        submitBtn = driver.find_element_by_xpath(xLinkedin['xLogin'])
        submitBtn.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, xLinkedin['xProfile']))).click()

    def addCertData(self, name, org, credId, credUrl):
        sleep(5)
        currentUrl = driver.current_url
        driver.get(currentUrl+'edit/forms/certification/new/')
        nameInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, xLinkedin['xCertName'])))
        nameInput.send_keys(name)
        sleep(1)
        orgInput = driver.find_element_by_xpath(xLinkedin['xCertOrg'])
        orgInput.send_keys(org)
        sleep(3)
        orgInput.send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        credIdInput = driver.find_element_by_xpath(xLinkedin['xCredId'])
        credIdInput.send_keys(credId)
        credUrlInput = driver.find_element_by_xpath(xLinkedin['xCredUrl'])
        credUrlInput.send_keys(credUrl)
        driver.find_element_by_xpath(xLinkedin['xSave']).click()


if __name__ == "__main__":
    # Get LinkedIn credentials
    email = input('Enter your linkedin email: ')
    password = getpass.getpass('Password: ')

    # Chrome environment setup
    opt = webdriver.ChromeOptions()
    opt.add_argument('--disable-gpu')
    opt.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    driver.get('https://linkedin.com')

    linkedIn = LinkedIn(email, password)
    linkedIn.login()

    # Add certifications to linkedin
    while True:
        name = input('Enter course name[nothing to cancel]: ')
        if name == '':
            break
        courseUrl = input(f'Enter course url for the course[\'{name}\']: ')
        org = input('Enter the name of the issuing organistion: ')
        courseId = courseUrl.split('/')[-1]
        linkedIn.addCertData(name=name, org=org,
                             credId=courseId, credUrl=courseUrl)
        print(f'Added: {name}')
        name = ''
    print('Completed!')
    driver.close()
