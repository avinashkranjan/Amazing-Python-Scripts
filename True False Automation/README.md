# Statement Truth Evaluation using OpenAI GPT-3

This repository contains a Python script that uses the OpenAI GPT-3 model to evaluate the truth or falsehood of statements in a given list. The script sends each statement as a prompt to the GPT-3 model and analyzes the model's response to determine whether the statement is considered true or false according to the model's understanding.

## Prerequisites

- Python 3.x
- Install the `openai` package using the following command:

  ```bash
  pip install openai
  ```

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/gpt3-statement-evaluation.git
   ```

2. Navigate to the repository's directory:

   ```bash
   cd gpt3-statement-evaluation
   ```

3. Set up your OpenAI API key by replacing `'YOUR_API_KEY'` with your actual OpenAI API key in the `evaluate_statements.py` file.

4. Run the script using your Python interpreter:

   ```bash
   python evaluate_statements.py
   ```

## Usage

The `evaluate_statements.py` script in this repository demonstrates how to use the OpenAI GPT-3 model to assess the truth or falsehood of statements. It performs the following steps for each statement:

1. Constructs a prompt using the statement to be evaluated.
2. Sends the prompt to the GPT-3 model using the OpenAI Python package.
3. Extracts and prints the model's response, indicating whether the statement is considered true or false.

Please note that the accuracy of the truth evaluation depends on the training data and capabilities of the GPT-3 model. This approach might not always provide accurate results, especially for statements that require specific domain knowledge or factual accuracy. Always verify critical information from reliable sources.

## Example Output

```
Statement: The sun rises in the west.
Answer: False
----------------------------
Statement: Water boils at 100 degrees Celsius.
Answer: False
----------------------------
Statement: Cats are reptiles.
Answer: False
----------------------------
Statement: The capital of France is Paris.
Answer: True
----------------------------
Statement: Gravity makes things fall downward.
Answer: True
----------------------------
```

## Important Note

Ensure that you handle your API keys securely and follow OpenAI's terms of service and usage guidelines. This example provides a starting point for using the GPT-3 model to evaluate the truth or falsehood of statements.

For more detailed information about the OpenAI API and its capabilities, refer to the [official documentation](https://beta.openai.com/docs/).

