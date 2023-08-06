# Predefined patterns and responses for the chatbot

patterns = [
    # Greetings
    (r'hi|hello|hey', ['Hello!', 'Hi!', 'Hey!', 'Hi there!']),
    (r'how are you?', ['I am good, thank you!',
     'I am doing well!', 'All good!', 'I\'m fine, thanks!']),
    (r'what is your name?', ['You can call me Chatbot.',
     'I am Chatbot!', 'My name is Chatbot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!',
     'Bye!', 'Have a great day!']),

    # Jokes
    (r'tell me a joke', ['Why don’t scientists trust atoms? Because they make up everything!',
                         'Parallel lines have so much in common. It’s a shame they’ll never meet.',
                         'Why did the scarecrow win an award? Because he was outstanding in his field!']),

    # Age
    (r'how old are you?', ['I am a computer program, so I don\'t have an age!',
                           'Age is just a number, and I don\'t have one!']),

    # Creator
    (r'who created you?', ['I was created by OpenAI.',
     'My creators are from OpenAI.']),

    # Compliments
    (r'(.*) (like|love) you', ["Aw, that's so sweet!",
     "Thank you! I really appreciate it."]),
    (r'you are (.*)(good|awesome|amazing)',
     ["Thank you! I'm here to assist you.", "I'm glad you think so!"]),

    # Weather
    (r'(.*) (weather|temperature) today', ["I'm sorry, I am just a chatbot and don't have access to real-time data.",
                                           "You can check the weather online or through a weather app."]),

    # Recommendations
    (r'(.*) (movie|book) (recommendation|recommend)', ["I recommend you watch 'The Shawshank Redemption' or read 'To Kill a Mockingbird'.",
                                                       "You might enjoy 'Inception' or 'The Great Gatsby'.",
                                                       "If you like action, 'The Dark Knight' is a great choice."]),

    # How to create/build something
    (r'how (can|do) (I|you) (create|build) (a|an) (.*)', ["To create {4}, you can follow these steps...",
                                                          "Building {4} requires some technical knowledge, but here are the basics...",
                                                          "Sure! Here's a basic guide on building {4}..."]),

    # User intentions
    (r'I (want|need) (.*)',
     ["Why do you need {1}?", "What would you do with {1}?"]),
    (r'I am (feeling|looking) (.*)',
     ["Why are you feeling {1}?", "Tell me more about why you are {1}."]),

    # More patterns and responses to handle different queries
    # Add more patterns and responses here to make the chatbot more engaging and diverse

    # Default response
    (r'.*', ["I'm sorry, I don't quite understand. Could you please rephrase that?",
             "I'm still learning, and I'm not sure how to respond to that.",
             "Let's talk about something else. What else would you like to know?"]),
]
