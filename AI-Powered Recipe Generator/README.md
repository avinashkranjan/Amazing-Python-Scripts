# AI-Powered Recipe Generator

## Description
AI-Powered Recipe Generator is a Python script that uses natural language processing (NLP) to analyze a database of recipes. Users can input a list of ingredients they have, and the script generates unique recipes based on their preferences and available ingredients. The generated recipes come with instructions and can be customized based on dietary preferences.

## Features
- Generate unique recipes based on user-provided ingredients and dietary preferences.
- Provide instructions for each generated recipe.
- Suggest ingredient substitutions if some ingredients are missing.
- Fetch nutritional information of the generated recipe (work in progress).
- Allow users to rate the generated recipe for feedback and improvement.
- Suggest similar recipes for more options.

## Requirements
- Python 3.6+
- nltk library (Natural Language Toolkit)

## Installation
1. Clone the repository or download the script (`recipe_generator.py`) to your local machine.
2. Install the required libraries using pip:

```bash
pip install nltk
```

## Usage
1. Run the script using Python:

```bash
python recipe_generator.py
```

2. Follow the on-screen prompts to enter your list of ingredients and dietary preferences.
3. The script will generate a unique recipe based on your inputs, along with instructions and a link to the original source.
4. Optionally, the script will ask for ingredient substitutions and user ratings.
