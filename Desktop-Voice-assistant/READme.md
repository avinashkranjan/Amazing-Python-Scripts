# DESKTOP VOICE ASSISTANT
It would be great to have a desktop voice assistant who could perform tasks like sending email, playing music, search wikipedia on its own when we ask it to. This desktop assistant does exactly that for the user.


# What tasks can it perform?
    1. It can send emails on your behalf.
    2. It can search wikipedia and read the first few lines for you.
    3. It can open youtube, google, facebook and spotify.
    4. Send messages in whatsapp on your behalf.
    5. Tell you jokes.
    6. Tell date and time for you.
    7. Open apps on your device.


# How to use 
    1. Start the assistant.
    2. Keep giving the required commands
    3. If done say 'no thanks' and the assistant will stop itself


# Side note
  Make sure you set Master as your name. (line 21)
  Enter the email and app password. (line 63)
  You need to be logged into whatsapp for using the assistant to send whatsapp messages. (While using 'Send Whatsapp message' option


# Additional features:
  You can use it to open apps on your device like word, one note, notepad, VS code etc.
  The path will vary from user to user.
  Here is the code you can use:

    import os
    elif 'Open <App name>' in query:
     path= "Location of the application"
     os.startfile(path)


# For using the mailSent function:
  Here for making the sent Email function work, there are certain changes that should be made in respective device or else the function won't work and a error will pop up
  For the function to work:
    1. In google search "Less secured apps in gmail"
    2. Select "Control access to less secure apps"
    3. Here enable the less secure apps for the account you will be using to send emails
  Now its a concern of security if we have to write our password this way
    for no privacy breach we can use the following steps:
    1. Go to goole and search "App passwords google"
    2. Open "App passwords-Sign in Google"
    3. Sign in the with the account you want to use for sending emails using this
    4.Under "select the app and device you want generate password for"
         i> Select App= Mail   Select Device= Windows 10
         ii>Click on generate
    5. Copy the app password and use it here.


# Development Status
The amount of things that can be done with this AI assistant is endless. This is just a basic structure which is at present complete. It might be using hotwords in future that will trigger the assistant, , might be used in sending the system to sleep mode, set alarm, send text messages to contacts on your phone and lot more.


# Developed by Sayantani Saha
