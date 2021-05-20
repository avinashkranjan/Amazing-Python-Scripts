import subprocess
import requests
import webbrowser

# executing a script and extracting the errors
p = subprocess.run(['python', 'filename.py'], capture_output=True, text=True)
s= p.stderr
s=s.split("\n")
s=s[-2]
errorType= errorMessage= ""
k=len(s)
for i in range(k):
    if s[i]==":":
        break
errorType=s[:i]
errorMessage=s[i+1:]

# using Stack Exchange API search feature
# parsing the json and extracting the links
URL="https://api.stackexchange.com/2.2/search"
PARAMS= {'intitle': errorType, 'tagged': 'python', 'nottagged':errorMessage, 'sort': 'votes', 'site': 'stackoverflow'}
r= requests.get(url= URL, params= PARAMS)
data= r.json()

links=[]
for i in data['items']:
    # get those question links which are answered
    if i["is_answered"]==True:
        links.append(i["link"])

# opening links the web browser
n1=len(links)
for i in range(7):
    if i<n1:
        webbrowser.open_new_tab(links[i])
