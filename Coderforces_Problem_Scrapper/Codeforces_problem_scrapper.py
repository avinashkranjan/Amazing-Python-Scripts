import os
from selenium import webdriver  # Automated webdriver
from PIL import Image
from fpdf import FPDF  # For converting images to pdf


def select_difficulty():
    """
    This function will let user to choose the difficulty level
    :return: difficulty_level[]
    """
    difficulty_level = []
    print("\nEnter the Range of difficulty  between 800 to 3500: ")
    difficulty_level.append(int(input("Min: ")))
    difficulty_level.append(int(input("Max: ")))

    return difficulty_level


def extracting_problem_links(diff_level):
    """
    This function saves first saves the link of the pages to scrape from
    and then the link of every question, saves it in list
    :param diff_level: difficulty_level entered by the user
    :return pblms_links: consists of all the available questions to scrape
    """
    no_of_questions = int(input("\nHow many Questions you want to scrape: "))

    pblms_link_scraped = 0
    pblms_links = []
    page = 1
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(DRIVER_PATH, options=options)
    print("\nRequesting URL ...")
    driver.get(f"https://codeforces.com/problemset/?tags={diff_level[0]}-{diff_level[1]}")

    # ===================Getting no. of Pages to Scrape=============================

    # It will give the total no. of pages present with that question from
    # which we are going to scrape
    page_links = []

    print("\nFinding available pages to scrape....")

    available_pages = driver.find_elements_by_css_selector("div.pagination a")
    for page_no in available_pages:
        page_links.append(page_no.get_attribute("href"))

    print(f"Available Pages to scrape are: {len(page_links[:-1])}")

    # ===================================================================================

    # ***************************** SCRAPING PAGE 1 *************************************
    print(f"\nScraping Page {page}")

    elements = driver.find_elements_by_css_selector("td.id.dark.left a" and "td.id.left a")
    for element in elements:
        # Saving the link in pblms_links
        pblms_links.append(element.get_attribute("href"))
        pblms_link_scraped += 1

        # If we scraped required no. of questions then return
        if pblms_link_scraped == no_of_questions:
            print(f"URLs of Question Scraped till now: {pblms_link_scraped}")
            print(f"\nURLs Scrapped Successfully {pblms_link_scraped} out of {no_of_questions}")
            return pblms_links
    page += 1
    print(f"URLs of Question Scraped till now: {pblms_link_scraped}")
    # *************************************************************************************

    # ----------------------------- SCRAPING SUBSEQUENT PAGES -----------------------------
    for link in page_links[1:-1]:
        print(f"\nScraping Page {page}")

        # Going to next Page
        driver.get(link)
        elements = driver.find_elements_by_css_selector("td.id.dark.left a" and "td.id.left a")
        for element in elements:
            # Saving the link in pblms_links
            pblms_links.append(element.get_attribute("href"))
            pblms_link_scraped += 1

            # If we scraped required no. of questions then return
            if pblms_link_scraped == no_of_questions:
                print(f"URLs of Question Scraped till now: {pblms_link_scraped}")
                print(f"\nURLs Scrapped Successfully {pblms_link_scraped} out of {no_of_questions}")
                return pblms_links

        print(f"URLs of Question Scraped till now: {pblms_link_scraped}")
        page += 1
    # ----------------------------------------------------------------------------------------------

    # scraped all the available questions but still the count is less
    print(f"\n{pblms_link_scraped} out of {no_of_questions} URLs able to scrapped !!!")
    return pblms_links


def getproblem(URLs):
    """
    getproblem() : It takes input from the user of codeforces problemID and difficulty
    level and then by using selenium and chrome webdriver, capturing screenshot of the
    Codeforces problem using ttypography tag because all the problems of codeforces are
    stored inside this div tag and saving it in a image.png file.
    Then saving the image.png as pdf file by using fdf library.
    """

    path = 'image.png'

    # Creating a Target Output Folder
    target_folder = './Coderforces_Problem_Scrapper/problems_pdf'
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    options = webdriver.ChromeOptions()
    # Headless = True for taking a scrolling snapshot
    options.headless = True
    driver = webdriver.Chrome(DRIVER_PATH, options=options)
    file_counter = 1

    for url in URLs:
        driver.get(url)
        # Deciding height by tag
        required_height = driver.execute_script(
            'return document.body.parentNode.scrollHeight')
        driver.set_window_size(1366, required_height)

        title = driver.find_element_by_class_name("title").text
        filename = title[3:] + '.pdf'

        # Taking SS of everything within the ttypography class
        driver.find_element_by_class_name('ttypography').screenshot(path)

        # Opening image with pillow so based to capture its height and width
        cover = Image.open(path)
        WIDTH, HEIGHT = cover.size
        MARGIN = 10
        # based on image's height and width we are adjusting the pdf margin and borders
        pdf = FPDF(unit='pt', format=[WIDTH + 2 * MARGIN, HEIGHT + 2 * MARGIN])
        pdf.add_page()  # Adding new page to the pdf
        pdf.image(path, MARGIN, MARGIN)

        pdf.output(os.path.join(target_folder, filename), "F")  # saving the pdf with the specified filename
        print(f'File saved in your directory ./problems_pdf/{filename}   ({file_counter}/{len(URLs)}) !')
        file_counter += 1


if __name__ == "__main__":
    DRIVER_PATH = input("Enter DRIVER PATH location: ")
    diff = select_difficulty()   # Accepting difficulty level from user
    problems_link = extracting_problem_links(diff)  # scraping the required the no. of links
    getproblem(problems_link)  # saving the Questions in PDF file.
    os.remove('image.png')
