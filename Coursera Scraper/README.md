# Coursera Courses Scraper
## Description
A simple scraping module that gets coursera courses by web scraping. The purpose of this is to provide an alternate way to get list of courses from coursera 

### Language
- [X] Python

### Usage
To access the `courses`, this application imports the following modules.
```python
import selenium
```
  
### Instructions to run this application

  1. Fork the repository and open `courses.py`
  2. Initialize the courses class with
```python
c = Courses("<Course_Name>","<No_of_pages>")
```
  3. Use any of the functions to get required data like
```python
c.scrape_all()
```
  4. It will return a dictionary containing the list of courses
  
##### Example Output
The functions will return  -
```
{
    data : [<List of Dictionaries>],
    msg : Course Titles for <Keyword>
}
```
