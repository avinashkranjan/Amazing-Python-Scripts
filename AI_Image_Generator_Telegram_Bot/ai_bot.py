from dotenv import load_dotenv
import os
from telegram import Update
import replicate
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

load_dotenv()


def getUrl(prompt):
    a = replicate.run(
        "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
        input={"prompt": prompt}
    )
    print(a)
    return a[0]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Hello {update.effective_user.first_name} I am your personal AI Image Generator \n Use /help to know all commands.")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        '''Here are a list of all commands:-
        /start - Start a conversation
        /help - Get a list of commands
        /imagine <prompt> - Get an AI generated image'''
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
        Sorry, I did not understand that command.
        Type \" /help \" to see all possible commands""")


async def imagine(update: Update, context: ContextTypes.DEFAULT_TYPE):
    arg = str(" ".join(context.args))
    url = getUrl(arg)
    await update.message.reply_photo(url)


app = ApplicationBuilder().token(os.environ.get('TELEGRAM_BOT_TOKEN')).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("imagine", imagine))
app.add_handler(MessageHandler(filters.COMMAND, handle_message))
app.run_polling()
