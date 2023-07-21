import requests
import telebot

bot_token = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Send me a city name")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    response = requests.get("http://api.weatherapi.com/v1/current.json?key={}&q={}".format(
        "2d3f4a2bd175414aa45175205221408", message.text)).json()
    bot.send_message(
        message.chat.id, format_response_to_human_readable(response))


def format_response_to_human_readable(response):
    location = response["location"]
    current = response["current"]
    astronomy = response["forecast"]["forecastday"][0]["astro"]

    return "Weather Information for {}\n"\
           "Temperature: {}°C\n"\
           "Wind: {} kph, {}\n"\
           "Humidity: {}%\n"\
           "Pressure: {} mb\n"\
           "Sunrise: {}\n"\
           "Sunset: {}\n"\
           "Day Length: {} hours {} minutes".format(
               location["name"],
               current["temp_c"],
               current["wind_kph"],
               current["wind_dir"],
               current["humidity"],
               current["pressure_mb"],
               astronomy["sunrise"],
               astronomy["sunset"],
               astronomy["sunrise"],
               astronomy["sunset"],
               astronomy["moon_phase"]
           )


bot.infinity_polling()
