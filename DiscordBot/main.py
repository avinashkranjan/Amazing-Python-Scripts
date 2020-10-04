import discord
from discord.ext import commands


# your token here, inside the ""
TOKEN = ""
# channel to send welcome messages to
WELCOME_CHANNEL = "welcome"


# you can change the prefix here
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("bot started")


@bot.event
async def on_member_join(member):
    welcome_channel = discord.utils.get(
            member.guild.channels,
            name=WELCOME_CHANNEL
            )
    # feel free to change this message!
    await welcome_channel.send(f"welcome {member.mention}, please read our rules and have a great time!")


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


if __name__ == "__main__":
    bot.run(TOKEN)
