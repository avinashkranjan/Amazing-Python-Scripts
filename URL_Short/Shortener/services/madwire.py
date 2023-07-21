# encoding: utf-8
"""
Madwire Shortener Implementation
"""
import json

from pyshorteners.base import BaseShortener
from pyshorteners.exceptions import ShorteningErrorException


class Madwire(BaseShortener):
    api_url = "https://m360.us/add"

    def __init__(self, **kwargs):
        super(Madwire, self).__init__(**kwargs)

    def short(self, url):
        params = {
            'link': url
        }

        response = self._post(self.api_url, data=params)

        if response.ok:
            return 'https://' + response.text

        raise ShorteningErrorException('There was an error shortening this '
                                       'url - {0}'.format(response.content))

    def expand(self, url):
        pass

    def total_clicks(self, url):
        pass
