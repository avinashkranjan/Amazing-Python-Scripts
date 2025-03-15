from chatterbot import ChatBot
import os
import re
# naming the ChatBot calculator
# using mathematical evaluation logic
# the calculator AI will not learn with the user input
Bot = ChatBot(name='Calculator',
              read_only=True,
              logic_adapters=["chatterbot.logic.MathematicalEvaluation"],
              storage_adapter="chatterbot.storage.SQLStorageAdapter")
#spacing issue with between value and the arthmetic operator solved by adding the formatted input
def format_expression(expression):
    return re.sub(r'([\+\-\*/%\^])', r' \1 ', expression)
    
# clear the screen and start the calculator
os.system('cls' if os.name == 'nt' else 'clear')
print("Hello, I am a calculator. How may I help you?")
while (True):
    # take the input from the user
    user_input = input("me: ")
    
    # check if the user has typed quit to exit the prgram
    if user_input.lower() == 'quit':
        print("Exiting")
        break
    formatted_input = format_expression(user_input)

    # otherwise, evaluate the user input
    # print invalid input if the AI is unable to comprehend the input
    try:
        response = Bot.get_response(formatted_input)
        print("Calculator:", response)
    except:
        print("Calculator: Please enter valid input.")
