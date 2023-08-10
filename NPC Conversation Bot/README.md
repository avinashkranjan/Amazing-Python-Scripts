# NPC Conversation Bot

Welcome to the NPC Conversation Bot! This Python script simulates an NPC (non-player character) that engages in text-based conversations with the user. The bot responds to various inputs and can perform simple tasks like weather inquiries and news updates.

## Features

- Basic greeting and conversation initiation
- Responds to user inputs and prompts
- Provides weather information for a specified city (hardcoded response)
- Fetches news headlines based on a specified topic (hardcoded response)
- Offers general chat and responds to a range of inputs

## Getting Started

1. **Prerequisites**: Ensure you have Python 3.x installed on your system.

2. **Installation**: Clone this repository to your local machine.

3. **Usage**: Open a terminal window and navigate to the directory containing the cloned repository.

```shell
cd npc-conversation-bot
```

Run the script by executing the following command:

```shell
python npc_bot.py
```

4. **Conversing with the Bot**: Once the script is running, you can engage in conversations with the NPC Bot. Type your messages and press Enter to see the bot's responses.

5. **Exiting**: To exit the conversation and close the bot, type `exit` and press Enter.

## Customization

- You can customize the conversation patterns and responses in the `conversation_patterns` list within the `npc_bot.py` script.
- To add more features, expand the bot's capabilities, or integrate external APIs, you can modify the `npc_conversation` function accordingly.

## Dependencies

- The script uses the `nltk` library for chat functionality. You can install it using:

```shell
pip install nltk
```

## Contribution

Feel free to contribute to this project by submitting pull requests or suggesting improvements.
