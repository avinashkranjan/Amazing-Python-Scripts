# The required libraries

import discord
import schedule
import asyncio
import requests
import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'
# Get a key at https://platform.openai.com/docs/api-reference


CLIENT_TOKEN = 'YOUR_DISCORD_TOKEN'
# Get a token at the discord developer portal https://discord.com/developers/docs/intro

CHANNEL_ID = "CHANNEL_ID"
# The channel ID, AKA the channel in which the bot will send news articles in

url = "https://newsapi.org/v2/top-headlines"
params = {
    "country": "us",
    "apiKey": "YOUR_NEWS_API_KEY"
    # Generate your API key from https://newsapi.org
}


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

latest_url = ""


def get_latest_article():
    global latest_article
    response = requests.get(url, params=params)
    articles = response.json()['articles']
    latest_article = articles[0]
    return latest_article


async def send_article():
    global latest_url
    latest_article = get_latest_article()
    if latest_article['url'] != latest_url:
        channel = await client.fetch_channel(CHANNEL_ID)
        message = f"New article: {latest_article['title']} - {latest_article['url']}"
        await channel.send(message)
        latest_url = latest_article['url']
        response_text = f'\n {message}'

        # Feel free to add your own prompts
        prompt = "Come up with a sarcastic response to this news article " + response_text
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        sarcastic_response = response.choices[0].text.strip()
        if sarcastic_response:
            await channel.send(sarcastic_response)
    else:
        return 'no update found'


@client.event
async def on_ready():
    print('Bot is ready.')
    schedule.every(10).minutes.do(send_article)

    while True:
        await send_article()
        # wait for 10 minutes before sending the next article to avoid using to many resources
        await asyncio.sleep(10*60)


client.run(CLIENT_TOKEN)
