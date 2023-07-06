import json
import pyautogui
import re
import pyfiglet
import getpass
import platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from clint.textui import colored, puts, indent
from time import sleep
from os import system


class ZoomZoom:

    user = getpass.getuser()
    data_path = 'data/meetings.json'
    screen_width, screen_height = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    chrome_options = Options()
    chrome_options.add_argument(
        f'--window-size={screen_width},{screen_height}')
    # finding the user's operating system because the process differs depending.
    operating_system = platform.system()
    if operating_system == 'Linux' or operating_system == 'Mac':
        clear = 'clear'
    elif operating_system == 'Windows':
        clear = 'cls'
    else:
        clear = 'clear'

    # this function loads in the meeting data from a the json file in the data directory
    def load_meeting_data(self):
        with open(self.data_path, 'r') as stored_data:
            meeting_data = json.load(stored_data)
        return meeting_data

    # this function (which is much too large) is retrieving the url and password form the user
    # the url and password are then sent to the automatic_join function for use.
    def meeting_link(self, data):
        while True:
            title = pyfiglet.figlet_format('Zoom Zoom !', font='slant')
            with indent(4):
                puts(colored.cyan(title))
            print()
            with indent(4, quote=' $'):
                puts(colored.green(f'Welcome to ZoomZoom {self.user}!'))
            print()
            with indent(4, quote=' *'):
                puts(
                    colored.yellow(
                        'WARNING: make you disable any window tiling before running this script or else it will not work.'
                    ))
                puts(
                    colored.yellow(
                        'WARNING: also make sure you download and add a compatible webdriver for your browser and put it in the "webdriver" directory.'
                    ))
            print()
            with indent(4):
                puts(colored.cyan('=== List of saved zoom meetings ==='))
            print()
            meeting_url_list = {
                str(count): meeting_name
                for count, meeting_name in enumerate(data['meetings'], 1)
            }
            if len(meeting_url_list) == 0:
                with indent(4, quote=' *'):
                    puts(
                        colored.red(
                            'there are currently no saved zoom meetings...'))
            else:
                for key, value in meeting_url_list.items():
                    with indent(4, quote=' >'):
                        puts(colored.blue(f'{key}: {value}'))
            print()
            print()
            meeting_url = input(
                'Enter zoom meeting meeting id/url or choose the number of a saved meeting id: '
            )
            if meeting_url in meeting_url_list:
                system(self.clear)
                saved_meeting_url = data["meetings"][
                    meeting_url_list[meeting_url]]["id"]
                saved_meeting_psw = data["meetings"][
                    meeting_url_list[meeting_url]]["psw"]
                return (saved_meeting_url, saved_meeting_psw, True)
            print()
            verify = input('Are you sure about the entered link/id? [y/n]: ')
            if verify != 'y':
                system(self.clear)
            else:
                break
        print()
        password = input('Does this meeting require a password? [y/n]: ')
        if password == 'y':
            pass_check = ""
            while password != pass_check:
                print()
                password = getpass.getpass('Enter meeting password: ')
                pass_check = getpass.getpass('Enter password again: ')
                if password != pass_check:
                    print()
                    with indent(4, quote=' *'):
                        puts(colored.red('PASSWORDS DID NOT MATCH!'))
                    print()
        else:
            password = 0
        return (meeting_url, password, False)

    def save_meeting(self, meeting_info, data):
        if not meeting_info[2]:
            meeting_url = meeting_info[0]
            meeting_psw = meeting_info[1]
            meeting_data = data
            print()
            save_meeting = input(
                'Would you like to save this meeting for future use? [y/n]: ')
            if save_meeting == 'y':
                print()
                meeting_name = input('Enter name for saved meeting: ')
                meeting_data["meetings"].update(
                    {meeting_name: {
                        "id": 0,
                        "psw": 0
                    }})
                meeting_data["meetings"][meeting_name]["id"] = meeting_url
                meeting_data["meetings"][meeting_name]["psw"] = meeting_psw
                with open(self.data_path, 'w') as stored_data:
                    json.dump(meeting_data, stored_data)
                print()
                with indent(4, quote=' $'):
                    puts(
                        colored.green(
                            f'{meeting_name} has been saved at {self.data_path}!'
                        ))
                sleep(1)
                system(self.clear)

    # This is the main function for joining the zoom session.
    # This function takes either a meeting id or url and its password
    # Then uses selenium and pyautogui to enter the information into the browser
    # And then enter the information into the zoom app on your desktop.
    def automatic_join(self, meeting_info):
        meeting_id = meeting_info[0]
        if meeting_id[:5] == 'https':
            meeting_id = re.search(r"\b/\d+", meeting_info[0]).group()[1:]
        meeting_psw = meeting_info[1]
        browser = webdriver.Chrome(options=self.chrome_options,
                                   executable_path='webdriver/chromedriver')
        browser.get('https://zoom.us/')
        join_meeting = browser.find_element_by_xpath(
            '//*[@id="btnJoinMeeting"]')
        join_meeting.click()
        sleep(1)
        for char in meeting_id:
            pyautogui.press(char)
        join_button = browser.find_element_by_xpath('//*[@id="btnSubmit"]')
        join_button.click()
        sleep(1)
        # For linux users.
        # This clicks the open window in the browser to open the zoom app on your computer.
        if self.operating_system == 'Linux':
            pyautogui.click(0.552 * self.screen_width,
                            0.152 * self.screen_height)
        else:
            pyautogui.click(0.552 * self.screen_width,
                            0.152 * self.screen_height + 75)
        # clicks join without video button when no password is needed.
        sleep(1)
        pyautogui.click(0.597 * self.screen_width, 0.625 * self.screen_height)
        # closes the zoom window to expose the password window
        sleep(1)
        if self.operating_system == 'Linux':
            pyautogui.press('escape')
        # Enters the password into the zoom password box only if a password is needed.
        if meeting_psw != 0:
            sleep(1)
            for char in meeting_psw:
                pyautogui.press(char)
        # clicks to submit entered password on the screen
        sleep(1)
        pyautogui.click(self.screen_width / 2, self.screen_height * 0.594)
        # clicks to join without video if a password is needed
        sleep(1)
        pyautogui.click(0.588 * self.screen_width, 0.628 * self.screen_height)


if __name__ == '__main__':
    zoom_zoom = ZoomZoom()
    clear = zoom_zoom.clear
    system(clear)
    meeting_data = zoom_zoom.load_meeting_data()
    meeting_info = zoom_zoom.meeting_link(meeting_data)
    zoom_zoom.save_meeting(meeting_info, meeting_data)
    zoom_zoom.automatic_join(meeting_info)
