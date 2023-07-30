from PyDictionary import PyDictionary


def main():
    """Main entry point of the Scrabble game."""
    print('*' * 10 + "Welcome to the Scrabble game" + '*' * 10)
    print("Let's start playing!!\n")
    score_board = {}
    for i in range(player_count()):
        player = input(f"Player {i+1}: ")
        score_board[player] = 0
    print('*' * 40)
    print(winner(get_input(score_board)).center(40, " "))
    print('*' * 40)
    print("Thank you for your time. Have a Nice day!")


def valid(word):
    """
    Checks if a word is valid by checking its meaning using PyDictionary.
    Args:
        word (str): The word to be validated.
    Returns:
        bool: True if the word is valid, False otherwise.
    """
    dictionary = PyDictionary()
    return bool(dictionary.meaning(word))


def compute_score(word):
    """
    Computes the score for a given word based on a score list.
    Args:
        word (str): The word for which the score needs to be computed.
    Returns:
        int: The computed score for the word.
    Raises:
        ValueError: If the word is invalid or contains non-alphabetic characters.
    """
    score_list = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
                'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
                'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
                'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    score = 0
    if word.isalpha():
        if valid(word):
            for char in word:
                score += score_list[char.lower()]
            return score
        raise ValueError("Invalid word")
    raise ValueError("Word should only contain alphabetic characters")


def player_count():
    """
    Prompts the user to input the number of players for the game.
    Returns:
        int: The number of players.
    Raises:
        ValueError: If the user inputs a non-positive number.
    """
    while True:
        try:
            count = int(input("How many players? "))
            if count < 1:
                raise ValueError("Please enter a positive number")
            return count
        except ValueError as e:
            print(str(e))


def get_input(score_board):
    """
    Retrieves the word input from each player and updates their scores.
    Args:
        score_board (dict): The dictionary storing the scores of each player.
    Returns:
        dict: The updated score board.
    """
    while True:
        for player in score_board:
            while True:
                try:
                    word = input(f"{player} | Type a word: ")
                    score_board[player] += compute_score(word)
                except ValueError as e:
                    print(str(e))
                else:
                    break

        if input("If exit, type Y: ").lower() == "y":
            print('*' * 40)
            break
        continue
    return score_board


def winner(score_board):
    """
    Args:
        score_board (dict): The dictionary storing the scores of each player.
    Returns:
        str: The winner(s) message.
    Raises:
        IndexError: If there are no players in the score board.
    """
    sorted_scores = sorted(score_board.items(),
                           key=lambda x: x[1], reverse=True)
    if len(sorted_scores) > 0:
        max_score = sorted_scores[0][1]
        winners = [player for player,
                   score in sorted_scores if score == max_score]
        if len(winners) > 1:
            return f"It's a tie. The winners are {', '.join(winners)}!!"
        return f"The winner is {winners[0]}!"
    return "No players found. Game over!"


if __name__ == "__main__":
    main()
