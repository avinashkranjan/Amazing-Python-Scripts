from selenium import webdriver
from time import sleep
from configparser import ConfigParser
from datetime import datetime
import csv

config = ConfigParser()
config.read('config.ini')
username = config.get('AUTH', 'USERNAME')
password = config.get('AUTH', 'PASSWORD')

classTime = ["09:20","11:40","14:25"]

class ClassAutomation():
    def __init__(self):
        self.count = 0
        self.findCount()
        #Runs endlessly and calls initClass method when it's class time
        while True:
            if datetime.now().strftime("%H:%M") in classTime:
                print(datetime.now().strftime("%H:%M"))
                self.initClass()
            sleep(30)
    
    #Initiates Class
    def initClass(self):
        className = self.findClass()
        if className is None:
            return
        print("Initiating...")
        self.login()
        self.driver.find_element_by_xpath("//div[text()='{}']".format(className)).click()
        sleep(10)
        link=self.driver.find_element_by_partial_link_text("https://meet.google.com/lookup/").text
        self.driver.get(link)
        sleep(10)
        self.driver.find_element_by_xpath("//span[text()='Join now']").click()
        sleep(60*60)
        print("Quitting...")
        sleep(5)
        self.driver.quit()
        if self.count < 2:
            self.count = self.count + 1
        else:
            self.count = 0
        self.findCount()

    #Returns the ClassName for the current time
    def findClass(self):
        with open("schedule.csv","r") as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                if row["Day"]==datetime.now().strftime("%a"):
                    return row[classTime[self.count]]
            return None
    #Determines the current time position in the classTime list
    def findCount(self):
        if self.findClass() is None:
            print("No Class Today")
            return
        currentTime=datetime.now().strftime("%H:%M")
        currentHour = int(currentTime.split(":")[0])
        currentMin = int(currentTime.split(":")[1])
        for i in classTime:
            if currentHour==int(i.split(":")[0]) and currentMin<int(i.split(":")[1]):
                self.count = classTime.index(i)
                print("Next Class at",classTime[self.count],"Today")
                break
            elif currentHour<int(i.split(":")[0]):
                self.count = classTime.index(i)
                print("Next Class at",classTime[self.count],"Today")
                break
            else:
                if classTime.index(i)==2:
                    self.count=0
                    print("Next Class at",classTime[self.count],"Tomorrow")
                    break
                continue

    #Logs into the google classroom with the account credentials
    def login(self):    
        profile = webdriver.FirefoxProfile('/path/to/the/created/profile')
        self.driver = webdriver.Firefox(profile)
        self.driver.get("https://accounts.google.com/")
        sleep(2)
        try:
            self.driver.find_element_by_name("identifier").send_keys(username)
            sleep(1)
        except:
            self.driver.find_element_by_name("Email").send_keys(username)
            sleep(1)
        try: 
            self.driver.find_element_by_id("identifierNext").click()
            sleep(4)
        except:
            self.driver.find_element_by_id("next").click()
            sleep(4)
        try:
            self.driver.find_element_by_name("password").send_keys(password)
            sleep(1)
        except:
            self.driver.find_element_by_name("Passwd").send_keys(password)
            sleep(1)
        try:    
            self.driver.find_element_by_id("passwordNext").click()
            sleep(4)
        except:
            self.driver.find_element_by_id("trustDevice").click()
            self.driver.find_element_by_id("submit").click()
            sleep(4)
        self.driver.get("https://classroom.google.com/")
        sleep(6)
        
ClassAutomation()