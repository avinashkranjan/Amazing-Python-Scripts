import requests
import json
from responses import PageSpeedResponse


class PageSpeed(object):
    """
    Google PageSpeed analysis client

    Attributes:
        api_key (str): Optional API key for client account.
        endpoint (str): Endpoint for HTTP request
    """

    def __init__(self, api_key=None):
        self.api_key = api_key
        self.endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'

    def analyse(self, url, strategy='desktop', category='performance'):
        """
        Run PageSpeed test

        Args:
            url (str): The URL to fetch and analyse.
            strategy (str, optional): The analysis strategy to use. Acceptable values: 'desktop', 'mobile'
            category (str, optional): A Lighthouse category to run; if none are given, only Performance category will be run

        Returns:
            response: PageSpeed API results
        """
        strategy = strategy.lower()

        params = {
            'strategy': strategy,
            'url': url,
            'category': category,
        }

        if self.api_key:
            params['key'] = self.api_key

        # Sanity Check
        if strategy not in ('mobile', 'desktop'):
            raise ValueError('invalid strategy: {0}'.format(strategy))

        # Returns raw data
        raw = requests.get(self.endpoint, params=params)

        response = PageSpeedResponse(raw)

        return response

    def save(self, response, path='./'):
        json_data = response._json
        with open(path + "json_data.json", 'w+') as f:
            json.dump(json_data, f, indent=2)


if __name__ == "__main__":
    ps = PageSpeed()
    response = ps.analyse('https://www.example.com', strategy='mobile')
    ls = [
        response.url, response.loadingExperience,
        response.originLoadingExperience,
        response.originLoadingExperienceDetailed,
        response.loadingExperienceDetailed, response.finalUrl,
        response.requestedUrl, response.version, response.userAgent
    ]  # , response.lighthouseResults]
    ps.save(response)
    print(ls)
