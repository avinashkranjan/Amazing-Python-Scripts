import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# List of statements to evaluate
statements = [
    "The sun rises in the west.",
    "Water boils at 100 degrees Celsius.",
    "Cats are reptiles.",
    "The capital of France is Paris.",
    "Gravity makes things fall downward.",
]

# Evaluate each statement using the GPT-3 model
for statement in statements:
    prompt = f"Check if the following statement is true or false:\nStatement: {statement}\nAnswer:"

    response = openai.Completion.create(
        engine="davinci",  # Use the appropriate engine
        prompt=prompt,
        max_tokens=1,      # Limit the response to 1 token
    )

    answer = response.choices[0].text.strip()

    print(f"Statement: {statement}")
    print(f"Answer: {answer}")
    print("----------------------------")
