from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import re

# function to get contents of url(public api) using requests


def gett():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


# function to check allowed extension


def image_urll():
    extension = ['jpg', 'jpeg', 'png']
    ext = ''
    while ext not in extension:
        url = gett()
        ext = re.search("([^.]*)$", url).group(1).lower()
    return url


def get():
    contents = requests.get('https://xkcd.com/info.0.json').json()
    img = contents['img']
    return img


def image_url():
    extension = ['jpg', 'jpeg', 'png']
    ext = ''
    while ext not in extension:
        img = get()
        ext = re.search("([^.]*)$", img).group(1).lower()
    return img


# function to display dog picture


def dog(update, context):
    url = image_urll()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)


# function to display meme


def meme(update, context):
    img = image_url()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)


# Welcome message will be displayed when /hi command is sent


def hi(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hi! I am telebot...How is it going.")


# tongue-twister will be displayed when /play command is sent


def play(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Let's have fun!Repeat this tongue twister 5 times:She sells seashells by the seashore."
    )


# Displays message when incorrect command is sent


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Please type the right command.")


# your token token has to be provided in <<YOUR-TOKEN>> place


def main():
    upd = Updater('<<YOUR-TOKEN>>', use_context=True)
    disp = upd.dispatcher
    unknown_handler = MessageHandler(Filters.command, unknown)
    hi_handler = CommandHandler('hi', hi)
    disp.add_handler(CommandHandler('meme', meme))
    disp.add_handler(CommandHandler('play', play))
    disp.add_handler(CommandHandler('dog', dog))
    disp.add_handler(hi_handler)
    disp.add_handler(unknown_handler)
    upd.start_polling()
    upd.idle()


main()
