from PyDictionary import PyDictionary


def get_meaning(word):
    dictionary = PyDictionary()
    return dictionary.meaning(word)


if __name__ == "__main__":
    word = input("Please enter the word: ")
    print("Word Meaning : " + str(get_meaning(word)))