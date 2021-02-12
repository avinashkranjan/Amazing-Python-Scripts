import pyshorteners

url = input("Enter URL: ")

print ("URL after Shortening : ", pyshorteners.Shortener().tinyurl.short(url))
