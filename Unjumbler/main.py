# Define the jumbled word
jumbled = input("Enter a word to jumble: ")

def find_unjumbled_words(jumbled_word):
    # Open the file containing English words
    with open('english_words_list[HEAVY].txt', 'r') as file:
        # Initialize a list to store unjumbled words
        unjumbled_words = []

        # Iterate through each line in the file
        for line in file:
            # Remove trailing whitespace and store the word in 'word' variable
            word = line.strip()

            # Check if the length of the word matches the jumbled word or use 'True' to match any length
            if len(word) == len(jumbled_word) or True:
                # Check if the sets of characters in the word and jumbled word are the same
                if set(word) == set(jumbled_word):
                    # If the condition is met, add the word to the 'unjumbled_words' list
                    unjumbled_words.append(word)

    # Close the file
    file.close()

    # Return the list of unjumbled words
    return unjumbled_words

if __name__ == "__main__":
    # Call the function with the jumbled word and print the results
    unjumbled_words = find_unjumbled_words(jumbled)
    print(unjumbled_words)
