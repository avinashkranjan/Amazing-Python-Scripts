# YouTube API Video Search Example

This repository provides a simple Python script that demonstrates how to use the YouTube API to search for videos based on a query. The script fetches video details such as titles and video IDs from the search results.

## Prerequisites

- Python 3.x
- Install the `google-api-python-client` library using the following command:

```bash
pip install google-api-python-client
```

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/youtube-api-search.git
   ```

2. Navigate to the repository's directory:

   ```bash
   cd youtube-api-search
   ```

3. Replace `'YOUR_API_KEY'` with your actual YouTube API key in the `script.py` file.

4. Run the script using your Python interpreter:

   ```bash
   python script.py
   ```

## Usage

The `script.py` file in this repository contains the sample code to search for videos using the YouTube API. The script performs the following steps:

1. Imports the necessary libraries.
2. Initializes the YouTube API client with your API key.
3. Defines a search query.
4. Calls the `search.list` method to retrieve search results for videos.
5. Prints video information (title and video ID) from the search results.

The script can be easily customized for your use case, allowing you to explore more YouTube API features.

## Example Output

```
Video Title: Python Programming Tutorial - 1 | Python Tutorial For Beginners | Python Training | Edureka
Video ID: WGJJIrtnfpk
------------------------------
Video Title: Python Tutorial for Beginners [Full Course] 2019
Video ID: HBxCHonP6Ro
------------------------------
...
```

## Important Note

Please ensure that you handle your API keys securely and follow YouTube's API terms of service and usage guidelines. This example provides a starting point for using the YouTube API for video searches.

For more detailed information about the YouTube Data API and its capabilities, refer to the [official documentation](https://developers.google.com/youtube/v3).

