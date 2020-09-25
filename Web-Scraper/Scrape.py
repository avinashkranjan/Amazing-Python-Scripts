import bs4 as bs
import urllib.request

test = []
for i in range(1,6):
    sauce = urllib.request.urlopen("https://www.geeksforgeeks.org/ibm-placement-paper-quantitative-analysis-set-"+str(i)+"/").read()
    soup = bs.BeautifulSoup(sauce,'lxml')
    var = soup.find_all('ol')[0].find_all('li')
    for x in var:
        try:
            thisQuestion = {'question':"",'options':[],'answer':""}
            st = x.find_all('strong')
            if (len(st)!=0):
                thisQuestion['question'] = x.find_all('strong')[0].getText()
                optionsHtml = x.find_all('li')
                options=[]
            for t in optionsHtml:
                options.append(t.getText())   
            thisQuestion['options'] = options  
            thisQuestion['answer']=x.find('pre').find('b').getText()[2:-2]
            thisQuestion['answer']=options.index(thisQuestion['answer'])
            test.append(thisQuestion)
        except:
            continue

print(len(test))
print(test)