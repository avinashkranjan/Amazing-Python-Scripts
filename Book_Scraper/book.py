# for scraping books
from bs4 import BeautifulSoup as bs
import requests
# to identify emoji unicode characters
import emoji
import pyfiglet
import itertools
import threading
import time
import sys


def is_emoji(text):
    """This function returns True if there is an emoji in the given string else False"""
    return bool(emoji.get_emoji_regexp().search(text))


def link_to_get(link):
    """This function will get the url of the image & book download direct link using the given link for book download"""
    response = requests.get(link)
    th_html = bs(response.text, "html.parser")
    td_all = th_html.find_all("td", id="info")
    td_all = td_all[0]
    td_a = td_all.find_all("a")
    link_href = td_a[1].get("href")
    img_link_td = td_all.find("img", alt="cover")
    img_link_src = img_link_td.get("src")
    img_link = f"http://library.lol{img_link_src}"
    return [link_href, img_link]


def book_get(name, mainres=100, results=5):
    """This function returns the list of books for the given name

        You can give in name : 
                        1. title of book
                        2. isbn of book
                        3. author of book
                        4. publisher of book

        mainres :
                1. 25
                2. 50
                3. 100

        Results:
                    [   0.Book Name, 
                        1.Author, 
                        2.Size, 
                        3.Book Type, 
                        4.Book Link, 
                        5.Book Image Link
                        6.Language]"""
    Books = []
    if is_emoji(name) == True:
        return "Error: emoji"
    if name == "":
        return "Error: enter name"
    name = name.replace(" ", "+")
    # getting request and response
    url = f"http://libgen.is/search.php?req={name}&lg_topic=libgen&open=0&view=simple&res={mainres}&phrase=1&column=def"
    # print(url)
    response = requests.get(url)
    bs_html = bs(response.text, "html.parser")

    if "Search string must contain minimum 3 characters.." in bs_html.body:
        return "Error: Title Too Short"

    # scraping the site for response
    table = bs_html.find_all("table")
    table = table[2]
    table_rows = table.find_all("tr")
    a = len(table_rows)
    table_rows.pop(0)
    # print(url, "\n\n")
    if a > 1:
        counter = 1
        for i in table_rows:
            if counter <= results:
                # make book list
                book_lst = []
                # getting all table datas
                table_datas = i.find_all("td")
                # book name
                book_name = table_datas[2].get_text()
                # author name
                author = table_datas[1].get_text()
                # getting link to book
                link_row = table_datas[9]
                a = link_row.find("a", href=True)
                link = a.get("href")
                # getting image url & direct book download link
                link_all = link_to_get(link)
                # getting language
                language_row = table_datas[6]
                language = language_row.get_text()
                # getting size of book
                size_row = table_datas[7]
                size = size_row.get_text()
                # getting type of book
                type_row = table_datas[8]
                type_ofit = type_row.get_text()
                # this will only take pdfs in English Language
                if (type_ofit != "pdf" and type_ofit != "epub") or language != "English":
                    continue
                book_lst.append(book_name)
                book_lst.append(author)
                book_lst.append(size)
                book_lst.append(type_ofit)
                book_lst.append(link_all[0])
                book_lst.append(link_all[1])
                book_lst.append(language)
                Books.append(book_lst)
                # print(f"\n\n\n{book_lst}\n\n\n")
                counter += 1
        if len(Books) >= 1:
            return Books
        else:
            return "Error: no results found"
    else:
        return "Error: no results found"

# a = book_get("Harry Potter",25,5)
# print(a)
# for i in a :
#     print(f"\n\nName : {i[0]}\nAuthor : {i[1]}\nSize : {i[2]}\nFormat : {i[3]}\nLink : {i[4]}\nImage : {i[5]}\n\n")


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r...Searching Book ' + c)
        sys.stdout.flush()
        time.sleep(0.1)


if __name__ == "__main__":
    print(pyfiglet.figlet_format("Book Scraper"))
    print("---------------------------------------------------------------")
    print("---------------------------------------------------------------")
    while (True):
        print("\nEnter your Choice: \n1 - Search Book\n2 - Exit")
        entry = int(input())
        if (entry == 1):
            print("Enter name of book : ")
            book_name = input()
            # loading
            done = False
            # here is the animation
            t = threading.Thread(target=animate)
            t.start()
            books = book_get(book_name, 25, 5)
            done = True
            try:
                for i in books:
                    print(
                        f"\n\nName : {i[0]}\nAuthor : {i[1]}\nSize : {i[2]}\nFormat : {i[3]}\nLink : {i[4]}\nImage : {i[5]}\n")
            except:
                if (book_get == "Error: no results found"):
                    print("Book not Found/n")
                elif (book_get == "Error: Title Too Short"):
                    print("Title too short/n")
        elif (entry == 2):
            print(pyfiglet.figlet_format("Thank You for Using"))
            print("---------------------------------------------------------------")
            print("---------------------------------------------------------------")
            break
