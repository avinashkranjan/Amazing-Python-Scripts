import pandas as pd
import requests
import urllib.request
from bs4 import BeautifulSoup
import wikipediaapi


class myScraper:

    # Initializing the Constructor
    def __init__(self, player):

        self.wiki_lang = wikipediaapi.Wikipedia(
            'en', extract_format=wikipediaapi.ExtractFormat.HTML)
        self.wiki_page = self.wiki_lang.page(player)
        self.page_html_text = self.wiki_page.text
        self.soup = BeautifulSoup(self.page_html_text, "lxml")
        self.player = player

    def get_club_details(self, sections, level=0):
        for s in sections:
            if 'Club career' in s.title:
                print(s.title)
            for s in s.sections:
                level = level + 1
                print(s.title)
                if (s.sections is None):
                    return
                else:
                    for s in s.sections:
                        level = level + 1
                        print(s.title)

    def execute(self):
        self.get_club_details(self.wiki_page.sections, level=0)


# def print_sections(sections, level=0):
#     for s in sections:
#         if 'Club career' in s.title:
#             print(s.title)
#             #print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:100]))
#             for s in s.sections:
#                 level=level + 1
#                 print(s.title)
#                 if(s.sections is None):
#                     return
#                 else:
#                     for s in s.sections:
#                         level = level+1
#                         print(s.title)

# break
# print_sections(wiki_page.sections)


def main():
    player = input("Please Enter the player Info")
    my_scraper_obj = myScraper(player)
    my_scraper_obj.execute()


if __name__ == '__main__':
    main()
