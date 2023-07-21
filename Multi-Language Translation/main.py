import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

headers = {
    "content-type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "application/gzip",
    "X-RapidAPI-Key": "ENTER RAPID API KEY HERE",
    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

# function to send a request


def multi_translate(languages: list, phrase: str):
    print(phrase)
    res = {}
    for i in languages:
        payload = {
            "q": phrase,
            "target": i
        }

        response = requests.post(url, data=payload, headers=headers)

        res[i] = response.json()['data']['translations'][0]['translatedText']
    return res


print(multi_translate(["ru", "fr"], "hi"))
