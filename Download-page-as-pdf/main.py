#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
import pyppdf
import re
from pyppeteer.errors import PageError, TimeoutError, NetworkError


def main():
    parser = argparse.ArgumentParser(description='Page Downloader as PDF')
    parser.add_argument('--link', '-l', action='store', dest='link',
                        required=True, help='Inform the link to download.')
    parser.add_argument('--name', '-n', action='store', dest='name',
                        required=False, help='Inform the name to save.')

    arguments = parser.parse_args()

    url = arguments.link

    if not arguments.name:
        name = re.sub(r'^\w+://', '', url.lower())
        name = name.replace('/', '-')
    else:
        name = arguments.name

    if not name.endswith('.pdf'):
        name = name + '.pdf'

    print(f'Name of the file: {name}')

    try:
        pyppdf.save_pdf(name, url)
    except PageError:
        print('URL could not be resolved.')
    except TimeoutError:
        print('Timeout.')
    except NetworkError:
        print('No access to the network.')


if __name__ == '__main__':
    main()
