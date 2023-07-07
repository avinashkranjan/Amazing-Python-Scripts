import time
from selenium import webdriver
import sqlite3


def sql_connection():
    """
    Establishes a connection to the SQL file database
    :return connection object:
    """
    con = sqlite3.connect('PlaystoreDatabase.db')
    return con


def sql_table(con):
    """
    Creates a table in the database (if it does not exist already)
    to store the app info
    :param con:
    :return:
    """
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS apps(QUERY text, URL text, NAME text, RATING text, "
                " REVIEWS text, INSTALLS text, VERSION text, LASTUPDATE text, "
                " COMPANY text, CONTACT text)")
    con.commit()


def sql_insert_table(con, entities):
    """
    Inserts the desired data into the table to store app info
    :param con:
    :param entities:
    :return:
    """
    cur = con.cursor()
    cur.execute('INSERT INTO apps(QUERY text, URL, NAME, RATING, REVIEWS, '
                'INSTALLS, VERSION, LASTUPDATE, COMPANY, CONTACT) '
                'VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', entities)
    con.commit()


driver = webdriver.Chrome()

con = sql_connection()
sql_table(con)

while 1:
    query = input("\nEnter search query: ")

    driver.get(f'https://play.google.com/store/search?q={query}&c=apps')

    print('\nGetting all the desired info...\n')
    time.sleep(5)

    last_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(5)

    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(5)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    store_urls = []
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        if "details?id" in elem.get_attribute("href"):
            store_urls.append((elem.get_attribute("href")))

    store_urls = list(dict.fromkeys(store_urls))

    for every in store_urls:
        try:
            driver.get(every)
            url = every
            time.sleep(3)

            header1 = driver.find_element_by_tag_name("h1")
            name = header1.text

            star = driver.find_element_by_class_name("BHMmbe")
            rating = star.text

            comments = driver.find_element_by_class_name("EymY4b")
            reviews = comments.text.split()[0]

            stat_info_table = driver.find_elements_by_class_name("htlgb")
            stats = []
            for x in range(len(stat_info_table)):
                if x % 2 == 0:
                    stats.append(stat_info_table[x].text)

            stat_header = driver.find_elements_by_class_name("BgcNfc")
            for x in range(len(stat_header)):
                if stat_header[x].text == "Installs":
                    installs = stats[x]

                if stat_header[x].text == "Current Version":
                    version = stats[x]

                if stat_header[x].text == "Updated":
                    lastupdate = stats[x]

                if stat_header[x].text == "Offered By":
                    company = stats[x]

                if stat_header[x].text == "Developer":
                    for y in stats[x].split("\n"):
                        if "@" in y:
                            contact = y
                            break

                entities = (query, url, name, rating, reviews, installs, version, lastupdate
                            version, lastupdate, company, email)
                sql_insert_table(con, entities)

        except Exception as e:
            continue

    print('\nAll info collected successfully!!\n')

    ans = input('Press (y) to continue or any other key to exit: ').lower()
       if ans == 'y':
            continue
        else:
            print('Exiting..')
            break
