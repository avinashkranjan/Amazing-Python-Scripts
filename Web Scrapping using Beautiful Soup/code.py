import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.codechef.com/problems/TWORANGES?tab=statement'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Print the title of the webpage
print(f"Title: {soup.title.text}\n")

# Find and print all links on the page
print("Links on the page:")
for link in soup.find_all('a'):
    print(link.get('href'))

# Extract text from paragraphs
print("\nText from paragraphs:")
for paragraph in soup.find_all('p'):
    print(paragraph.text)

# Extract image URLs
print("\nImage URLs:")
for img in soup.find_all('img'):
    img_url = img.get('src')
    if img_url:
        print(img_url)

# Count and categorize tags
print("\nTag counts:")
tag_counts = {}
for tag in soup.find_all():
    tag_name = tag.name
    if tag_name:
        tag_counts[tag_name] = tag_counts.get(tag_name, 0) + 1

for tag, count in tag_counts.items():
    print(f"{tag}: {count}")

# Filter and print valid links
print("\nValid links:")
for link in soup.find_all('a'):
    href = link.get('href')
    if href and re.match(r'^https?://', href):
        print(href)

# Save data to a file
with open('webpage_data.txt', 'w') as file:
    file.write(f"Title: {soup.title.text}\n\n")
    file.write("Links on the page:\n")
    for link in soup.find_all('a'):
        file.write(f"{link.get('href')}\n")
    file.write("\nText from paragraphs:\n")
    for paragraph in soup.find_all('p'):
        file.write(f"{paragraph.text}\n")

print("\nData saved to 'webpage_data.txt'")
