import urllib3
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen

class AppURLopener(urllib.request.FancyURLopener):
    version = "Chrome"

def getLinks():
	f = open('links','r')
	lst = []
	count = 0
	for line in f:
		if not '&hearts' in line:
			string = ''
			start = False
			name = ''
			# removing name
			ind = 0
			for x in line:
				if x == ']':
					ind +=1
					break
				ind += 1
			line = line[ind:]
			for i in line:
				if i == ')':
					break
				elif i == '(':
					start = True
					continue
				if start == True:
					string +=i
			lst.append(string)
		else:
			count +=1
	print("Premium = ",count)
	return lst

if __name__ == '__main__':
	links = getLinks()
	print( len(links) )
	for l in links:
		print( l )
	print('\n')
	total = len(links)
	ind = 296
	links = links[296:]
	files = {}
	files['Easy'] = open('easy','a')
	files['Medium'] = open('medium','a')
	files['Hard'] = open('hard','a')
	files['not found'] = open('not found','a')

	count = {}
	count['Easy'] = 1
	count['Medium'] = 1
	count['Hard'] = 1
	count['not found'] = 1

	for link in links:
		print("ind = ",ind," left = ",total-ind," Scrapping ",link)
		print("Opening")
		opener = AppURLopener()
		link = opener.open(link)
		page=BeautifulSoup(link)
		print("Opened")
		#finding difficulty of problem
		allli = page.find_all('li')
		diff = 'not found'
		for li in allli:
			if "Medium" in str(li):
				diff = 'Medium'
				break;
			elif "Hard" in  str(li):
				diff = 'Hard'
				break
			elif "Easy" in str(li):
				diff = 'Easy'
				break
		print(page.title)
		name = page.title.string
		print('problem name: ',name)
		allmeta = page.find_all('meta')
		for meta in allmeta:
			if meta.get('name') == 'description':
				ques = meta.get('content')
				ques = ques.encode('utf-8')
				files[diff].write(str(count[diff]) + ') ' + name + '\n')
				files[diff].write(ques.decode("utf-8"))
				count[diff] += 1
				break
		ind +=1

	print("done: ",ind)		