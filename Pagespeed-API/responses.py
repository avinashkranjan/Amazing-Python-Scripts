import json


class Response(object):
    """ 
    Base Response Object

    Attributes:
        self.json (dict): JSON representation of response
        self._request (str): URL of
        self._response (`requests.models.Response` object): Response object from requests module
    """

    def __init__(self, response):
        response.raise_for_status()

        self._response = response
        self._request = response.url
        self._json = json.loads(response.content)


class PageSpeedResponse(Response):
    """ 
    PageSpeed Response Object

    Attributes:
        self.url (str):
        self.speed (int):
        self.statistics (`Statistics` object):
    """
    @property
    def url(self):
        return self._json['id']

    @property
    def loadingExperience(self):
        return self._json['loadingExperience']['overall_category']

    @property
    def originLoadingExperience(self):
        return self._json['originLoadingExperience']['overall_category']

    @property
    def originLoadingExperienceDetailed(self):
        metrics = self._json['originLoadingExperience']['metrics']
        keys_ = list(metrics.keys())

        originLoadingExperienceDetailed_ = {}

        for each in keys_:
            originLoadingExperienceDetailed_[each] = metrics[each]['category']

        return originLoadingExperienceDetailed_

    @property
    def loadingExperienceDetailed(self):
        metrics = self._json['loadingExperience']['metrics']
        keys_ = list(metrics.keys())

        loadingExperienceDetailed_ = {}

        for each in keys_:
            loadingExperienceDetailed_[each] = metrics[each]['category']

        return loadingExperienceDetailed_

    # In case of re-directs
    @property
    def requestedUrl(self):
        return self._json['lighthouseResult']['requestedUrl']

    @property
    def finalUrl(self):
        return self._json['lighthouseResult']['finalUrl']

    @property
    def version(self):
        return self._json['lighthouseResult']['lighthouseVersion']

    @property
    def userAgent(self):
        return self._json['lighthouseResult']['userAgent']

    @property
    def lighthouseResults(self):
        return self._json['lighthouseResult']
