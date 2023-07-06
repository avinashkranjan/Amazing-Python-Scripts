from bs4 import BeautifulSoup
import requests as req

currencies = []

page = req.get('https://www.x-rates.com/').text

soup = BeautifulSoup(page, 'html.parser')

options = soup.find_all('option')[:-11]

for option in options:
    currency_short = option.text[:(option.text.find(" "))]
    currency_name = option.text[(option.text.find(" ") + 3):]
    current_element = {'name': currency_name, 'short': currency_short}
    currencies.append(current_element)
    print('{}. {} ({})'.format(len(currencies), current_element['name'],
                               current_element['short']))

currency_index = int(input('Enter your currency\'s position number: ')) - 1
currency = currencies[currency_index]
amount = input(
    '\033cEnter amount of {}s (if amount isn\'t integer, then write it with a dot, not comma): '
    .format(currency['name'].lower()))

currencies_table_url = 'https://www.x-rates.com/table/?from={}&amount={}'.format(
    currency['short'], amount)

currencies_table_page = req.get(currencies_table_url).text

soup = BeautifulSoup(currencies_table_page, 'html.parser')

table_rows = soup.findChild('table', attrs={
    'class': 'tablesorter'
}).findChildren('tr')[1:]

print('\033cFor {} {}s you\'ll get:'.format(amount, currency['name'].lower()))

for table_row in table_rows:
    row_data = table_row.findChildren('td')
    exchange_rate = {
        'currency': row_data[0].text,
        'amount': float(row_data[1].text)
    }
    print('{:.3f} {}s'.format(exchange_rate['amount'],
                              exchange_rate['currency']))
