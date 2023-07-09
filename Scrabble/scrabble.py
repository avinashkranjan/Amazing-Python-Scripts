from PyDictionary import PyDictionary

def main():
    print("\n" + '*'*10 + "Welcome to the Scrabble game" + '*'*10 + "\n" + "Let's start playing!!\n")
    score_board = {}
    for i in range(player_count()):
        player = input(f"Player {i+1}: ")
        score_board[player] = 0
    print('*'*40 + "\n")
    print(winner(get_input(score_board)).center(40, " ") +"\n")
    print('*'*40 + "\n"+"Thank you for your time. Have a Nice day!")

def valid(word):
    if PyDictionary().meaning(word, True) == None :
        return False
    else:
        return True

def compute_score(word):
    score_list = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3,
                  'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}
    score = 0
    if word.isalpha():
        if valid(word):
            for i in word:
                score += score_list[i.lower()]
            return score
        else:
            raise NameError
    else:
        raise ValueError

def player_count():
    while True:
        try:
            count = int(input("How many players? "))
        except ValueError:
            print("Please type a number in integer format.")
            continue
        else:
            return count
            break

def get_input(score_board):
    while True:
        for player in score_board:
            while True:
                try:
                    word = input(f"{player} | Type a word: ")
                    score_board[player] += compute_score(word)
                except BaseException:
                    print("Please type a valid word.")
                    continue
                else:
                    break

        if input("If exit, type Y: ") == "Y":
            print('*'*40 + "\n")
            break
        else:
            continue
    return score_board

def winner(score_board):
    sorted_scores = sorted(score_board.items(), key=lambda x: x[1], reverse= True)
    max = sorted_scores[0][1]
    winners = [sorted_scores[0][0]]
    for i in sorted_scores[1:]:
        if i[1] == max:
            winners.append(i[0])
    if len(winners) > 1:
        return f"It's a tie. The winners are {', '.join(winners)}!!"
    else:
        return f"The winner is {winners[0]}!"

if __name__ == "__main__":
    main()