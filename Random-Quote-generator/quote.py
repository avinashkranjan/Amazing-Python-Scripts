import requests


def generate_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']

        return f'{author} - {quote}'

    else:
        return "Failed to fetch a quote"


# Generate and print a random quote
print(generate_quote())
