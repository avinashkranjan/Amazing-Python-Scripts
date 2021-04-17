import os
from selenium import webdriver  # Automated webdriver
from PIL import Image
from fpdf import FPDF  # For converting images to pdf
DRIVER_PATH = ''

def getproblem():
    """
    getproblem() : It takes input from the user of codeforces problemID and difficulty
    level and then by using selenium and chrome webdriver, capturing screenshot of the
    Codeforces problem using ttypography tag because all the problems of codeforces are
    stored inside this div tag and saving it in a image.png file.
    Then saving the image.png as pdf file by using fdf library.
    """

    # Taking input from the user to search for the problem
    Pblm_id = input("Enter the Problem ID: ")
    difficulty = input("Enter the difficulty level: ")
    filename = input('Enter the file name to store Question: ') + '.pdf'

    # Going to the specific URL
    url = "https://codeforces.com/problemset/problem/" + Pblm_id + "/" + difficulty
    path = 'image.png'
    options = webdriver.ChromeOptions()

    # Headless = True for taking a scrolling snapshot
    options.headless = True
    driver = webdriver.Chrome(DRIVER_PATH, options=options)
    driver.get(url)
    # Deciding height by tag
    required_height = driver.execute_script(
        'return document.body.parentNode.scrollHeight')
    driver.set_window_size(1366, required_height)

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
    pdf.output(filename, "F")  # saving the pdf with the specified filename 

    print(f'\nGreat Success!!! Check your directory for {filename} file!')


if __name__ == "__main__":
    DRIVER_PATH = input("Enter DRIVER PATH location: ")
    getproblem()
    os.remove('image.png')
