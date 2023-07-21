# 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀 WELCOME TO SPACE NEWS AI CHAT MODEL 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀

from IPython import display
from PIL import Image
from playsound import playsound
from gtts import gTTS
import matplotlib.pyplot as plt
import urllib.request
import random
import io
import os
import requests
import time
import nasapy
print('🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀\n')

# Enter the API key of NASA
Api_Key = input("Enter the NASA API Key: ")

# Importing modules

# Function which handles the news data of space


def spaceNews():
    print("\nWhat day would you like to know ?")

    # Date must be between 16 Jun, 1995 and till now
    Date = input("Enter date {yyyy-mm-dd}: ")

    # Fetching data from the nasa
    print("\nExtracting Data......")
    print('\nPlease wait.....')
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)
    Params = {'date': str(Date)}
    r = requests.get(Url, params=Params)

    # Parsing the fetched data for displaying
    Data = r.json()

    # Parsing the extracted data
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']

    # Requesting for the image url to fetch and store into an array
    Image_r = requests.get(Image_Url)
    FileName = str(Date) + '.jpg'
    # Saving the images
    with open(FileName, 'wb') as f:
        f.write(Image_r.content)
    img = Image.open(FileName)

    # Clear the terminal for the next operation
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀\n')

    # Displaying the fetched data
    img.show()
    print(f"\nTitle of this news - {Title}")
    print(f"\nBrief Description \n\n{Info}")
    print(f"\nFileName - {FileName}\n")

# Function which fetch the mars images of different dates


def MarsImage():
    date = input("\nEnter date {yyyy-mm-dd}: ")
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&api_key={Api_Key}"

    # Fetching data from the internet
    r = requests.get(url)
    Data = r.json()

    # Extracting data from the fetched data set
    Photos = Data['photos'][0:9]

    if Data['photos'] == []:
        print("\nSorry, No data found!\n")
    else:
        for index, photo in enumerate(Photos):
            # Creating a lists of different values
            camera = photo['camera']
            full_camera_name = camera['full_name']
            date_of_photo = photo['earth_date']
            img_url = photo['img_src']

            # Downloading images from the internet
            p = requests.get(img_url)
            img = f'{index}.jpg'
            with open(img, 'wb') as file:
                file.write(p.content)
            os.startfile(img)

            print(
                f'Image "{index}.jpg" was captured with {full_camera_name} on {date_of_photo}\n')
            time.sleep(1)

# Function whixh tells about the number of asteroids in a range of dates


def Astro():
    # Getting two dates from the user for calculation of number of asteroids in between this range
    print("\nDifference between start and last dates is not more than 7 days.")
    print("\nNow, What's the start date ?")
    start_date = input("Enter date {yyyy-mm-dd}: ")  # Start date
    print("\nAnd the last date ?")
    end_date = input("Enter date {yyyy-mm-dd}: ")  # Last date

    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"

    # Fetching data from the internet
    r = requests.get(url)
    Data = r.json()

    # Clear the terminal for the next operation
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀\n')

    # Extracting data from the fetched data set
    Total_Astro = Data['element_count']
    print(
        f"\nTotal no. of asteroid falling on The Earth between {start_date} and {end_date} is : {Total_Astro} Asteroids\n")

    # enumarating the objects one by one
    neo = Data['near_earth_objects']

    for body in neo[start_date]:
        # parsing the object to extract 3 different values
        id = body['id']
        name = body['name']
        absolute = body['absolute_magnitude_h']

        # Finally printing the extracted data in a readable format
        print(id, name, absolute)

    print("\nID & Name of those asteroids are listed above.\n")

# Function which gives information about different solar bodies


