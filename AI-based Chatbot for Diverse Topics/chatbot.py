import spacy

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Function to get the response from the chatbot


def get_response(query):
    # Process the user query
    doc = nlp(query)

    # Extract important information from the user query (e.g., named entities)
    named_entities = [ent.text for ent in doc.ents]

    # Example: Detecting greetings and responding accordingly
    greetings = ["hello", "hi", "hey", "howdy"]
    if any(greet in query.lower() for greet in greetings):
        return "Hello! How can I assist you today?"

    # Example: Handling 'who' questions
    if "who" in query.lower() and "is" in query.lower():
        # Replace 'who is' with an empty string to get the subject of the question
        subject = query.lower().replace("who is", "").strip()
        if subject:
            # Custom logic for specific topics
            if subject == "python":
                return "Python is a popular programming language known for its simplicity and versatility."
            elif subject == "ai":
                return "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that can perform tasks that typically require human intelligence."
            elif subject == "elon musk":
                return "Elon Musk is a visionary entrepreneur and CEO of companies like SpaceX and Tesla, known for his ambitious goals in space exploration and sustainable energy."

    # Example: Handling 'what' questions
    if "what" in query.lower() and "is" in query.lower():
        # Replace 'what is' with an empty string to get the subject of the question
        subject = query.lower().replace("what is", "").strip()
        if subject:
            # Custom logic for specific topics
            if subject == "python":
                return "Python is a popular programming language known for its simplicity and versatility."
            elif subject == "ai":
                return "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that can perform tasks that typically require human intelligence."
            elif subject == "elon musk":
                return "Elon Musk is a visionary entrepreneur and CEO of companies like SpaceX and Tesla, known for his ambitious goals in space exploration and sustainable energy."
            elif subject == "global warming":
                return "Global warming is the long-term increase in Earth's average surface temperature due to human activities like burning fossil fuels and deforestation."

    # Example: Handling 'where' questions
    if "where" in query.lower():
        # Custom logic for specific locations
        if "city" in named_entities:
            city = named_entities[named_entities.index("city") + 1]
            if city == "new york":
                return "New York City, often called NYC, is a major city in the United States known for its culture, arts, and diverse population."
            elif city == "paris":
                return "Paris is the capital city of France and is famous for its art, history, and iconic landmarks like the Eiffel Tower."

    # Example: Handling 'when' questions
    if "when" in query.lower():
        # Custom logic for specific events
        if "world war 2" in query.lower():
            return "World War II took place from 1939 to 1945, involving many countries and causing significant global impact."

    # If no specific response is generated, provide a default response
    return "I'm sorry, but I'm not sure how to help with that."


# Main chat loop
print("Chatbot: Hello! How can I assist you today? Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
