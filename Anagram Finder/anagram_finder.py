from nltk.corpus import words
import nltk
nltk.download('words')


def find_anagrams(search_words, word_list):
    # Function to sort letters in a word and return it as a string
    def sort_word(word):
        return ''.join(sorted(word))

    # Create a dictionary to store anagrams
    anagrams = {}

    # Group words based on their sorted letter representations
    for w in word_list:
        sorted_word = sort_word(w)
        if sorted_word in anagrams:
            anagrams[sorted_word].append(w)
        else:
            anagrams[sorted_word] = [w]

    results = {}

    # Find anagrams for each search word
    for search_word in search_words:
        sorted_word = sort_word(search_word)
        if sorted_word in anagrams:
            results[search_word] = anagrams[sorted_word]
        else:
            results[search_word] = []

    return results


if __name__ == "__main__":
    # Retrieve the NLTK word list
    nltk_word_list = words.words()

    # Sample search words
    search_words = ["silent", "debit card", "funeral", "astronomer"]

    # Combine the NLTK word list with the existing word list
    word_list = [
        "listen", "silent", "enlist", "tinsel", "hello", "world", "python",
        "astronomer", "moonstarer", "debit card", "bad credit", "punishments", "nine thumps",
        "dormitory", "dirty room", "the eyes", "they see", "a gentleman", "elegant man",
        "funeral", "real fun", "slot machines", "cash lost in me", "eleven plus two", "twelve plus one"
    ] + nltk_word_list

    results = find_anagrams(search_words, word_list)

    for search_word, anagrams in results.items():
        if anagrams:
            print(f"Anagrams of '{search_word}': {', '.join(anagrams)}")
        else:
            print(f"No anagrams found for '{search_word}'.")
