#use the following command to install instaloader
#pip3 install instaloader

import instaloader
username = str(input('Enter username: '))
x = instaloader.Instaloader()
print(x.download_profile(username, profile_pic_only=True))
