import random

# List of inspirational quotes
inspirational_quotes = [
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "The only way to achieve the impossible is to believe it is possible. - Charles Kingsleigh",
    "The only thing standing between you and your goal is the story you keep telling yourself. - Jordan Belfort",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The best way to predict the future is to create it. - Peter Drucker",
    "The only thing standing between you and your goal is the story you keep telling yourself. - Jordan Belfort"
]


def generate_random_quote():
    return random.choice(inspirational_quotes)


if __name__ == "__main__":
    print("Welcome to the Random Inspirational Quote Generator!")
    print("Here's your quote for today:")
    print(generate_random_quote())
