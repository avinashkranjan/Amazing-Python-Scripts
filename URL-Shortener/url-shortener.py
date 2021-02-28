import pyshorteners


def shorten_url(url):
    return pyshorteners.Shortener().tinyurl.short(url)


url = input("Enter URL: ")
print("URL after Shortening : ", shorten_url(url))
