import pandas as pd
import requests
import urllib.request
from bs4 import BeautifulSoup
import wikipediaapi
    
wiki_lang = wikipediaapi.Wikipedia('en',extract_format=wikipediaapi.ExtractFormat.HTML)
wiki_page = wiki_lang.page('Christiano Ronaldo')
page_html_text = wiki_page.text
soup = BeautifulSoup(page_html_text, "lxml")
def print_sections(sections, level=0):
    for s in sections:
        if 'Club career' in s.title:
            print(s.title)
            #print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:100]))
            for s in s.sections:
                level=level + 1
                print(s.title)
                if(s.sections is None):
                    return
                else:
                    for s in s.sections:
                        level = level+1
                        print(s.title)

        #break
print_sections(wiki_page.sections)
