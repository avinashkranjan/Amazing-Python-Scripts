import requests
from bs4 import BeautifulSoup as bs
import sys
import argparse

# Code to add the command line interface
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--movie", required=True, help="Movie Name")
args = vars(parser.parse_args())

#Base IMBD URL to search for movie titles
IMDB_URL = "https://www.imdb.com/search/title/?title="

#Movie the user wants to search for
USER_DEFINED_MOVIE = args['movie']

#To handle connection error
try:
    response = requests.get(IMDB_URL+USER_DEFINED_MOVIE)

except requests.exceptions.ConnectionError as error:
    sys.exit("Check your connection!")

#Creating a soup object
soup = bs(response.content, 'html.parser')

#Function to scrap the details about the movie, set n/a if some detail is missing and store the detail into a dictionary
def scrap_and_store(soup):
    
    #This dictionary stores the movie information
    movie_info = {}
    
    #Try and except blocks to ensure correct data retrival
    try:
        movie = soup.select(".lister-item-content")[0]
    except:
        movie = "N/A"
    
    if movie == "N/A":
        sys.exit("Movie not found in IMDB")

    try:
        movie_info['Name'] = movie.find("a").contents[0]
    except:
        movie_info['Name'] = "N/A"
    try:
        movie_info['Rating'] = movie.select(".value")[0].contents[0]
    except:
        movie_info['Rating'] = "N/A"
    try:
        movie_info['Released'] = movie.find_all("span")[1].contents[0][1:-1]
    except:
        movie_info['Released'] = "N/A"
    try:
        movie_info['Certificate'] = movie.select(".certificate")[0].contents[0]
    except:
        movie_info['Certificate'] = "N/A"
    try:
        movie_info['Runtime'] = movie.select(".runtime")[0].contents[0]
    except:
        movie_info['Runtime'] = "N/A"
    try:
        movie_info['Genre'] = movie.select(".genre")[0].contents[0].strip()
    except :
        movie_info['Genre'] = "N/A"
    try:    
        movie_info['Summary'] = movie.select(".text-muted")[2].contents[0].strip()
    except:
        movie_info['Summary'] = "N/A"
    try:    
        movie_info['Director'] = movie.find_all('p')[2].find_all("a")[0].contents[0]
    except:
        movie_info['Director'] = "N/A"

    try:
        cast_members = movie.find_all('p')[2].find_all("a")[1:]
    except:
        cast_members = []

    cast_name = ""
    for member in cast_members:
        cast_name+=member.contents[0]+", "


    movie_info['Cast'] = cast_name[:-2]
    return movie_info    

#This function fetches the movie information and prints it systematically
def main():

    info = scrape_and_store(soup)
    for key,value in info.items():
        print(f"{key} : {value}")
