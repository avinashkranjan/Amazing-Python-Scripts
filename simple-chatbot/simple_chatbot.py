from chatterbot import ChatBot
from chatterbot.Trainer import ChatterBotCorpusTrainer

bot = ChatBot("Pykit-Bot")
trainer = ChatBotCorpusTrainer(bot)
Trainer.train("chatterbot.corpus.english.conversation", "chatterbot.corpus.english.greetings")
my_input = input("ask me anything !")
response = bot.get_response(my_input)
