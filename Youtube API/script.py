from googleapiclient.discovery import build

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Define the search query
search_query = 'python programming tutorial'

# Call the search.list method to retrieve search results
search_response = youtube.search().list(
    q=search_query,
    type='video',
    part='id,snippet',
    maxResults=10
).execute()

# Print video information from the search results
for item in search_response['items']:
    video_title = item['snippet']['title']
    video_id = item['id']['videoId']
    print(f"Video Title: {video_title}")
    print(f"Video ID: {video_id}")
    print("------------------------------")
