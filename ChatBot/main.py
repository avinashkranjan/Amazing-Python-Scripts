import discord
import openai
import logging
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='?', intents=intents)
openai.api_key = "sk-j1rJknittI0TDNEpUTHQoQUJMHLrErGJyHg89uy71MyuHb4a"
token = "MTA4NjIyMDc5NTIxMjIyMjQ2NQ.GfPEh0.RowJPDw0TUb5S1rUAdZARDaYQRHkhbudgATC14"

# Configure logging
logging.basicConfig(level=logging.ERROR)

@client.event
async def on_ready():
    print('I am ready')

@client.event
async def on_message(message):
    # Ignore messages sent by the bot
    if message.author.bot:
        return

    # Use the GPT-3 API to generate a response
    if message.content.startswith('?'):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=f"{message.content}\n",
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            # Send the response back to the user
            await message.channel.send(response.choices[0].text)
        except Exception as e:
            logging.error(f"Error occurred during API call: {e}")

    # Call the regular command handler for other messages
    await client.process_commands(message)

@client.command()
async def hi(ctx):
    await ctx.send(f"Hi there {ctx.author.mention}")

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def echo(ctx, *, message):
    await ctx.send(message)

client.run(token)