def SolarBodies():
    print("\nExtracting data.....\n")
    print("\nPlease wait.....\n")

    # Link of the website to fetch data of different bodies of the solar system
    url = "https://api.le-systeme-solaire.net/rest/bodies/"

    # Fetching data from the internet
    r = requests.get(url)
    Data = r.json()  # Save the fetched data after converting into json object

    # Clear the terminal for the next operation
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀\n')

    # Listing the data / parsing the data set
    bodies = Data['bodies']
    Number = len(bodies)
    print(f"\nNumber of bodies in solar system : {Number}")

    try:
        # Getting input from the user
        Body = input(
            "\nTell me the name of the solar bodies you want to know - ")
        while (Body == None):
            Body = input("\nPlease enter the valid input - ")
        Body = Body.replace(" ", "")

        print("\nPlease wait......\n")

        # Fetching data for that body
        body = Body
        url_2 = f"https://api.le-systeme-solaire.net/rest/bodies/{body}"
        rrr = requests.get(url_2)  # Fetchin data from the internet
        data = rrr.json()

        # Listing / parsing the dataset
        mass_1 = data['mass']['massValue']
        mass = mass_1*1000  # Converting mass into the trillion tons unit
        volume = data['vol']['volValue']
        density = data['density']
        gravity = data['gravity']
        escape = data['escape']
        radius = data['meanRadius']
        avgTemp = data['avgTemp']
        str = data['bodyType']

        # Displaying the fetched data set in a readable / understandable format
        print(
            f"\n------------------------------- Data of {body} -------------------------------------")
        print(f"\n       Mass of {body} - {mass} trillion tons")
        print(f"\n       Volume of {body} - {volume} trillion kilometer^cube")
        print(
            f"\n       Gravity of {body} - {gravity} meter per second^square")
        print(
            f"\n       Escape Velocity of {body} - {escape} meter per second")
        print(
            f"\n       Density of {body} - {density} gram per centimeter^cube")
        print(f"\n       Radius of {body} - {radius} kilometer")
        print(f"\n       Average Temperature of {body} - {avgTemp} Kelvin")
        print(f"\n       Body Type of {body} - {str}")
        print(f"\n-----------------------------------------------------------------------------------\n")
    except:
        print(f"\nData of {body} is not found!\n")

# Function which fetch the images of different solar bodies


def solarBodiesPictures():
    # List of different images for displaying to the user
    # Keys of Google drive images
    imageKeys = [
        '1rktYDEGz0Y95PmN1sJlp0oWchznNBxFY',
        '18p1HDuJzf_0Xa-70pHm7okK_ZtcfnPs3',
        '1uc85CRZD9m_K5N3sZHh97l9laas9y5yd',
        '1zFsOQ3vca-x-UhUK7hzxdAQzuJ0tGIWr',
        '1Ae8zekmbQ7fhFA5ZpCSNVwnuBdDSLtxt',
        '1K6O-xQPz5G35pEtaYdjkRHdpk0ZtOTSd',
        '1SzvHL_E8uA7Hq7D3SDmIAmuaGyzpc4I_',
        '1WUn2Kq0iBnmajNHOggIAwt-nhefhZGOM',
        '16KhTjl3Mw9LZ-3Ed2Mic4E2HCb6KteZW',
        '1taq_Q1JjWKQqrWLB5Fpuhm1Utl8v0wtl',
        '1uySzU1yyDv5aQF9YEFcYQwUcmOlFV-j9',
        '1Sj0CtJ_kHbM03geTs-FmKPj5IBafdfyP',
        '1rgSN5kjGR_iR5w0vqAUDEEZbWctzn_dE',
        '1_zAN7M2pfw0tF5Lss453gjC41HZcxI74',
        '1Pa_x3o4FcYbnGyC2nibMYhg-ZGr-0EtC',
        '1mPlEp4Okgqad001RnOsjvSMyVZiKBFqY',
        '1PmBullQHcZhmP1ook9NKkYVaO9_vI1KH',
        '1dFXMnIePv6SgPtHKJNhllHd6o25IaUFO',
        '1eNJlTy5_MHaFMdH4FSXxwhGXsDriZmTF',
        '1wxokZjLeJKRufBwlzCqnTGVOi9Oj8D5v',
        '1urlYip6h0-su85TdWqa0vaXrOtEptbHD',
        '1j7jWkVihd2VFcr0C-FcKTFqptLu6cbwQ',
        '1IYcfhxtr02mYNAAjt1cpa196LDSBO3H-',
        '1zNQwgjG-_pBsDuvgXyjndA0ld51LQD1i',
        '1HktS1ginfv2QWOjLINa_r5IXJIv-nE_I'
    ]

    print("Extracting data.....\n")
    # Selecting a random image key
    imageKey = random.choice(imageKeys)
    imageURL = f'https://drive.google.com/uc?export=view&id={imageKey}'

    # Fetch the image content
    response = requests.get(imageURL)
    image_content = response.content

    # Load the image using PIL
    image = Image.open(io.BytesIO(image_content))

    print('\nLoading image.....\n')
    # Display the image
    plt.figure()
    plt.imshow(image)
    plt.axis('off')
    plt.show()

