
```markdown
# OpenAI Chatbot Example

This repository contains examples of using the OpenAI GPT-3 model to create a chatbot that can hold conversations with users.

## Prerequisites

- OpenAI Python Package (`openai`)
- `requests` library (for Method 2)

You can install the required libraries using the following commands:

```bash
pip install openai requests
```

## Method 1 - Using OpenAI Python Package

This method demonstrates how to use the OpenAI Python package to create a chatbot using the `gpt-3.5-turbo` model.

The code provided in the repository (`method_1_openai_package.py`) includes:

- Setting up the OpenAI API key.
- Initiating a conversation with a system message.
- Taking user inputs and generating replies using the chatbot.
- Displaying the chat history.

## Method 2 - Using API Endpoint

This method demonstrates how to interact with the OpenAI API directly using HTTP requests.

The code provided in the repository (`method_2_api_endpoint.py`) includes:

- Defining the API endpoint URL.
- Creating a payload with user inputs and other parameters.
- Sending a POST request to the API endpoint.
- Extracting and displaying the generated response.

## Usage

1. Set up your OpenAI API key by replacing `'sk-'` in the code with your actual API key.

2. Choose the method you want to use (Method 1 or Method 2).

3. Run the selected script using a Python interpreter:

   ```bash
   python method_1_openai_package.py
   ```
   or
   ```bash
   python method_2_api_endpoint.py
   ```

4. Observe the interaction with the chatbot and the generated responses.

## Notes

- Make sure to review the OpenAI API documentation for more information on available models, parameters, and best practices.

