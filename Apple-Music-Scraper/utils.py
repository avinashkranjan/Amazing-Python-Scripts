import urllib.parse
import requests
import json
from bs4 import BeautifulSoup


def get_cover(url, width, height, img_format="jpg", crop_option=""):
    """
    Generate a full Apple Music artwork URL\
    with proper width, height, format, and crop settings.

    Parameters
    ----------
    url : str
        The original Apple Music artwork template URL
        containing `{w}`, `{h}`, `{f}`, `{c}`.
    width : int or str
        Target width of the image.
    height : int or str
        Target height of the image.
    img_format : str, optional
        Image format (jpg, png, etc.). Defaults to "jpg".
    crop_option : str, optional
        Cropping mode used by Apple Music artwork URLs. Defaults to empty string.

    Returns
    -------
    str
        Fully formatted artwork URL.

    Notes
    -----
    Apple Music uses dynamic artwork URLs where dimensions and format are embedded
    in the URL as placeholders such as `{w}`, `{h}`, `{f}`, and `{c}`.
    """
    if not isinstance(url, str):
        return url

    try:
        new_url = (
            url.replace("{w}", str(width))
               .replace("{h}", str(height))
               .replace("{c}", crop_option)
               .replace("{f}", img_format)
        )
        return new_url
    except (TypeError, AttributeError):
        return url


def convert_album_to_song_url(album_url):
    """
    Convert an Apple Music album-track URL into a direct Apple Music song URL.

    Parameters
    ----------
    album_url : str
        Full Apple Music album URL that
        contains a track ID via the query parameter `?i=...`.

    Returns
    -------
    str or None
        Direct Apple Music song URL if `i` parameter exists.
        Otherwise, returns `None`.

    Examples
    --------
    Input:
        https://music.apple.com/us/album/song-name/12345?i=67890

    Output:
        https://music.apple.com/us/song/song-name/67890

    Notes
    -----
    Apple Music album pages embed individual song IDs through the query parameter `i`,
    which must be extracted and placed into a `/song/` URL.
    """
    try:
        parsed = urllib.parse.urlparse(album_url)
        query_params = urllib.parse.parse_qs(parsed.query)
        song_id = query_params.get("i", [None])[0]

        if not song_id:
            return None

        parts = parsed.path.split("/")
        if len(parts) < 4:
            return None

        country = parts[1]
        title = parts[3]

        return f"https://music.apple.com/{country}/song/{title}/{song_id}"

    except (IndexError, KeyError, TypeError, AttributeError, ValueError):
        return None


def get_all_singles(url="https://music.apple.com/us/artist/king-princess/1349968534"):
    """
    Fetch all singles & EP URLs from an Apple Music artist page.

    Parameters
    ----------
    url : str, optional
        Base artist page URL. Defaults to the sample King Princess artist link.

    Returns
    -------
    list[str]
        A list of Apple Music URLs for all singles & EPs for the artist.

    Notes
    -----
    - Apple Music loads singles under the `/see-all?section=singles` endpoint.
    - This function retrieves the serialized server data, parses the `items` section,
      and extracts the correct song/EP URLs.
    - Used internally by `artist_scrape()`.
    """
    result = []

    full_url = f"{url}/see-all?section=singles"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(full_url, headers=headers, timeout=10)
        res.raise_for_status()
    except requests.RequestException:
        return result

    soup = BeautifulSoup(res.text, "html.parser")
    script_tag = soup.find("script", {"id": "serialized-server-data"})
    if not script_tag:
        return result

    try:
        data = json.loads(script_tag.text)
        sections = data[0]["data"]["sections"]
        if not sections:
            return result

        items = sections[0].get("items", [])
    except (json.JSONDecodeError, KeyError, IndexError, TypeError):
        return result

    for item in items:
        try:
            action_url = (
                item["segue"]["actionMetrics"]
                ["data"][0]["fields"]["actionUrl"]
            )
            result.append(action_url)
        except (KeyError, IndexError, TypeError):
            continue

    return result


def safe_action_url(item):
    """
    Safely extract an Apple Music "actionUrl" from a section item.

    This function attempts to extract a playable or navigational URL from
    Apple Music's internal JSON structure. It first looks for URLs provided
    via `segue -> actionMetrics`, which is the most common structure. If that
    fails, it falls back to the `contentDescriptor` URL when available.

    Parameters
    ----------
    item : dict
        A dictionary representing an Apple Music content item inside a section.

    Returns
    -------
    str or None
        The extracted URL if available, otherwise None.

    Notes
    -----
    This helper prevents repetitive try/except blocks throughout all scraper
    functions and gracefully handles missing keys, unexpected formats, or
    incomplete items.
    """
    try:
        # segue-based URLs (most items)
        return item["segue"]["actionMetrics"]["data"][0]["fields"]["actionUrl"]
    except Exception:
        pass

    try:
        # fallback: plain contentDescriptor
        return item["contentDescriptor"]["url"]
    except Exception:
        return None


