from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


class geeksforgeeks:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 100)
    # using seleinum to access html content
    url = f"https://practice.geeksforgeeks.org/courses?utm_source=geeksforgeeks&utm_medium=main_header&utm_campaign=courses"
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    def get_popular_now(self):
        """
        Fetches popular now courses and related information from gfg portal

        :return: datatype : dictionary containing:
            -> Name : Name of courses
            -> Rating : Rating of courses
            -> Interested : Number of people interested
            -> Price : Price of given course
        """
        try:
            popular_now = geeksforgeeks.soup.find(
                "div",
                {
                    "class": "ui cards courseListingPage_cardLayout__multW courseListingPage_toggleCourseCards__pWBVA"
                },
            )
            name = []
            rating = []
            interested = []
            price = []

            for items in popular_now.find_all(
                "a", {"class": "ui card courseListingPage_courseCardContainer__lLZiS"}
            ):
                course_name = items.find(
                    "h4",
                    {
                        "class": "ui left aligned header courseListingPage_myAuto__i6GdI sofia-pro course_heading"
                    },
                )
                name.append(course_name.text)
                rating_geek = items.find("span", {"class": "urw-din"})
                if not rating_geek:
                    rating_geek = "Information not available"
                else:
                    rating_geek = rating_geek.text
                rating.append(rating_geek)
                interseted_geeks = items.find(
                    "div",
                    {
                        "class": "courseListingPage_descriptionText__zN_K1 sofia-pro g-opacity-50 g-mb-0 grid_with__meta"
                    },
                )
                interested.append(interseted_geeks.text.split(" ")[0])
                course_price = items.find(
                    "p", {"class": "sofia-pro g-mb-0 courseListingPage_batchFee__0NlbJ"}
                )
                price.append(course_price.text)

            course_popular_now = dict(
                {
                    "Name": name,
                    "Rating": rating,
                    "Interested": interested,
                    "Price": price,
                }
            )
            return {
                "data": course_popular_now,
                "message": "Popular Courses are now fetched",
            }
        except (WebDriverException, NoSuchElementException) as e:
            raise Exception(
                f"An error occurred while scraping popular courses: {str(e)}")

    def get_self_paced(self):
        """
        Fetches self-paced courses and related information from gfg portal

        :return: datatype : dictionary containing:
            -> Name : Name of courses
            -> Rating : Rating of courses
            -> Interested : Number of people interested
            -> Price : Price of given course
        """
        try:
            self_paced = geeksforgeeks.soup.find(
                "div",
                {
                    "class": "ui cards courseListingPage_cardLayout__multW courseListingPage_courseCardsGrid__VYBzZ"
                },
            )
            name = []
            rating = []
            interested = []
            price = []
            for items in self_paced.find_all(
                "a", {"class": "ui card courseListingPage_courseCardContainer__lLZiS"}
            ):
                course_name = items.find(
                    "h4",
                    {
                        "class": "ui left aligned header courseListingPage_myAuto__i6GdI sofia-pro course_heading"
                    },
                )
                name.append(course_name.text)
                course_rating = items.find("div", {"class": "courseListingPage_courseCardContentsGrid__jk3VM"}).find(
                    "span", {"class": "urw-din"})
                if not course_rating:
                    course_rating = "Information not available"
                else:
                    course_rating = course_rating.text
                rating.append(course_rating)
                course_interseted = items.find(
                    "div",
                    {
                        "class": "courseListingPage_descriptionText__zN_K1 sofia-pro g-opacity-50 g-mb-0 grid_with__meta"
                    },
                )
                interested.append(course_interseted.text.split(" ")[0])
                course_price = items.find(
                    "p", {"class": "sofia-pro g-mb-0 courseListingPage_batchFee__0NlbJ"}
                )
                price.append(course_price.text)

            course_self_paced = dict(
                {
                    "Name": name,
                    "Rating": rating,
                    "Interested": interested,
                    "Price": price,
                }
            )
            return {
                "data": course_self_paced,
                "message": "Self paced Courses are now fetched",
            }
        except (WebDriverException, NoSuchElementException) as e:
            raise Exception(
                f"An error occurred while scraping popular courses: {str(e)}")

    def get_live_course(self):
        """
        Fetches self-paced courses and related information from gfg portal

        :return: datatype : dictionary containing:
            -> Name : Name of courses
            -> Rating : Rating of courses
            -> Interested : Number of people interested
            -> Price : Price of given course
        """
        try:
            live = geeksforgeeks.soup.find(
                "div", {"class": "g-mt-8"}
            ).next_sibling.next_sibling.next_sibling
            name = []
            rating = []
            interested = []
            price = []
            for item in live.find_all(
                "a", {"class": "ui card courseListingPage_courseCardContainer__lLZiS"}
            ):
                course_name = item.find(
                    "h4",
                    {
                        "class": "ui left aligned header courseListingPage_myAuto__i6GdI sofia-pro course_heading"
                    },
                )
                name.append(course_name.text)
                course_rating = item.find("div", {"class": "meta"})
                if not course_rating:
                    course_rating = "Information not available"
                else:
                    course_rating = course_rating.text
                rating.append(course_rating)
                course_interseted = item.find(
                    "div",
                    {
                        "class": "courseListingPage_descriptionText__zN_K1 sofia-pro g-opacity-50 g-mb-0 grid_with__meta"
                    },
                )
                interested.append(course_interseted.text.split(" ")[0])
                course_price = item.find(
                    "p", {"class": "sofia-pro g-mb-0 courseListingPage_batchFee__0NlbJ"}
                )
                if not course_price:
                    course_price = "0"
                else:
                    course_price = course_price.text
                price.append(course_price)

            course_live = dict(
                {
                    "Name": name,
                    "Rating": rating,
                    "Interested": interested,
                    "Price": price,
                }
            )
            return {
                "data": course_live,
                "message": "Live Courses are now fetched",
            }
        except (WebDriverException, NoSuchElementException) as e:
            raise Exception(
                f"An error occurred while scraping popular courses: {str(e)}")
