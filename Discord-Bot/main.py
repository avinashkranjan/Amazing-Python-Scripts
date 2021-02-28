import random

import discord
from discord.ext import commands

# your token here, inside the ""
TOKEN = ""
# channel to send welcome messages to
WELCOME_CHANNEL = "welcome"
# all the nicknames for the random_nickname command
NICKS = ["example1", "example2", "example3"]

# you can change the prefix here
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("bot started")


@bot.event
async def on_member_join(member):
    welcome_channel = discord.utils.get(member.guild.channels,
                                        name=WELCOME_CHANNEL)
    # feel free to change this message!
    await welcome_channel.send(
        f"welcome {member.mention}, please read our rules and have a great time!"
    )


@commands.has_permissions(ban_members=True)
@bot.command()
async def ban(ctx, user: discord.Member):
    """Ban the given user"""
    await ctx.guild.ban(user, delete_message_days=0)
    await ctx.send(f"banned {user}")


@commands.has_permissions(ban_members=True)
@bot.command()
async def unban(ctx, user: discord.User):
    "Unban the given user"
    await ctx.guild.unban(user)
    await ctx.send(f"unbanned {user}")


@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, user: discord.User):
    "Kick the given user"
    await ctx.guild.kick(user)
    await ctx.send(f"kicked {user}")


@bot.command(aliases=["rnick"])
async def random_nick(ctx):
    """Set your nickname to a random one"""
    new_nick = random.choice(NICKS)
    await ctx.author.edit(nick=new_nick)
    await ctx.send(f"Your new nickname is {new_nick}")


@commands.has_permissions(manage_nicknames=True)
@bot.command(aliases=["change_name"])
async def change_nick(ctx, user: discord.Member, *, new_nick):
    """Change somebody elses nickname."""
    await user.edit(nick=new_nick)
    await ctx.send(f"Changed the nick of {user.mention} to `{new_nick}`")


if __name__ == "__main__":
    bot.run(TOKEN)
