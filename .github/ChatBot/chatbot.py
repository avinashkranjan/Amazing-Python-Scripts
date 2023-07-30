import nltk
from nltk.chat.util import Chat, reflections
# Import patterns from the chat_patterns.py file
from chat_patterns import patterns

chatbot = Chat(patterns, reflections)


def start_chat():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    nltk.download('punkt')
    start_chat()
