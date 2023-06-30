# Telegram AI Image Generator Bot 
This is an AI Image generator bot. It can create original images from a single text prompt!


# Screenshot
![Bot Screenshot](telegramBotScreenShot.png)


# Getting Started
This package is simple to use and allows to build an image generation telegram bot

## Prerequisites

 - Python
 - Telegram Bot API Key
 - Replicate Stable Diffusion API Key

## Installation

 

 1. Get a free telegram bot API key from @BotFather telegram bot. 
 2. Also get a free stable diffusion API key from https://replicate.com/account/api-tokens
![Replicate Screenshot](replicatess.png)
 3. Clone the repo
`git clone https://github.com/<your_username>/Amazing-Python-Scripts`
`cd ai_image_generation_telegram_bot`
 3. Install the requirements from the requirements.txt file
 ` pip install -r requirements.txt`
 4. Enter the bot token from BotFather in the **TELEGRAM_BOT_TOKEN** in the .env file.
 5. Enter the bot token from Replicate in the **REPLICATE_API_TOKEN** in the .env file.
 6. Now run the ai_bot.py file and start chatting.

# Bot Commands
You can see a list of commands by typing */help*

| Commands          | Description                                   |
|-------------------|-----------------------------------------------|
| /start            | Start a conversation                          |
| /help             | Get a list of all the commands                |
| /imagine `prompt` | Create an image based on the given command    |

#
*Created by [Arnav Kohli](https://github.com/THEGAMECHANGER416)*