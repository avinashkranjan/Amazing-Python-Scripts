The users can run the script 
Usage: python script.py [URL] "[CSS selector]" [Interval in minutes]

Example : python script.py https://www.timeanddate.com/worldclock/ "body > div.main-content-div > section.bg--grey.pdflexi-t--small > div > div:nth-child(2) > div.my-city__clocks > div > div:nth-child(3) > span > span" 1  

If there is a change in content it will be displayed in the command line.