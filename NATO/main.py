NATO_phonetic_dict = {'A': "Alfa",
                      "B": "Bravo",
                      "C": "Charlie",
                      "D": "Delta",
                      "E": "Echo",
                      "F": "Foxtrot",
                      "G": "Golf",
                      "H": "Hotel",
                      "I": "India",
                      "J": "Juliet",
                      "K": "Kilo",
                      "L": "Lima",
                      "M": "Mike",
                      "N": "November",
                      "O": "Oscar",
                      "P": "Papa",
                      "Q": "Quebec",
                      "R": "Romeo",
                      "S": "Sierra",
                      "T": "Tango",
                      "U": "Uniform",
                      "V": "Victor",
                      "W": "Whiskey",
                      "X": "X-ray",
                      "Y": "Yankee",
                      "Z": "Zulu"}


def generate_phonetic():
    word = input("Enter a word: ")
    try:
        NATO_phonetic_list = [NATO_phonetic_dict[letter.upper()]
                              for letter in word]
    except KeyError:
        print("Sorry Only Letters in Alphabets please....")
        generate_phonetic()
    else:
        print(NATO_phonetic_list)


generate_phonetic()
