
import ipaddress
import json
import requests
from docopt import docopt


def cloudflare_lookup(type, record):
    url = f"https://1.1.1.1/dns-query?name={record}&type={type}"
    headers = {'accept': 'application/dns-json'}
    response = requests.get(url, headers=headers)
    j_data = json.loads(response.text)
    return j_data.get('Answer', j_data.get('Question'))


valid_types = {'A', 'MX', 'PTR', 'SRV', 'TXT', 'NS'}

if __name__ == '__main__':
    arguments = docopt(__doc__, version='doh-dig 0.1')
    if arguments['type']:
        t = arguments['<type>'].upper()
        r = arguments['<record>'].lower()
        if t not in valid_types:
            exit('Invalid type')
        x = cloudflare_lookup(t, r)
        print(json.dumps(x))
    elif arguments['ptr']:
        ip = arguments['<ip>']
        arpa = ipaddress.ip_address(ip).reverse_pointer
        x = cloudflare_lookup('PTR', arpa)
        print(json.dumps(x))
    else:
        print(arguments)
