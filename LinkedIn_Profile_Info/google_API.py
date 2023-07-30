import re
import requests
import logging
import time

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
                if resp.status_code == 200:
                    data = resp.json()
                    items = data.get("items", [])
                    results.extend(items)

                    next_page = data.get("queries", {}).get("nextPage", [])
                    if not next_page:
                        break
                    params["start"] = next_page[0]["startIndex"]
                elif resp.status_code == 429:  # API rate limiting
                    retry_after = int(resp.headers.get("Retry-After", 5))
                    logger.warning(
                        f"Google Custom Search API rate limit reached. Retrying in {retry_after} seconds.")
                    time.sleep(retry_after)
                else:
                    resp.raise_for_status()  # Raise an exception for other HTTP status codes
        except requests.exceptions.RequestException as e:
            logger.exception(f"Error in _hit_api: {e}")
        except Exception as e:
            logger.exception(
                "An error occurred while processing the API response.")
        return results
