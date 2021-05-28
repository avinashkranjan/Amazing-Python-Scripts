# importing the required libraries
from datetime import datetime as dt

# Change the list to the websites you wish to block
websites = [ "www.youtube.com", "twitter.com","www.skype.com/en", "www.facebook.com","www.instagram.com"]
# Change the path to your hosts files folder
host = "C:\Windows\System32\drivers\etc\hosts"
# change the path to where you want to redirect 
redirect = "127.0.0.1:8080"

# Change the date when you want to start and end
start = dt(2021, 4, 25)
end = dt(2021, 4, 24)

while True:
    # When we wish to add the list of sites to be blocked
    if start <= dt(dt.now().year, dt.now().month, dt.now().day) < end:
        with open(host, "r+") as file:
            temp = file.read()
            for site in websites:
                if site in temp:
                    pass
                else:
                    # write command adds the sites to be blocked in the host file
                    file.write(redirect + " " + site + "\n")
        print("The site has been blocked.")
        break
    # When we wish to remove the list of sites to be blocked
    else:
        with open(host, "r+") as file:
            temp = file.readlines()
            file.seek(0)
            for line in temp:
                if not any(site in line for site in websites):
                    file.write(line)
            # truncate command deletes the sites to be blocked from host file
            file.truncate()
        print("The site has been unblocked.")
        break
