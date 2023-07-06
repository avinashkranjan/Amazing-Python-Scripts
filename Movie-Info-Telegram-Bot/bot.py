import logging
import requests
import re
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import itertools
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import decouple

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = decouple.config("API_KEY")

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        'What can this bot do?\n\nThis bot gives brief information about any movie from IMDb website'
        + '\nSend /name movie_name to know the genre and rating of the movie.\nSend /genre genre_name to'
        + 'get the list of movies belonging to that genre'
    )


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def genre(update, context):
    """Send a list of movies when the command /genre is issued."""
    url = 'https://www.imdb.com/search/title/'
    genre = str(update.message.text)[7:]
    print(genre)
    r = requests.get(url+'?genres='+genre)
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.find('title')
    if title.string == 'IMDb: Advanced Title Search - IMDb':
        update.message.reply_text("Sorry,No such genre.Try again")
    else:
        res = []
        res.append(title.string+'\n')
        tags = soup('a')
        for tag in tags:
            movie = re.search('<a href=\"/title/.*>(.*?)</a>', str(tag))
            try:
                if "&amp;" in movie.group(1):
                    movie.group(1).replace("&amp;", "&")
                res.append(movie.group(1))
            except:
                pass
        stri = ""
        for i in res:
            stri += i+'\n'
        update.message.reply_text(stri)


def name(update, context):
    """Send the first 3 search results of the movie name in IMDb site when the command /name is issued."""
    movie = str(update.message.text)[6:]
    print(movie)
    res = get_info(movie)
    stri = ""
    for i in res:
        for a in i:
            stri += a+'\n'
        stri += '\n'
    update.message.reply_text(stri)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def get_info(movie):
    "To scrape IMDb and get genre and rating of the movie "
    url = 'https://www.imdb.com/find?q='
    r = requests.get(url+movie+'&ref_=nv_sr_sm')
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.find('title')
    tags = soup('a')
    pre_url = ""
    count = 0
    lis = []
    res = []
    for tag in tags:
        if(count > 2):
            break
        m = re.search('<a href=.*>(.*?)</a>', str(tag))
        try:
            lis = []
            link = re.search('/title/(.*?)/', str(m))
            new_url = 'https://www.imdb.com'+str(link.group(0))
            if new_url != pre_url:
                html = requests.get(new_url)
                soup2 = BeautifulSoup(html.text, "html.parser")
                movietitle = soup2.find('title').string.replace('- IMDb', ' ')
                a = soup2('a')
                span = soup2('director')
                for item in span:
                    print(item)
                genrestring = "Genre : "
                for j in a:
                    genre = re.search(
                        '<a href=\"/search/title\?genres=.*> (.*?)</a>', str(j))
                    try:
                        genrestring += genre.group(1)+' '
                    except:
                        pass
                atag = soup2('strong')
                for i in atag:
                    rating = re.search('<strong title=\"(.*?) based', str(i))
                    try:
                        rstring = "IMDb Rating : "+rating.group(1)
                    except:
                        pass
                details = "For more details : "+new_url
                lis.append(movietitle)
                lis.append(genrestring)
                lis.append(rstring)
                lis.append(details)
                pre_url = new_url
                count += 1
                res.append(lis)
        except:
            pass
    return res


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - reply in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("name", name))
    dp.add_handler(CommandHandler("genre", genre))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
