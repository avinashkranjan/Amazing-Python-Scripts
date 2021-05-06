import re
import requests

url = input("Enter Url: ")
text = requests.get(url).text

# Regex query which search for the particular email format.
x = re.findall(r"[a-zA-Z]+@{1}[a-zA-Z]+[.]{1}[a-zA-Z]+", text)

val = ""
for i in x:
    val += i+"\n"  # this adds all the email data found in val variable

if val == "":
    print("No emails found in the website")
else:
    filename = input("Enter the file Name you want (without extension):")
    with open(f"{filename}.txt", "w") as file:
        file.write(val)
        print("Your File has been Saved")
        print("Email(s) found:\n")
        print(val)
