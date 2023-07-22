def text_file_analyzer(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            # Count lines
            num_lines = content.count('\n') + 1

            # Count words
            words = content.split()
            num_words = len(words)

            # Count characters
            num_characters = len(content)

            return num_lines, num_words, num_characters
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0, 0, 0

if __name__ == "__main__":
    file_path = input("Enter the path of the text file: ")

    lines, words, characters = text_file_analyzer(file_path)
    print(f"Number of lines: {lines}")
    print(f"Number of words: {words}")
    print(f"Number of characters: {characters}")
