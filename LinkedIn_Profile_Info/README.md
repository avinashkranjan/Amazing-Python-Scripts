# LinkedIn Profile Picture

Python package to crawl LinkedIn profile pictures using the Google Custom Search API.

## Overview

This Python package allows you to retrieve LinkedIn profile pictures by providing the profile URL. The package uses the Google Custom Search API to search for the profile pictures associated with the LinkedIn ID.

## Features

- Retrieve LinkedIn profile picture URL using the profile URL.
- Get additional profile information such as name, headline, and public URL.

## Installation

You can install the package using pip:

```bash
pip install linkedin-profile-picture
```
## Information about Google API

The proper code for google API is in google_API.py

The provided code defines a Python class called GoogleSearchAPI, which is designed to interact with the Google Custom Search API to perform custom searches on Google and retrieve search results related to specific LinkedIn profiles. Let's explain how this code can be used and how it fits into a larger context:

1. GoogleSearchAPI class:

- Initialization (__init__): The GoogleSearchAPI class is initialized with two parameters: key and cx. These parameters represent the API key and custom search engine ID required to access the Google Custom Search API.

- API Request (_hit_api): The _hit_api method is responsible for making requests to the Google Custom Search API. It takes a LinkedIn ID (extracted from the LinkedIn profile URL) as input and constructs a request to search for results related to that ID. The method supports pagination to retrieve multiple pages of search results.

- Response Handling (_create_api_response): The _create_api_response method processes the API response and extracts relevant information from it. If the API response status code is 200, it retrieves search results and stores them in the results list. Otherwise, it stores the error response in the error attribute of an APIResponse object.

2. Usage:
To use the GoogleSearchAPI class, you would typically do the following steps:

- Import the required modules and create an instance of the GoogleSearchAPI class, providing your API key and custom search engine ID.

Get the LinkedIn profile URL for which you want to find the profile picture. Extract the LinkedIn ID from this URL using the extract_id method of the ProfilePicture class.

- Use the get_profile_picture method of the ProfilePicture class to get the profile picture URL by passing the LinkedIn profile URL as input. This method internally uses the GoogleSearchAPI class to perform the custom search and extract the profile picture URL.

- Optionally, you can use the get_profile_info method of the ProfilePicture class to fetch additional profile information like name, headline, and public URL from the LinkedIn profile.

3. API Rate Limiting:
The code handles API rate limiting gracefully. If the Google Custom Search API returns a status code of 429 (Too Many Requests), it means the API rate limit has been reached for a particular period. In such cases, the code waits for the number of seconds specified in the "Retry-After" header sent by the API and then retries the API request. This ensures that the code doesn't exceed the API rate limit and avoids getting blocked.