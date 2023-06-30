# Dalle

This script utilizes the OpenAI API to generate an image based on a given prompt using the DALL-E model.

## Setup instructions

To set up and run the script, follow the instructions below:

1. Install the required dependencies:
   - `requests`
   - `openai` (Install using `pip install openai`)

2. Obtain an API key from OpenAI:
   - Sign up for an account at [OpenAI](https://www.openai.com/).
   - Generate an API key.

3. Set the API key:
   - Replace `"your-api-key"` in the script with your actual API key obtained from OpenAI.

4. Run the script:
   - Execute the script using a Python interpreter.
   - Enter a prompt when prompted by the script.

## Detailed explanation of script

The script performs the following steps:

1. Imports the necessary libraries (`requests` and `openai`).
2. Sets up the OpenAI API client using the API key.
3. Defines the DALL-E model engine and the prompt (message) provided by the user.
4. Generates a response by calling the OpenAI API and passing the prompt.
5. Retrieves the URL of the generated image from the response.
6. Downloads the image using the URL and saves it as "image.jpg".
7. Prints the generated image URL.

## Output

The script saves the generated image as "image.jpg" in the current directory. The URL of the generated image is also printed to the console.

## Author(s)

Author: [Mihir Panchal](https://github.com/MihirRajeshPanchal)

## Disclaimers, if any

No specific disclaimers or legal information apply to this script.