# This function will tells about the current news of space with images


def todayNews():
    nasa = nasapy.Nasa(key=Api_Key)

    # Get today's date in YYYY-MM-DD format:
    d = input("Enter date {yyyy-mm-dd}: ")

    print('\nExtracting data....\n')
    print('\nPlease wait.....\n')

    # Get the image data:
    apod = nasa.picture_of_the_day(date=d, hd=True)

    # POINT A:
    # Check the media type available:
    if (apod["media_type"] == "image"):

        # POINT B:
        # Displaying hd images only:
        if ("hdurl" in apod.keys()):

            # POINT C:
            # Saving name for image:
            title = d + "_" + \
                apod["title"].replace(" ", "_").replace(":", "_") + ".jpg"

            # POINT D:
            # Path of the directory:
            image_dir = "./"

            # Checking if the directory already exists?
            dir_res = os.path.exists(image_dir)

            # If it doesn't exist then make a new directory:
            if (dir_res == False):
                os.makedirs(image_dir)

            # POINT E:
            # Retrieving the image:
            urllib.request.urlretrieve(
                url=apod["hdurl"], filename=os.path.join(image_dir, title))

            # Clear the terminal for the next operation
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀\n')

            # POINT F:
            # Displaying information related to image:
            if ("date" in apod.keys()):
                print("Date image released: ", apod["date"])
                print("\n")

            if ("copyright" in apod.keys()):
                print("This image is owned by: ", apod["copyright"])
                print("\n")

            if ("title" in apod.keys()):
                print("Title of the image: ", apod["title"])
                print("\n")

            if ("explanation" in apod.keys()):
                print("Description for the image: ", apod["explanation"])
                print("\n")

            if ("hdurl" in apod.keys()):
                print("URL for this image: ", apod["hdurl"])
                print("\n")

            # POINT G:
            # Displaying main image:
            img = Image.open(os.path.join(image_dir, title))
            img.show()

            # Point H:
            # Text to Speech Conversion:
            # Take input from user:
            choice = input("\nPress * to hear the audio explanation : ")
            if (choice == "*"):
                # Text to be converted:
                mytext = apod["explanation"]

                # Creating an object:
                myobj = gTTS(text=mytext, lang="en", slow=False)

                # Generating audio file name:
                audio_title = d + "_" + apod["title"] + ".mp3"

                # Save the converted file:
                myobj.save(os.path.join(image_dir, audio_title))

                # Name of sound file:
                sound_file = os.path.join(image_dir, audio_title)

                # Playing the converted file
                display.display(display.Audio(sound_file, autoplay=True))

                playsound(f'.\\{audio_title}')

    # POINT I:
    # If media type is not image:
    else:
        print("\nSorry, Image not available!\n")
        time.sleep(2)

# Function which keeps holding all the other functions


def SpaceNews():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('''
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀 WELCOME TO SPACE AI CHAT MODEL 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
                                               (By Avdhesh Varshney)
                                        (https://github.com/Avdhesh-Varshney)

                                            1. Today space news
                                            2. Any other day of space news
                                            3. Display mars images
                                            4. Display data of asteroids
                                            5. About any solar bodies
                                            6. Pictures of solar bodies

                                            0. To exit the program

🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
        ''')

        choice = input("Please enter your choice: ")
        while choice.isdigit() == False:
            choice = input("\nPlease enter value in the range [0-6] - ")
        choice = int(choice)

        # Clear the terminal for the next operation
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀\n')

        if choice == 0:
            print("Thanks for coming !")
            print('\n🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀\n')
            time.sleep(2)
            exit()

        elif choice == 1:
            todayNews()

        elif choice == 2:
            spaceNews()

        elif choice == 3:
            MarsImage()

        elif choice == 4:
            Astro()

        elif choice == 5:
            SolarBodies()

        elif choice == 6:
            solarBodiesPictures()

        else:
            print("\nYou have entered the wrong choice !\n")

        print('\n🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀\n')
        input('\nPress "Enter" key to proceed further...\n')


# Program starts
SpaceNews()
