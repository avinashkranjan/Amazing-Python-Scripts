import re
import time
import random
from bs4 import BeautifulSoup
import requests


class LyricsDotComScraper:

    stype = {"exact": 2, "title": 1}
    gender = ["m", "f", "g"]
    qtype = {"albums": 3, "artists": 2}
    decade = list(range(1930, 2020, 10))
    albums = "#content-body > div:nth-child(1) >\
div:nth-child(4) > p:nth-child(3) > button:nth-child(1)"
    base_url = "https://www.lyrics.com/"

    def __init__(self, **kwargs):
        self.params_bs4objs = []
        self.count = kwargs.get("count")
        self.listener = kwargs.get("listener")
        self.lyrics = []
        self.artists = []
        self.albums = []

    @staticmethod
    def parse_params(**kwargs):
        """
        Allowed parameters are
        'stype': This is specifies the type of match
            for the search it takes values 2 for exact match
            and 1 for Exact match within title. It defaults
            to within lyrics if not specified.
        'gender': Can either be 'm' for male, 'f' for female or
            'g' for group. Defaults to all. it can also take a
            list or tuple of genders for multiple matches
        'qtype': Can be 3 to only show albums that match the search
            or 2 to show artists that match the search it can also
            take a list or tuple of both as values for multiple matches
        'genre': Can be any of the items in the genres class variable.
            it can also take a list or tuple of multiple genres as values
            for multiple matches
        'decade':Takes any (or a tuple(list) of multiple values) of the
            values specified in the decade class variable
        "year": It can be a year of a tuple or list of years between 1900 and
             whatever year this is.
        "style": It can be a value of a tuple or list of values in the style
            class variable.
        """

        lens = []
        for i in kwargs.values():
            if isinstance(i, (list, tuple)):
                lens.append(len(i))
            else:
                lens.append(1)
        noofparams = 1
        for i in lens:
            if i:
                noofparams *= i

        params = [
            {} for i in range(noofparams)
        ]  # List of parameter dictionaries for multiple searches
        for i in kwargs:
            if len(kwargs[i]) > 0:
                if isinstance(kwargs[i], (tuple, list)):
                    each = int(noofparams / len(kwargs[i]))
                    k = 0
                    for j in kwargs[i]:
                        if j:
                            for m in range(k, k + each):
                                params[m][i] = j
                            k += each
                else:
                    for x in range(noofparams):
                        params[x][i] = kwargs[i]
        return params

    def search(self, params, search_path="serp.php"):
        url = self.base_url + search_path
        for i in params:
            print(f"Sending request to {url} with parameters {i}")
            req = requests.get(url, params=i)
            html = req.text
            req_obj = BeautifulSoup(html, "lxml")
            results = req_obj.select(".category-header > hgroup:nth-child(2)")
            try:
                lyrics, artists, albums, search_term = results[0].find_all("strong")
                message = f"Search Results: {lyrics.text} lyrics, \
                    {artists.text} artists, {albums.text} albums for search term {search_term.text}"
                print(message)
            except IndexError:
                print(f"There are no search results for request {req.url}")

            self.params_bs4objs.append([i, req_obj])
            time.sleep(2)
        self.extract()

    def extract(self):
        self.lyrics.extend(self.parse_lyrics())
        self.albums.extend(self.extract_albums())
        self.albums.extend(self.extract_artists())

    @staticmethod
    def extract_full_lyrics(
        full_lyric_url, title, download=False, filename="[[auto_generate]]"
    ):
        """ """
        req = requests.get(full_lyric_url)
        content = req.text
        lyric = LyricsDotComScraper.extract_lyrics_remove_tags(content)
        if download and filename == "[[auto_generate]]":
            filename = (
                title.replace(" ", "_")
                + "-"
                + str(random.randrange(10000000, 99999999))
                + "-lyrics.txt"
            )
            with open(filename, "w") as f:
                f.write(lyric)

        lyric = LyricsDotComScraper.extract_lyrics_remove_tags(content)
        return [lyric, filename] if download == "download" else lyric

    @staticmethod
    def extract_lyrics_remove_tags(content):
        remove_tags_regex = re.compile(
            r"(<.*>)(?=(\w+<))"
        )  # Regex with findall splits tag elements into_opening, content, closing_tag
        lyricsobj = BeautifulSoup(content, "lxml")
        try:
            lyricsbody = lyricsobj.select("#lyric-body-text")[0].text
            with open("gg.html", "w") as f:
                f.write(lyricsbody)
        except IndexError:
            return ""
        for opening, text, closing in remove_tags_regex.findall(lyricsbody):
            # Planning on doing something with the definitions?
            del(text)
            lyricsbody.replace(opening, "")
            lyricsbody.replace(closing, "")
        return lyricsbody

    @staticmethod
    def extract_fulllyrics_url_with_snippet(obj, selector=".lyric-body"):
        """
        extract lyrics snippet and url from beautifulsoup object.
        """
        extract = obj.select(selector)
        onclick = extract[0].get("onclick")
        start = onclick.find("href='") + 6
        end = onclick.find("';")
        url = onclick[start:end]
        lyric_snippet = extract[0].text.replace("<em>", "").replace("</em>", "")
        return url, lyric_snippet

    def extract_data(self, obj, selector):
        extract = obj.select(selector)
        if not extract:
            return "", ""
        text = list(extract[0].children)[0].text
        url = list(extract[0].children)[0].get("href")
        if not url.startswith("https://"):
            url = self.base_url.rstrip("/") + url

        return text, url

    @staticmethod
    def extract_thumbnail(obj, selector=".album-thumb"):
        extract = obj.select(selector)
        if not extract:
            return "", ""
        img_url = list(extract[0].children)[0].get("src")
        img_title = list(extract[0].children)[0].get("title").replace(" ", "_").lower()
        return img_title, img_url

    def parse_lyrics(self):
        lyrics = []
        count = 0
        for j in self.params_bs4objs:
            if j[0].get("qtype") == 1:
                lyrics_select = j[1].select(".sec-lyric")
                for i in lyrics_select:
                    if count == self.count:
                        return lyrics
                    item = {}
                    title, lyric_url = self.extract_data(i, ".lyric-meta-title")
                    artist, artist_link = self.extract_data(
                        i, ".lyric-meta-album-artist"
                    )
                    year, year_link = self.extract_data(i, ".lyric-meta-album-year")
                    album, album_url = self.extract_data(i, ".lyric-meta-album")
                    (
                        url,
                        snippet,
                    ) = LyricsDotComScraper.extract_fulllyrics_url_with_snippet(i)
                    item["title"] = title
                    item["lyric_url"] = lyric_url
                    item["artist"] = artist
                    item["artist_link"] = artist_link
                    item["year"] = year
                    item["year_link"] = year_link
                    item["full_lyrics_url"] = url
                    item["snippet"] = snippet
                    item["album"] = album
                    item["album_url"] = album_url
                    lyrics.append(item)
                    count += 1
        return lyrics

    def extract_albums(self):
        albums = []
        count = 0
        for j in self.params_bs4objs:
            if j[0].get("qtype") == 3:
                bsobj = j[1]
                album_tables = bsobj.select(".tdata td")
                for i in album_tables:
                    if count == self.count:
                        return albums
                    album = {}
                    j = i.select("a")
                    album["album_title"] = j[0].get("title")
                    album["album_url"] = self.base_url + j[0].get("href")
                    if "artist" in j[-1].get("href"):
                        album["album_artist"] = j[-1].text
                        album["album_artist_url"] = self.base_url + j[-1].get("href")
                    else:
                        album["album_artist_url"] = album["album_artist"] = "N/A"
                    albums.append(album)
                    count += 1
        return albums

    def extract_artists(self):
        artists = []
        count = 0
        for j in self.params_bs4objs:
            if j[0].get("qtype") == 2:
                bsobj = j[1]
                artist_tables = bsobj.select(".tdata td")
                for i in artist_tables:
                    if count == self.count:
                        return artists
                    artist = {}
                    j = i.select("a")[0]
                    artist["artist_name"] = j.get("title")
                    artist["artist_link"] = self.base_url + j.get("href")
                    artists.append(artist)
                    count += 1
        return artists

    def extract_album_content(self, html):
        bsobj = BeautifulSoup(html, "lxml")
        content_data = bsobj.select("#content-main .tdata tr")
        album_content = []
        for i in content_data:
            album_entry = {}
            j = i.select("a")[0]
            album_entry["song_name"] = j.text
            album_entry["song_url"] = self.base_url + j.get("href")
            album_entry["song_duration"] = list(i.children)[-2].text
            album_content.append(album_entry)

        return album_content