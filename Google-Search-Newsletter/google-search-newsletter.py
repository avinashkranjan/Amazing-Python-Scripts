from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as Options_firefox
from selenium.webdriver.chrome.options import Options as Options_chrome
from email.mime.text import MIMEText
from configparser import ConfigParser
import smtplib

newsletter_file = 'newsletter.txt'
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)


def scrape_news():

    # get user settings
    driver = config.get('your_settings', 'driver')
    search_topic = config.get('your_settings', 'search_topic')

    # set up driver
    PATH_TO_DRIVER = "./%s" % driver

    if driver == 'geckodriver':
        firefox_options = Options_firefox()

        # run in headless mode
        firefox_options.headless = True

        # disable cookies to prevent popups
        firefox_pref = webdriver.FirefoxProfile()
        firefox_pref.set_preference("network.cookie.cookieBehavior", 2)

        browser = webdriver.Firefox(executable_path=PATH_TO_DRIVER,
                                    options=firefox_options,
                                    firefox_profile=firefox_pref)

    elif driver == 'chromedriver':
        chrome_options = Options_chrome()

        # run in headless mode
        chrome_options.add_argument('--headless')

        # disable cookies to prevent popups
        chrome_options.add_experimental_option(
            'prefs', {'profile.default_content_setting_values.cookies': 2})

        browser = webdriver.Chrome(executable_path=PATH_TO_DRIVER,
                                   options=chrome_options)

    else:
        print('ERROR: driver not supported')

    print('Getting search results...')

    # open URL
    browser.get('https://google.com')

    # select google search bar
    google_search = browser.find_element_by_name('q')

    # type news topic to search
    google_search.send_keys(search_topic)
    google_search.send_keys(Keys.ENTER)

    browser.implicitly_wait(5)

    browser.find_element_by_css_selector('a[data-sc="N"]').click()

    browser.implicitly_wait(5)

    # get all elements containing news title
    all_headings = browser.find_elements_by_xpath(
        '//div[contains(@role, "heading") and contains(@aria-level, "2")]')

    # get all elements containing links for each news title
    all_links = browser.find_elements_by_xpath('//g-card/div/div/div[2]/a')

    # open file for writing
    file = open(newsletter_file, 'w')

    # loop over each title and link, print each to the file
    for heading, link in zip(all_headings, all_links):
        file.write('\n\n')
        file.write(heading.text)
        file.write('\n')
        file.write(link.get_attribute('href'))

    browser.close()
    print('Done. Search results exported to "newsletter.txt"')

    pass


def send_email():

    print('Sending email...')

    # get user settings
    email_subject = config.get('your_settings', 'email_subject')
    email_smtp = config.get('your_settings', 'email_smtp')
    sender_email_address = config.get('your_settings', 'sender_email_address')
    email_password = config.get('your_settings', 'email_password')
    receiver_email_address = config.get('your_settings',
                                        'receiver_email_address')

    # newsletter file will be sent by email
    with open(newsletter_file, 'r') as file:
        file_content = file.read()

    # configure mail
    message = MIMEText(file_content)
    message['Subject'] = email_subject
    message['From'] = sender_email_address
    message['To'] = receiver_email_address

    # set smtp server
    server = smtplib.SMTP(email_smtp, '587')
    server.ehlo()
    server.starttls()

    # send email
    server.login(sender_email_address, email_password)
    server.send_message(message)
    server.quit()

    print("Email sent!")

    pass


if __name__ == "__main__":
    scrape_news()
    send_email()
    pass
