# Import libraries
import googleapiclient.discovery
from google.oauth2 import service_account

# YouTube API credentials
API_KEY = ''  # Replace with your actual API key
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

# Path to your service account JSON key file
SERVICE_ACCOUNT_FILE = ''

# Authenticate with the YouTube Data API
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

youtube = googleapiclient.discovery.build(
    'youtube', 'v3', credentials=credentials)

# Define a function to get video statistics


def get_video_stats(video_id):
    # Retrieve live views and likes data
    request = youtube.videos().list(
        part='statistics',
        id=video_id
    )
    response = request.execute()

    # Extract live views and likes count from the API response
    if 'items' in response and len(response['items']) > 0:
        statistics = response['items'][0]['statistics']
        print(response)
        live_views = int(statistics['viewCount'])
        live_likes = int(statistics['likeCount'])
        live_comments = int(statistics['commentCount'])

        # Print the results
        print(f'Live views: {live_views}')
        print(f'Live likes: {live_likes}')
        print(f'Live Comments : {live_comments}')
    else:
        print('No video statistics found')


# Main function
def main():
    video_id = input("Enter Youtube Video Link : ")
    get_video_stats(video_id.split('/')[-1])


# Run the main function if this file is executed as a script
if __name__ == '__main__':
    main()
