from bs4 import BeautifulSoup
import requests
import csv

pages = int(input('How many pages do you want to scrape ? : '))
dict0 = {
    1: 'Computer Science',
    2: 'Marketing',
    3: 'Finance Internship',
    4: 'Mechanical Internship',
    5: 'HR Internship',
    6: 'Digital Marketing Internship',
    7: 'Electronics Internship',
    8: 'Content Writing Internship',
    9: 'Civil Internship',
}
dict = {
    'Computer Science':
    'https://internshala.com/internships/computer%20science-internship',
    'Marketing': 'https://internshala.com/internships/marketing-internship',
    'Finance Internship':
    'https://internshala.com/internships/finance-internship',
    'Mechanical Internship':
    'https://internshala.com/internships/mechanical-internship',
    'HR Internship': 'https://internshala.com/internships/hr-internship',
    'Digital Marketing Internship':
    'https://internshala.com/internships/digital%20marketing-internship',
    'Electronics Internship':
    'https://internshala.com/internships/electronics-internship',
    'Content Writing Internship':
    'https://internshala.com/internships/content%20writing-internship',
    'Civil Internship': 'https://internshala.com/internships/civil-internship'
}
x = 1
for item in dict.keys():
    print(x, item)
    x += 1
ch = int(input("Enter the categroy. eg 1 for Computer Science : "))
url = dict[dict0[ch]]
print('--------URL : ' + url)
with open('internshala.csv', mode='a') as f:
    writer = csv.writer(f,
                        delimiter=',',
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow([
        'Company', 'Profile', 'Location/s', 'From', 'Upto', 'Duration',
        'Stipend', 'Link'
    ])
    for i in range(1, pages + 1):
        print('Page', i)
        resp = requests.get(url + "/page-" + str(i))
        data = BeautifulSoup(resp.content, 'lxml')
        companies = data.findAll("div", {"class": "heading_6 company_name"})
        profiles = data.findAll("div", {"class": "heading_4_5 profile"})
        locations = data.findAll("div", {"id": "location_names"})
        details = data.findAll("div",
                               {"class": "internship_other_details_container"})
        links = data.findAll("a", {"class": "view_detail_button"})
        for x in range(0, len(companies)):
            company = companies[x].text.strip()
            profile = profiles[x].text.strip()
            location = locations[x].text.strip()
            link = 'www.internshala.com/' + links[x]['href']
            detail = details[x].text
            detail = detail.split('\n')
            extracted = []
            for item in detail:
                item = item.strip()
                if item != '':
                    extracted.append(item)
            info = [company, profile, location]
            info.append(extracted[1].replace('immediatelyImmediately',
                                             'Immediately'))
            info.append(extracted[7])
            info.append(extracted[3])
            info.append(extracted[5])
            info.append(link)
            writer.writerow(info)
input('Done!\nAll the best ;-)')
