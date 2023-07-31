# AI-Based Chatbot

An AI-based chatbot implemented in Python using the spaCy NLP library. The chatbot is designed to engage in conversations on a wide range of topics, from general knowledge to specific domains. It can understand user queries and respond in a relevant and informative manner.

## Requirements

- Python 3.x
- spaCy (Install using: `pip install spacy`)
- spaCy English language model (Install using: `python -m spacy download en_core_web_sm`)

## Usage

1. Clone the repository to your local machine

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the chatbot:

```bash
python chatbot.py
```

## Features

- Responds to greetings and basic conversation starters.
- Handles 'who', 'what', 'where', and 'when' and many more questions with custom responses for specific topics.
- Able to identify named entities like cities and provide relevant information.

## Customization

You can extend the chatbot's functionality by adding more domain-specific logic and custom responses. Update the `get_response()` function in the `chatbot.py` script to handle additional topics or integrate external APIs for more comprehensive responses.

## Contributing

Contributions to the project are welcome! If you have any improvements, bug fixes, or new features to add, feel free to submit a pull request.

