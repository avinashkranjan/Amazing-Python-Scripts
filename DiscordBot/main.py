import discord
from discord.ext import commands


# your token here, inside the ""
TOKEN = ""


# you can change the prefix here
bot = commands.Bot(command_prefix="!")


if __name__ == "__main__":
    bot.run(TOKEN)
