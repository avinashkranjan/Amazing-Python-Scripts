import re
import requests
url = input("Enter Url: ")
text = requests.get(url).text
x = re.findall(r"[a-zA-Z]+@{1}[a-zA-Z]+[.]{1}[a-zA-Z]+", text)   #This is a regex query which search for the particular email format.
for i in x: 
    val+=i+"\n"                                                  #this adds all the email data found in val variable  
filename= input("Enter the file Name you want: ")                #You can use any file name you want for your output file
with open(f"{filename}.txt","w") as file:
    file.write(val)
    print("Your File has been Saved")
    print("Email(s) found:\n")
    print(val)
