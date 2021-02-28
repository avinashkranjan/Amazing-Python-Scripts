import urllib.request


def check_website_status():
    prompt = "Enter the Website URL:  "
    while True:
        url = str(input(prompt))  # prompt
        if url.startswith('https://'):
            pass
        elif url.startswith('http://'):
            pass
        else:
            url = 'https://' + url
        try:
            headers = {}
            headers['User-Agent'] = (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
            req = urllib.request.Request(url, headers=headers)
            page = urllib.request.urlopen(req)
            code = str(page.getcode())
            print('The website ' + url + ' has returned a ' + code + ' code')
            break
        except Exception as e:
            print(str(e))
            print("Make sure you are entering a valid URL")
            try_again = input("Do you want to try again (y/n): ")
            try_again = try_again.lower()
            if try_again == 'y':
                continue
            else:
                break


check_website_status()
