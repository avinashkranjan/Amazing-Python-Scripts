import sys
import os
from selenium import webdriver  # Automated webdriver
from PIL import Image  # For manipulating images
from fpdf import FPDF  # For converting images to pdf

# This function takes in the url from which the article has to be downloaded.
# With selenium chrome driver it gets the screenshot of the article tag and
# saves it as a png image. The path of the image is sent to conver_image_to_pdf()


def get_html(url):
    path = "image.png"
    options = webdriver.ChromeOptions()
    # True is required for taking the screenshot with scroll.
    options.headless = True
    driver = webdriver.Chrome(
        r"chromedriver_win32\chromedriver.exe", options=options)
    driver.get(url)  # url is passes
    required_height = driver.execute_script(
        "return document.body.parentNode.scrollHeight"
    )  # gets the scroll height
    # sets the window height and width
    driver.set_window_size(1366, required_height)
    driver.find_element_by_tag_name("article").screenshot(
        path
    )  # Every article in GeeksForGeeks has article tag
    convert_image_to_pdf("image.png")


# This function uses fpdf library to convert the image passed from the last
# function to a pdf. For image manipulation it uses pillow.


def convert_image_to_pdf(path):
    cover = Image.open(path)
    width, height = cover.size
    margin = 20
    # Setting up the dimensions
    pdf = FPDF(unit="pt", format=[width + 2 * margin, height + 2 * margin])
    pdf.add_page()  # Adding new page to the pdf
    pdf.image(path, margin, margin)
    pdf_filename = input("Enter the file name: ") + ".pdf"
    pdf.output(pdf_filename, "F")
    print("Success!!")


if __name__ == "__main__":
    if len(sys.argv) > 1:  # Get the url of the site from where you want to download
        url = " ".join(sys.argv[1:])
    else:
        url = input("Enter the URL: ")
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    get_html(url)
    os.remove("image.png")
