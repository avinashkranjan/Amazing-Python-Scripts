import requests
from bs4 import BeautifulSoup

def get_github_traffic(repo_url):
    response = requests.get(repo_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the element containing the traffic data
    traffic_element = soup.find('a', {'data-tab-item': 'i4traffic-tab'})

    if traffic_element:
        # Extract the traffic data
        traffic_data = traffic_element.find('span', {'class': 'Counter'}).text.strip()
        return traffic_data
    else:
        return "Traffic data not found."

if _name_ == "_main_":
    repo_url = 'https://github.com/username/repository'
    traffic_data = get_github_traffic(repo_url)
    print(f"Traffic data: {traffic_data}")