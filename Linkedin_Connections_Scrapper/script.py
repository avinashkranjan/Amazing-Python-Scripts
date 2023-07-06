# Linkedin My_Connections Scrapper
# Written by XZANATOL
from selenium.webdriver.common.action_chains import ActionChains
from optparse import OptionParser
from selenium import webdriver
import pandas as pd
import time
import sys
import re

pattern_name = "\\n(.+)\\n"  # Used to extract names
pattern_headline = 'occupation\\n(.+)\\n'  # Used to extract headlines

# Help menu
usage = """
<Script> [Options]

[Options]
    -h, --help        Show this help message and exit.
    -e, --email       Enter login email
    -p, --password    Enter login password
    -s, --skills      Flag to scrap each profile, and look at its skill set

Operation Modes:
> Basic mode
    This will scrap all LinkedIn connections list with there corresponding Name, Headline, and Profile link.
> Skills scrapper mode (-s/--skills)
    (Time Consuming mode)
    This will do the same job of basic mode but along with visiting each profile and extracting the skills of each.
"""

# Load args
parser = OptionParser()
parser.add_option("-e", "--email", dest="email", help="Enter login email")
parser.add_option("-p", "--password", dest="password",
                  help="Enter login password")
parser.add_option("-s", "--skills", action="store_true", dest="skills",
                  help="Flag to scrap each profile, and look at its skill set")


def login(email, password):
    """LinkedIn automated login function"""
    # Get LinkedIn login page
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.linkedin.com")
    # Locate Username field and fill it
    session_key = driver.find_element_by_name("session_key")
    session_key.send_keys(email)
    # Locate Password field and fill it
    session_password = driver.find_element_by_name("session_password")
    session_password.send_keys(password)
    # Locate Submit button and click it
    submit = driver.find_element_by_class_name("sign-in-form__submit-button")
    submit.click()
    # Check credentials output
    if driver.title != "LinkedIn":
        print("Provided E-mail/Password is wrong!")
        driver.quit()
        sys.exit()
    # Return session
    return driver


def scrap_basic(driver):
    """Returns 3 lists of Names, Headlines, and Profile Links"""
    driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
    # Bypassing Ajax Call through scrolling the page up and down multiple times
    # Base case is when the height of the scroll bar is constant after 2 complete scrolls
    time_to_wait = 3  # Best interval for a 512KB/Sec download speed - Change it according to your internet speed
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # This loop is for bypassing a small bug upon scrolling that causes the Ajax call to be cancelled
        for i in range(2):
            time.sleep(time_to_wait)
            driver.execute_script("window.scrollTo(0, 0);")  # Scroll up to top
            time.sleep(time_to_wait)
            # Scroll down to bottom
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

        new_height = driver.execute_script(
            "return document.body.scrollHeight")  # Update scroll bar height
        if new_height == last_height:
            break
        last_height = new_height

    # Extract card without links
    extracted_scrap = driver.find_elements_by_class_name(
        "mn-connection-card__details")
    extracted_scrap = [_.text for _ in extracted_scrap]
    # Append data to a seperate list
    names = []
    headlines = []
    for card in extracted_scrap:
        # Try statements just in case of headline/name type errors
        try:
            names.append(re.search(pattern_name, card)[0])
        except:
            names.append(" ")

        try:
            headlines.append(re.search(pattern_headline, card)[0])
        except:
            headlines.append(" ")

    # Extract links
    extracted_scrap = driver.find_elements_by_tag_name('a')
    links = []
    for i in extracted_scrap:
        link = i.get_attribute("href")
        if "https://www.linkedin.com/in" in link and not link in links:
            links.append(link)
    # Return outputs
    return driver, names, headlines, links


def scrap_skills(driver, links):
    skill_set = []
    length = len(links)
    for i in range(length):
        link = links[i]  # Get profile link
        driver.get(link)

        # Bypassing Ajax Call through scrolling through profile multiple sections
        time_to_wait = 3
        last_height = driver.execute_script(
            "return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            # This loop is for bypassing a small bug upon scrolling that causes the Ajax call to be cancelled
            for i in range(2):
                time.sleep(time_to_wait)
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight/4);")
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight/3);")
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight/2);")
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight*3/4);")
                time.sleep(time_to_wait)
                # Scroll down to bottom
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")

            new_height = driver.execute_script(
                "return document.body.scrollHeight")  # Update scroll bar height
            if new_height == last_height:
                break
            last_height = new_height

        # Locate button
        buttons = driver.find_elements_by_tag_name('button')
        length = len(buttons)
        for button_num in range(length):
            i = buttons[button_num].get_attribute("data-control-name")
            if i == "skill_details":
                button = buttons[button_num]
                break
        # Scroll then click the button
        actions = ActionChains(driver)
        actions.move_to_element(button).click().perform()
        # Finally extract the skills
        skills = driver.find_elements_by_xpath(
            "//*[starts-with(@class,'pv-skill-category-entity__name-text')]")
        skill_set_list = []
        for skill in skills:
            skill_set_list.append(skill.text)
        # Append each skill set to its corresponding name
        # Appending all to one string
        skill_set.append(" -- ".join(skill_set_list))
    # Return session & skills
    return driver, skill_set


def save_to_csv(names, headlines, links, skills):
    # If skills argument was false
    if skills is None:
        skills = [None]*len(names)
    # Make a dataframe and append data to it
    df = pd.DataFrame()
    for i in range(len(names)):
        df = df.append({"Name": names[i], "Headline": headlines[i],
                       "Link": links[i], "Skills": skills[i]}, ignore_index=True)
    # Save to CSV
    df.to_csv("scrap.csv", index=False, columns=[
              "Name", "Headline", "Link", "Skills"])


# Start checkpoint
if __name__ == "__main__":
    (options, args) = parser.parse_args()

    # Inputs
    email = options.email
    password = options.password
    skills = options.skills

    driver = login(email, password)  # Login Phase
    print("Successfull Login!")
    print("Commencing 'My-Connections' list scrap...")
    driver, names, headlines, links = scrap_basic(driver)  # Basic Scrap Phase
    print("Finished basic scrap, scrapped {}".format(len(names)))

    if skills:
        print("Commencing 'Skills' scrap...")
        driver, skill_set = scrap_skills(driver, links)  # Skills Scrap Phase
        print("Finished Skills scrap.")
        print("Saving to CSV file...")
        save_to_csv(names, headlines, links, skill_set)  # Save to CSV
    else:
        save_to_csv(names, headlines, links, None)  # Save to CSV

    print("Scrapping session has ended.")
    # End Session
    driver.quit()
