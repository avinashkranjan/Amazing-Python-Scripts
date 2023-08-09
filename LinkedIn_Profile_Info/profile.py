import re
import requests
from urllib.parse import urlparse, unquote
import logging

logger = logging.getLogger(__name__)


class GoogleSearchAPI:
    def __init__(self, key: str, cx: str):
        self._cx = cx
        self._key = key
        self._api_url = "https://www.googleapis.com/customsearch/v1"
        self._params = {
            "num": 10,
            "cx": self._cx,
            "key": self._key
        }

    def _hit_api(self, linkedin_id: str) -> list:
        results = []
        try:
            params = self._params.copy()
            params["exactTerms"] = f"/in/{linkedin_id}"
            while True:
                resp = requests.get(self._api_url, params=params)
                if resp.status_code != 200:
                    logger.warning(
                        f"Google Custom Search API error: {resp.status_code} - {resp.text}")
                    break

                data = resp.json()
                items = data.get("items", [])
                results.extend(items)

                next_page = data.get("queries", {}).get("nextPage", [])
                if not next_page:
                    break
                params["start"] = next_page[0]["startIndex"]
        except Exception as e:
            logger.exception("Error in _hit_api:")
        return results


class ProfilePicture:
    def __init__(self, key: str, cx: str):
        self._api_obj = GoogleSearchAPI(key, cx)

    def extract_id(self, link: str) -> str:
        """ To get a clean LinkedIn ID  """
        linkedin_id = link
        match = re.findall(r'\/in\/([^\/]+)\/?', urlparse(link).path)
        if match:
            linkedin_id = match[0].strip()
        linkedin_id = linkedin_id.strip("/")
        linkedin_id = unquote(linkedin_id)
        return linkedin_id

    def _check_picture_url(self, link: str) -> bool:
        match = re.search(
            r"(media-exp\d\.licdn\.com).+?(profile-displayphoto-shrink_)", link)
        return bool(match)

    def _check_url_exists(self, link: str) -> bool:
        try:
            resp = requests.head(link, timeout=5)
            return resp.status_code == 200
        except requests.RequestException:
            return False

    def _extract_profile_picture(self, linkedin_id: str, res: list) -> str:
        link = ""
        for item in res:
            linkedin_url = item.get("link", "")
            search_id = self.extract_id(linkedin_url)
            if search_id == linkedin_id:
                metatags = item.get("pagemap", {}).get("metatags", [])
                metatags = [tag.get("og:image")
                            for tag in metatags if "og:image" in tag]

                for url in metatags:
                    if self._check_picture_url(url) and self._check_url_exists(url):
                        link = url
                        break
            if link:
                break
        return link

    def _extract_profile_info(self, linkedin_id: str, res: list) -> dict:
        info = {}
        for item in res:
            linkedin_url = item.get("link", "")
            search_id = self.extract_id(linkedin_url)
            if search_id == linkedin_id:
                info["name"] = item.get("title")
                info["headline"] = item.get("snippet")
                info["public_url"] = linkedin_url
                break
        return info

    def get_profile_picture(self, link: str) -> str:
        linkedin_id = self.extract_id(link)
        api_resp = self._api_obj._hit_api(linkedin_id)
        profile_picture_url = self._extract_profile_picture(
            linkedin_id, api_resp)
        return profile_picture_url

    def get_profile_info(self, link: str) -> dict:
        linkedin_id = self.extract_id(link)
        api_resp = self._api_obj._hit_api(linkedin_id)
        profile_info = self._extract_profile_info(linkedin_id, api_resp)
        return profile_info
