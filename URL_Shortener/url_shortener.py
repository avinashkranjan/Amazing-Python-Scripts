import pyshorteners

def shorten(url):
    return pyshorteners.Shortener().tinyurl.short(long_url)

if __name__ == "__main__":
    print("URL Shortener: ")

    try:
        long_url = input("Enter a URL: ")
        short_url = shorten(long_url)
        print(f"Your shortened URL is: {short_url}")
    
    except:
        print("Invalid URL. Please enter a valid input.")
