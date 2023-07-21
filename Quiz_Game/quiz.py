
# List of questions for quiz

questions = [
    'who is the developer of Python Language',
    'when did india gets independence',
    'what is the Indian currency',
    'Who is World first cloned human baby',
    'who is the founder of Hinduism'
]

# list of answers for above questions

answers = [
    'Guido Van',
    '1947',
    'INR',
    'Eve',
    'No Specific'
]

#  List of options for above questions

options = [
    ['Dennis Ritchie', 'Alan Frank', 'Guido Van', 'Albert'],
    ['1947', '1995', '1950', '1957'],
    ['DOLLARS', 'YEN', 'EURO', 'INR'],
    ['Erik', 'Maria', 'Sophie', 'Eve'],
    ['Mahavira Swami', 'Mahatma Buddha', 'No Specific', 'Prophet Mohammed']
]

# Quiz Game | Designed by Ishita

#  Defining function for game playing


def play_game(username, questions, answers, options):
    print("Hello,", username, "welcome to the QUIZ game")
    print("All the Best for the Game :>")
    score = 0
    for i in range(5):
        current_questions = questions[i]
        # print(questions[i])
        correct_answer = answers[i]
        current_question_options = options[i]
        print("Questions:", current_questions)
        for index, each_options in enumerate(current_question_options):
            print(index+1, ") ", each_options, sep='')
        user_answer_index = int(input("Please enter your choice(1,2,3,4): "))
        user_answer = current_question_options[user_answer_index-1]
        if user_answer == correct_answer:
            print("correct answer")
            score = score + 100
        else:
            print("wrong answer")
            break
    print("Your final score is", score)
    return username, score

# Defining function for viewing the score


def view_scores(names_and_scores):
    for name, score in names_and_scores.items():
        print(name, "has scored", score)

# Defining the function for start of the score


def quiz(questions, answers, options):
    names_and_scores = {}
    while True:
        print("Welcome to the quiz game")
        print("1) Play\n2) View Scores\n3) Exit")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            username = (input("Please enter your name: "))
            username, score = play_game(username, questions, answers, options)
            names_and_scores[username] = score
        elif choice == 2:
            view_scores(names_and_scores)
        elif choice == 3:
            break
        else:
            print("Your choice is not correct")

#  Program execution starts from here


quiz(questions, answers, options)
