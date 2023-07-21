import random
import quote


def generate_quotes():
    print("1. Inspirational")
    print("2. Motivational")
    print("3. Funny")
    print("4. Love")
    print("5. Life")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        search_term = "inspirational"
    elif choice == 2:
        search_term = "motivational"
    elif choice == 3:
        search_term = "funny"
    elif choice == 4:
        search_term = "love"
    elif choice == 5:
        search_term = "life"
    else:
        print("Invalid choice!")
        return
    quotes = quote.quote(search_term)
    num = int(input("Enter the No. of quotes to generate: "))
    for i in range(num):
        print(i+1, ".", random.choice(quotes)['quote'])


generate_quotes()