def find_section(sections, key):
    """
    Locate a specific Apple Music section by matching a substring in its ID.

    This utility searches through the list of sections extracted from
    Apple Music's `serialized-server-data` and returns the first section
    whose "id" field contains the provided key substring.

    Parameters
    ----------
    sections : list[dict]
        List of section dictionaries parsed from Apple Music page data.
    key : str
        Substring to search for inside the section ID.

    Returns
    -------
    dict or None
        The matching section dictionary if found, otherwise None.

    Notes
    -----
    Apple Music uses structured section IDs such as:
        - "artist-detail-header-section"
        - "track-list"
        - "music-videos"
        - "similar-artists"
    This function simplifies section lookup and reduces repeated loops and
    conditional chains in scraper functions.
    """
    for sec in sections:
        if key in sec.get("id", ""):
            return sec
    return None


def append_urls_from_section(section, target_list):
    """
    Extract URLs from a section and append them to a target list.

    This helper iterates through all items inside a given Apple Music
    section, uses `safe_action_url()` to safely extract their URLs,
    and appends each valid URL to the provided list.

    Parameters
    ----------
    section : dict or None
        The section dictionary containing an "items" list. If None, the
        function does nothing.
    target_list : list
        The list to which valid extracted URLs will be appended.

    Returns
    -------
    None
        This function modifies target_list in-place.

    Notes
    -----
    Many Apple Music sections such as:
        - top songs
        - albums
        - playlists
        - videos
        - similar artists
    share the same internal structure. This helper removes code duplication
    and ensures unified URL extraction behavior.
    """
    if not section:
        return
    for it in section.get("items", []):
        url = safe_action_url(it)
        if url:
            target_list.append(url)


