import re
import requests
url = input("Enter Url: ")
text = requests.get(url).text
x = re.findall(r"[a-zA-Z]+@{1}[a-zA-Z]+[.]{1}[a-zA-Z]+", text)
val=""
for i in x:
    val+=i+"\n"
filename= input("Enter the file Name you want: ")
with open(f"{filename}.txt","w") as file:
    file.write(val)
    print("Your File has been Saved")
    print("Email(s) found:\n")
    print(val)
