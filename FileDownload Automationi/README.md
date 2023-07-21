# File Downloader

This script allows you to easily download files from a given URL and save them to a local directory. It utilizes the `requests` library to handle the HTTP requests and provide a convenient way to download files.

## Prerequisites

Before running this script, ensure that you have the following installed:

- Python 3.x
- The `requests` library. You can install it by running the following command:

  ```
  pip install requests
  ```

## Usage

1. Import the `requests` library:

   ```python
   import requests
   ```

2. Define the `download_file` function, which takes three parameters: `url`, `save_path`, and `file_name`. This function downloads the file from the provided URL and saves it to the specified location.

   ```python
   def download_file(url, save_path, file_name):
       response = requests.get(url)
       file_path = save_path + "\\" + file_name
       with open(file_path, 'wb') as file:
           file.write(response.content)
       print("File downloaded successfully!")
   ```

3. Provide the necessary information:

   - Specify the URL of the file you want to download:

     ```python
     file_url = "https://files.ceenaija.com/wp-content/uploads/music/2022/09/Keane_-_Somewhere_Only_We_Know_CeeNaija.com_.mp3"
     ```

   - Set the save path where you want to store the file. Replace `YOUR_SAVE_PATH` with the desired directory path:

     ```python
     save_path = r"YOUR_SAVE_PATH"
     ```

   - Prompt the user to enter the desired file name:

     ```python
     file_name = input("Enter the file name: ")
     ```

4. Download the file by calling the `download_file` function with the provided parameters:

   ```python
   download_file(file_url, save_path, file_name)
   ```

The file will be downloaded and saved to the specified location. You can customize the script to fit your specific needs by modifying the URL, save path, and file name.
