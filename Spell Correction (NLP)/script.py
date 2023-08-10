from textblob import TextBlob

def main():
    user_input = input("Enter a sentence: ")
    
    corrected_text = TextBlob(user_input).correct()
    
    print(f"Original: {user_input}")
    print(f"Corrected: {corrected_text}")

if __name__ == "__main__":
    main()
