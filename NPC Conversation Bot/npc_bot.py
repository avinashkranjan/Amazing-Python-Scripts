import random
import nltk
from nltk.chat.util import Chat, reflections

# conversation patterns and responses
conversation_patterns = [
    (r'hello|hi|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you|how\'s it going', ['I\'m just a computer program, but I\'m doing well!', 'I don\'t have feelings, but I\'m here to help.']),
    (r'what\'s your name', ['I\'m the NPC Bot. How can I assist you?', 'Call me NPC Bot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Farewell!']),
    (r'who are you', ['I\'m your friendly NPC assistant!', 'I\'m here to provide information and chat with you.']),
    (r'what can you do', ['I can answer questions, chat with you, and assist you in various tasks. Just ask!', 'I\'m here to engage in conversation and help you out.']),
    (r'tell me a joke', ['Sure, here\'s one: Why don\'t scientists trust atoms? Because they make up everything!', 'Why did the chicken go to the seance? To talk to the other side!']),
    (r'how old are you', ['I\'m a virtual creation, so I don\'t age. But I\'m up-to-date with information!']),
    (r'help', ['Sure, I can assist you with various tasks. You can ask about weather, news, or even have a general chat. Just let me know!']),
    (r'weather', ['I can provide weather information for your location. Please tell me the city name.']),
    (r'news', ['I can fetch the latest news headlines for you. Would you like news on a specific topic or general headlines?']),
    (r'.*', ['Interesting. Please tell me more.', 'I\'m here to listen. Feel free to share your thoughts.', 'I\'m not sure I understand. Can you explain further?'])
]

def fetch_weather(city):
    # For this example, return a hardcoded response
    return f"The weather in {city} is currently sunny with a temperature of 25°C."

def fetch_news(topic=None):
    # For this example, return a hardcoded response
    if topic:
        return f"Here are the latest news headlines on {topic}: ..."
    else:
        return "Here are the latest general news headlines: ..."

def npc_conversation():
    print("NPC Bot: Hello! How can I help you today?")
    chatbot = Chat(conversation_patterns, reflections)
    
    while True:
        player_input = input("You: ").lower()
        if player_input == 'exit':
            print("NPC Bot: Goodbye!")
            break
        elif 'weather' in player_input:
            city = input("Please provide the city name: ")
            response = fetch_weather(city)
        elif 'news' in player_input:
            topic = input("Please specify a news topic (optional): ")
            response = fetch_news(topic)
        else:
            response = chatbot.respond(player_input)
        print("NPC Bot:", response)

if __name__ == "__main__":
    nltk.download('punkt')
    npc_conversation()
