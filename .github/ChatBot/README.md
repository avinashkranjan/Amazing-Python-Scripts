# Rule Based Chatbot using NLTK

This is a simple rule based chatbot implemented using the Natural Language Toolkit (NLTK) library in Python. The chatbot engages in conversations with users by matching their input with predefined patterns and providing appropriate responses.

## How it Works

The chatbot is built using NLTK's `Chat` class, which allows us to define patterns and corresponding responses. When the user inputs a message, the chatbot searches for a pattern that matches the input and responds with the associated response. If there's no direct match, the chatbot provides a default response to handle any unrecognized inputs.

The predefined patterns cover a range of greetings, questions about the chatbot, jokes, recommendations, and handling user intentions. The chatbot is designed to respond politely and engagingly to various types of user queries.

## Usage

1. Run the `chatbot.py` script, and the chatbot will greet you with a welcome message.
2. Enter your message or query, and the chatbot will respond accordingly.
3. To stop the conversation, simply type `quit` as your input, and the chatbot will bid you goodbye.

## Improving the Chatbot

The predefined patterns can be expanded to make the chatbot more engaging and diverse. In the `chat_patterns.py` file, you can add more patterns and responses to handle a broader range of queries. By doing so, you can reduce the likelihood of default responses and create a more dynamic and interactive chatbot.

## Dependencies

To run the chatbot, ensure you have the following installed:

- Python 3.x
- NLTK library

You can install the required dependencies using pip:

```bash
pip install nltk
