import requests


def download_file(url, destination):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print("File downloaded successfully.")
    else:
        print("Failed to download file.")


# Example usage: Download a file from a URL
file_url = 'https://example.com/path/to/file.txt'
save_as = 'downloaded_file.txt'
download_file(file_url, save_as)
