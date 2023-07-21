import os
import time
import urllib
import requests
from urllib.parse import quote
import array as arr


class simple_image_download:
    def __init__(self):
        pass

    def urls(self, keywords, limit):
        keyword_to_search = [str(item).strip() for item in keywords.split(',')]
        i = 0
        links = []
        while i < len(keyword_to_search):
            url = 'https://www.google.com/search?q=' + quote(
                keyword_to_search[i].encode(
                    'utf-8')) + '&biw=1536&bih=674&tbm=isch&sxsrf=ACYBGNSXXpS6YmAKUiLKKBs6xWb4uUY5gA:1581168823770&source=lnms&sa=X&ved=0ahUKEwioj8jwiMLnAhW9AhAIHbXTBMMQ_AUI3QUoAQ'
            raw_html = self._download_page(url)

            end_object = -1

            j = 0
            while j < limit:
                while (True):
                    try:
                        new_line = raw_html.find('"https://', end_object + 1)
                        end_object = raw_html.find('"', new_line + 1)

                        buffor = raw_html.find('\\', new_line + 1, end_object)
                        if buffor != -1:
                            object_raw = (raw_html[new_line + 1:buffor])
                        else:
                            object_raw = (raw_html[new_line + 1:end_object])

                        if '.jpg' in object_raw or 'png' in object_raw or '.ico' in object_raw or '.gif' in object_raw or '.jpeg' in object_raw:
                            break

                    except Exception as e:
                        print(e)
                        break

                links.append(object_raw)
                j += 1

            i += 1
        return (links)

    def download(self, keywords, limit):
        keyword_to_search = [str(item).strip() for item in keywords.split(',')]
        main_directory = "simple_images/"
        i = 0

        while i < len(keyword_to_search):
            self._create_directories(main_directory, keyword_to_search[i])
            url = 'https://www.google.com/search?q=' + quote(
                keyword_to_search[i].encode('utf-8')) + '&biw=1536&bih=674&tbm=isch&sxsrf=ACYBGNSXXpS6YmAKUiLKKBs6xWb4uUY5gA:1581168823770&source=lnms&sa=X&ved=0ahUKEwioj8jwiMLnAhW9AhAIHbXTBMMQ_AUI3QUoAQ'
            raw_html = self._download_page(url)

            end_object = -1

            j = 0
            while j < limit:
                while (True):
                    try:
                        new_line = raw_html.find('"https://', end_object + 1)
                        end_object = raw_html.find('"', new_line + 1)

                        buffor = raw_html.find('\\', new_line + 1, end_object)
                        if buffor != -1:
                            object_raw = (raw_html[new_line+1:buffor])
                        else:
                            object_raw = (raw_html[new_line+1:end_object])

                        if '.jpg' in object_raw or 'png' in object_raw or '.ico' in object_raw or '.gif' in object_raw or '.jpeg' in object_raw:
                            break

                    except Exception as e:
                        print(e)
                        break

                path = main_directory + keyword_to_search[i]

                # print(object_raw)

                if not os.path.exists(path):
                    os.makedirs(path)

                filename = str(
                    keyword_to_search[i]) + "_" + str(j + 1) + ".jpg"

                try:
                    r = requests.get(object_raw, allow_redirects=True)
                    open(os.path.join(path, filename), 'wb').write(r.content)
                except Exception as e:
                    print(e)
                    j -= 1
                j += 1

            i += 1

    def _create_directories(self, main_directory, name):
        try:
            if not os.path.exists(main_directory):
                os.makedirs(main_directory)
                time.sleep(0.2)
                path = (name)
                sub_directory = os.path.join(main_directory, path)
                if not os.path.exists(sub_directory):
                    os.makedirs(sub_directory)
            else:
                path = (name)
                sub_directory = os.path.join(main_directory, path)
                if not os.path.exists(sub_directory):
                    os.makedirs(sub_directory)

        except OSError as e:
            if e.errno != 17:
                raise
            pass
        return

    def _download_page(self, url):

        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData

        except Exception as e:
            print(e)
            exit(0)
