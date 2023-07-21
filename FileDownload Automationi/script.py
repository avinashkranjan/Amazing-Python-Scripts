import requests


def download_file(url, save_path, file_name):
    """
    Download a file from a given URL and save it to a specified directory.

    Parameters:
    - url (str): The URL of the file to be downloaded. 
                 Get the URL of download button through it's inspect button.
    - save_path (str): The directory path where the file will be saved.
    - file_name (str): The name to be used for the downloaded file.
    """
    response = requests.get(url)
    file_path = save_path + "\\" + file_name
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print("File downloaded successfully!")


# Example URL
file_url = "https://files.ceenaija.com/wp-content/uploads/music/2022/09/Keane_-_Somewhere_Only_We_Know_CeeNaija.com_.mp3"

# Example save path
save_path = r"C:\Users\hp\Music"

# Prompt user for file name
file_name = input("Enter the file name: ")

# Download the file
download_file(file_url, save_path, file_name)
