import requests


def get_linkedin_posts(access_token):
    url = 'https://api.linkedin.com/v2/shares?q=owners&owners=urn:li:person:YOUR_USER_ID&count=10'
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        posts = data.get('elements', [])
        for post in posts:
            post_text = post.get('text', '')
            print(post_text)
    else:
        print(
            f"Error: {response.status_code} - {data.get('message', 'Unknown error')}")


if __name__ == "__main__":
    # Replace YOUR_ACCESS_TOKEN and YOUR_USER_ID with appropriate values
    access_token = "YOUR_ACCESS_TOKEN"
    get_linkedin_posts(access_token)
