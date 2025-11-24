# Apple Music Scraper

A powerful unofficial scraper for extracting structured metadata from Apple Music web pages using web-scraping techniques and reverse-engineered `serialized-server-data`.  
This tool is for **educational purposes only** and does **not** use any official Apple API.

- **Functionalities**
  - Search for artists, songs, albums, playlists, and videos
  - Extract song metadata and preview URLs
  - Fetch album details including tracks, artist info, similar albums, and videos
  - Scrape playlist and shared room song URLs
  - Retrieve video metadata and direct video links
  - Fetch full artist information including top songs, albums, biography, and more

---

## Setup Instructions

1. Clone or download the project  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Import and use the scraper in your Python script:
   ```python
   result = search('night tapes')
   artists = result['artists']

   artist_url = artists[0]['url']
   artist = artist_scrape(artist_url)

   latest_night_tapes_song_url = artist['latest']

   song = album_scrape(latest_night_tapes_song_url)
   song_name = song['title']
   song_cover = song['image']

   print(f"\nLatest Night Tapes Song: {song_name}\nCover Art: {song_cover}\n")
   ```

---

## Detailed Explanation

Each scraping function processes the `serialized-server-data` embedded in Apple Music’s webpage structure.  
The scraper extracts metadata such as:
- Titles, URLs, artwork
- Track lists
- Preview links
- Album/artist relationships
- Related videos or albums  
All results are returned as **structured JSON objects** for easy access in your applications.

---

## Output

The scraper returns JSON structures like:

```json
{
  "title": "Example Song",
  "artist": "Example Artist",
  "image": "https://example-image.jpg",
  "preview": "https://example-preview.m4a",
  "related": [...],
  "songs": [...]
}
```

You can log these results, display them in an interface, or process them however you like.

---

## Author

- [**Abssdghi**](https://github.com/Abssdghi)

---

## Disclaimers

- This project is **not affiliated with Apple Inc.**  
- It uses **web scraping** and may break if Apple changes its internal web structure.  
- For **educational and personal use only**. Redistribution of scraped content may violate Apple Music’s Terms of Service.