def fetch_page(url):
    """
    Fetch the HTML content of a web page.

    Args:
        url (str): The target URL to request.

    Returns:
        str or None: The text content of the page if the request succeeds,
        otherwise None.
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        rspn = requests.get(url, headers=headers, timeout=10)
        rspn.raise_for_status()
        return rspn.text
    except Exception:
        return None


def parse_server_data(html):
    """
    Parse serialized server data from an Apple Music–like HTML page.

    The function looks for a <script> tag with id="serialized-server-data"
    and attempts to load the JSON contained within it.

    Args:
        html (str): Raw HTML content.

    Returns:
        dict or None: The parsed sections dictionary if found and valid,
        otherwise None.
    """
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.find("script", {"id": "serialized-server-data"})
    if not tag:
        return None

    try:
        data = json.loads(tag.text)
        return data[0]["data"]["sections"]
    except Exception:
        return None


def extract_header_sections(sections):
    """
    Extract specific sections from a list of server data sections.

    Searches for:
        - music-video-header
        - more-by-artist
        - more-in-genre

    Args:
        sections (list): List of section dictionaries.

    Returns:
        tuple: (header, more_by_artist, more_in_genre) where each element
        may be a dictionary or None.
    """
    header, more, similar = None, None, None

    for sec in sections:
        sec_id = sec.get("id", "")
        if "music-video-header" in sec_id:
            header = sec
        elif "more-by-artist" in sec_id:
            more = sec
        elif "more-in-genre" in sec_id:
            similar = sec

    return header, more, similar


def extract_video_header(header):
    """
    Extract key information from the music video header section.

    Args:
        header (dict): The header section dictionary.

    Returns:
        dict: A dictionary containing:
            - title (str)
            - artwork (dict)
            - artist_link (dict)
    """
    item = header.get("items", [{}])[0]
    return {
        "title": item.get("title", ""),
        "artwork": item.get("artwork", {}).get("dictionary", {}),
        "artist_link": item.get("subtitleLinks", [{}])[0],
    }


def extract_video_url(html):
    """
    Extract the direct video URL from JSON-LD schema data inside the HTML.

    Looks for a <script> tag with id="schema:music-video" and
    type="application/ld+json".

    Args:
        html (str): Raw HTML page content.

    Returns:
        str: The video content URL if found, otherwise an empty string.
    """
    soup = BeautifulSoup(html, "html.parser")
    try:
        json_tag = soup.find(
            "script",
            {"id": "schema:music-video", "type": "application/ld+json"},
        )
        sd = json.loads(json_tag.string)
        return sd["video"]["contentUrl"]
    except Exception:
        return ""


def extract_urls(section):
    """
    Extract action URLs from a section's item list.

    Args:
        section (dict or None): A section dictionary containing "items".

    Returns:
        list[str]: A list of extracted URLs. Empty if section is None
        or items contain no valid URLs.
    """
    if not section:
        return []
    urls = []
    for item in section.get("items", []):
        url = safe_action_url(item)
        if url:
            urls.append(url)
    return urls


def find_section_indices(sections):
    """
    Identify the indices of key sections in the album/server data.

    Scans each section's "id" field and maps matching identifiers to:
        - album
        - track_list
        - track_section
        - video
        - more
        - similar

    Args:
        sections (list[dict]): List of section dictionaries parsed from
            serialized server data.

    Returns:
        dict: A dictionary mapping section names to their index (int) or
        None if not found.
    """
    idx = {
        "album": None,
        "track_list": None,
        "track_section": None,
        "video": None,
        "more": None,
        "similar": None,
    }

    for i, sec in enumerate(sections):
        sec_id = sec.get("id", "")
        if "album-detail" in sec_id:
            idx["album"] = i
        elif "track-list " in sec_id:
            idx["track_list"] = i
        elif "track-list-section" in sec_id:
            idx["track_section"] = i
        elif "video" in sec_id:
            idx["video"] = i
        elif "more" in sec_id:
            idx["more"] = i
        elif "you-might-also-like" in sec_id:
            idx["similar"] = i

    return idx


def extract_album_header(item):
    """Extract title, image, caption, artist."""
    result = {
        "title": item.get("title", ""),
        "image": "",
        "caption": item.get(
            "modalPresentationDescriptor", {}
        ).get("paragraphText", ""),
        "artist": {"title": "", "url": ""},
    }

    # image
    artwork = item.get("artwork", {}).get("dictionary", {})
    result["image"] = get_cover(
        artwork.get("url", ""),
        artwork.get("width", 0),
        artwork.get("height", 0),
    )

    # artist
    try:
        sl = item.get("subtitleLinks", [])[0]
        result["artist"]["title"] = sl.get("title", "")
        result["artist"]["url"] = (
            sl["segue"]["actionMetrics"]
            ["data"][0]["fields"]["actionUrl"]
        )
    except Exception:
        pass

    return result


def extract_song_list(section):
    """
    Extract a list of song URLs from a track list section.

    Converts album URLs to song URLs using `convert_album_to_song_url`.

    Args:
        section (dict or None): The "track list" section.

    Returns:
        list[str]: A list of usable song URLs. Returns an empty list if
        the section is None or no valid URLs are found.
    """
    songs = []
    if not section:
        return songs

    for it in section.get("items", []):
        try:
            url = it["contentDescriptor"]["url"]
            song_url = convert_album_to_song_url(url)
            if song_url:
                songs.append(song_url)
        except Exception:
            continue

    return songs


def extract_more(sim_or_more_section):
    """
    Extract URLs from a 'more' or 'similar' section.

    Uses safe_action_url() to resolve the internal action URL.

    Args:
        sim_or_more_section (dict or None): The section containing items.

    Returns:
        list[str]: Extracted URLs. Empty list if section is None or has
        no valid items.
    """
    if not sim_or_more_section:
        return []

    urls = []
    for item in sim_or_more_section.get("items", []):
        url = safe_action_url(item)
        if url:
            urls.append(url)

    return urls


def extract_video_urls(section):
    """
    Extract the raw video URLs from a 'video' section.

    Args:
        section (dict or None): The section containing video items.

    Returns:
        list[str]: A list of video URLs. Returns an empty list if the
        section is None or contains no valid video entries.
    """
    vids = []
    if not section:
        return vids

    for v in section.get("items", []):
        try:
            vids.append(v["contentDescriptor"]["url"])
        except Exception:
            continue

    return vids


def parse_search_items(section, use_links=False):
    """
    Generic parser for Apple Music search result sections.

    Parameters
    ----------
    section : dict
        Section containing "items".
    use_links : bool
        If True, use titleLinks/subtitleLinks instead of title/subtitle.

    Returns
    -------
    list[dict]
    """
    items_out = []

    for item in section.get("items", []):
        try:
            url = item["contentDescriptor"]["url"]

            if use_links:
                title = item["titleLinks"][0]["title"]
                artist = item["subtitleLinks"][0]["title"]
            else:
                title = item.get("title", "")
                artist = item.get("subtitleLinks", [{}])[0].get("title", "")

            artwork = item.get("artwork", {}).get("dictionary", {})
            img = get_cover(
                artwork.get("url", ""),
                artwork.get("width", 0),
                artwork.get("height", 0),
            )

            items_out.append({
                "title": title,
                "artist": artist,
                "url": url,
                "image": img
            })

        except Exception:
            continue

    return items_out
