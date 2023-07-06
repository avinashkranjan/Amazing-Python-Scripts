import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import urllib.request as request
import urllib.parse
import json


class quiz(tk.Tk):
    def __init__(self):

        # welcome window
        super().__init__()
        self.s = ttk.Style()

        # App title
        self.title("Quiz Time")

        # setting dimension for window and placement on user's screen
        self.geometry("900x300+200+200")

        # Welcome message
        self.label_1 = tk.Label(
            self, text="Welcome to the Quiz!", width=30, font=("bold", 15))
        self.label_1.pack(padx=10, pady=30)

        # Start Quiz button
        self.btn_1 = ttk.Button(self, text="Start Quiz", command=lambda: self.label_1.destroy(
        ) or self.btn_1.destroy() or self.choices(),)
        self.btn_1.pack()

    def choices(self):
        # user's category and difficulty level preference are taken here

        # initializing the score array to store the user's score.
        self.score = [0]*10
        # play again gets redirected to this window

        # label for category preference
        self.label_1 = tk.Label(
            self, text="Choose a Category", width=20, font=("bold", 10))
        # widget is placed in fixed coordinates using 'place'
        self.label_1.place(x=250, y=50)

        # combobox/drop down menu for category preference
        self.category_choice = ttk.Combobox(self, values=["Random Category", "General Knowledge", "Books", "Movies", "Music", "Television", "Video Games",
                                                          "Science and Nature", "Computers", "Mathematics", "Mythology", "Sports",
                                                          "Geography", "History", "Animals", "Celebrities", "Anime and Manga",
                                                          "Cartoons and Animations", "Comics"])

        # widget is placed in fixed coordinates
        self.category_choice.place(x=480, y=50)

        # sets the default choice that's initially displayed
        self.category_choice.current(0)

        # label for difficulty preference
        self.label_2 = tk.Label(
            self, text="Choose a Difficulty Level", width=20, font=("bold", 10))
        # widget is placed in fixed coordinates
        self.label_2.place(x=265, y=100)

        # combobox/drop down menu for difficulty preference
        self.difficulty_choice = ttk.Combobox(
            self, values=["Easy", "Medium", "Hard"])
        # widget is placed in fixed coordinates
        self.difficulty_choice.place(x=480, y=100)

        # sets the default choice that's initially displayed
        self.difficulty_choice.current(1)

        # button to go to next window
        self.btn_1 = ttk.Button(
            self, text="Go", width=10, command=lambda: destroy_widgets() or self.getQuestions())
        # widget is placed in fixed coordinates
        self.btn_1.place(x=450, y=160, anchor='center')

        def destroy_widgets():
            # user's category choice and difficulty choice are saved
            self.category = self.category_choice.get()
            self.difficulty = self.difficulty_choice.get()

            # all widgets from this window are destroyed
            self.btn_1.destroy()
            self.category_choice.destroy()
            self.difficulty_choice.destroy()
            self.label_1.destroy()
            self.label_2.destroy()

    def getQuestions(self):
        # Chosen Category and Difficulty level are displayed here for confirmation
        # The user is also allowed to go back and change their preference

        # function call to the questions api to retrieve questions
        self.questionsapi(self.category, self.difficulty)

        # displays the category chosen by the user
        self.label_1 = tk.Label(
            self, text="Category: " + self.category, font=('italics', 13))
        # widget is placed in fixed coordinates and centered
        self.label_1.place(x=450, y=50, anchor="center")

        # displays the difficulty level chosen by the user
        self.label_2 = tk.Label(
            self, text="Difficulty: "+self.difficulty, font=('italics', 12))
        # widget is placed in fixed coordinates and centered
        self.label_2.place(x=450, y=100, anchor="center")

        # button redirects the user back to previous window to change their preference
        self.btn_1 = ttk.Button(
            self, text="Change Choice", command=lambda: destroy_widgets() or self.choices(), width=20)
        # widget is placed in fixed coordinates
        self.btn_1.place(x=400, y=150, anchor="e")

        # button to go to next window, to start playing
        self.btn_2 = ttk.Button(self, text="Next", command=lambda: destroy_widgets(
        ) or self.printQuestion(0), width=20)
        self.btn_2.place(x=500, y=150, anchor="w")

        def destroy_widgets():
            # destroy all widgets from this window
            self.btn_1.destroy()
            self.btn_2.destroy()
            self.label_1.destroy()
            self.label_2.destroy()

    def printQuestion(self, index):
        # function is recursively called to print each question
        # there are a total of 10 questions

        if index < 10:
            # label to display question number
            self.label_1 = ttk.Label(
                self, text="Question "+str(index+1), font=('bold', 11))
            self.label_1.place(x=450, y=30, anchor="center")

            # a label to display the question text
            # wraplength used to make sure the text doesn't flow out of the screen
            self.label_2 = tk.Label(self, text=self.questions[index], font=(
                'bold', 11), wraplength=700, justify=tk.CENTER)
            self.label_2.place(x=450, y=70, anchor="center")

            # button to display option 1
            self.option1 = tk.Button(self, text=self.options[index][0], wraplength=200, justify=tk.CENTER, borderwidth=0.5, relief=tk.SOLID, activebackground='#ddd',
                                     command=lambda: destroy_widgets() or self.printQuestion(index+1) or self.scoreUpdater(index, 0), width=30)
            self.option1.place(x=250, y=130, anchor="center")

            # button to display option 2
            self.option2 = tk.Button(self, text=self.options[index][1], wraplength=200, justify=tk.CENTER, borderwidth=0.5, relief=tk.SOLID, activebackground='#ddd',
                                     command=lambda: destroy_widgets() or self.printQuestion(index+1) or self.scoreUpdater(index, 1), width=30)
            self.option2.place(x=650, y=130, anchor="center")

            # button to display option 3
            self.option3 = tk.Button(self, text=self.options[index][2], wraplength=200, justify=tk.CENTER, borderwidth=0.5, relief=tk.SOLID, activebackground='#ddd',
                                     command=lambda: destroy_widgets() or self.printQuestion(index+1) or self.scoreUpdater(index, 2), width=30)
            self.option3.place(x=250, y=180, anchor="center")

            # button to display option 4
            self.option4 = tk.Button(self, text=self.options[index][3], wraplength=200, justify=tk.CENTER, borderwidth=0.5, relief=tk.SOLID, activebackground='#ddd',
                                     command=lambda: destroy_widgets() or self.printQuestion(index+1) or self.scoreUpdater(index, 3), width=30)
            self.option4.place(x=650, y=180, anchor="center")

            if index > 0:
                # button to navigate to previous question
                # appears from the second question onwards
                self.btn_2 = ttk.Button(self, text="Go to Previous Question",
                                        command=lambda: destroy_widgets() or self.printQuestion(index-1))
                self.btn_2.place(x=70, y=220)

        else:
            # once 10 questions have been printed we move onto here
            # a buffer window before we print the score

            # a label to notify the user that the quiz is done
            self.label_1 = tk.Label(
                self, text="Great Work. Hope you had fun!", font=("bold", 12))
            # widget is placed in fixed coordinates
            self.label_1.place(x=450, y=70, anchor="center")

            # button to navigate to the next page to view score
            self.btn_1 = ttk.Button(self, text="Get Score", command=lambda: self.label_1.destroy(
            ) or self.btn_1.destroy() or self.getScore(), width=15)
            # widget is placed in fixed coordinates
            self.btn_1.place(x=450, y=130, anchor="center")

        def destroy_widgets():
            # destroy all widgets from this window
            self.label_1.destroy()
            self.label_2.destroy()
            self.option1.destroy()
            self.option2.destroy()
            self.option3.destroy()
            self.option4.destroy()
            if index > 0:
                self.btn_2.destroy()

    def scoreUpdater(self, question, option):
        # function is called every time the user answers a question

        # the users answer is compared to the right answer to the question
        # the score array is updated accordingly
        if self.options[question][option] == self.correct_answers[question]:
            self.score[question] = 1
        else:
            self.score[question] = 0

    def getScore(self):
        # window to display score

        # save the user's score as an integer - previously an array
        # count() is used to count the number of correctly answered questions
        self.score = self.score.count(1)

        # following if conditions are targeted for a certain score range
        if self.score <= 4:
            self.label_1 = tk.Label(
                self, text="Better Luck Next Time!", font=("bold", 12))
            self.label_2 = tk.Label(
                self, text="Your Score is: " + str(self.score), font=("bold", 12))

        elif self.score == 5:
            self.label_1 = tk.Label(self, text="Not Bad!", font=("bold", 12))
            self.label_2 = tk.Label(
                self, text="Your Score is: " + str(self.score), font=("bold", 12))

        elif self.score < 10 and self.score > 5:
            self.label_1 = tk.Label(self, text="Good Job!", font=("bold", 12))
            self.label_2 = tk.Label(
                self, text="Your Score is: " + str(self.score), font=("bold", 12))

        elif self.score == 10:
            self.label_1 = tk.Label(self, text="Awesome!", font=("bold", 12))
            self.label_2 = tk.Label(
                self, text="Your Score is: " + str(self.score), font=("bold", 12))

        # labels are assigned definite coordinates on the window
        self.label_1.place(x=450, y=70, anchor="center")
        self.label_2.place(x=450, y=120, anchor="center")

        # Button to navigate the user to the quiz preferences window to play again
        self.btn_1 = ttk.Button(
            self, text="Play Again", command=lambda: destroy_widgets() or self.choices())
        self.btn_1.place(x=400, y=170, anchor="e")

        # button to quit
        self.btn_2 = ttk.Button(
            self, text="Quit", command=lambda: destroy_widgets() or self.destroy())
        self.btn_2.place(x=500, y=170, anchor="w")

        def destroy_widgets():
            # destroys all widgets from this window
            self.label_1.destroy()
            self.label_2.destroy()
            self.btn_1.destroy()
            self.btn_2.destroy()

    def questionsapi(self, category, difficulty):
        # questions for the quiz are retrieved using an api
        # api link https://opentdb.com/api_config.php

        # category to ID mapping is made here
        # the full list of category to id mapping can be retrieved here -> https://opentdb.com/api_category.php
        categoryMappings = {"General Knowledge": 9, "Books": 10, "Movies": 11, "Music": 12, "Television": 14,
                            "Video Games": 15, "Science and Nature": 17, "Computers": 18, "Mathematics": 19, "Mythology": 20, "Sports": 21,
                            "Geography": 22, "History": 23, "Animals": 27, "Celebrities": 26, "Anime and Manga": 31,
                            "Cartoons and Animations": 32, "Comics": 29}

        # random category is generated in the below if condition
        if category == "Random Category":
            self.category = random.choice(list(categoryMappings.keys()))
        # category is obtained through the category mappings
        category_id = categoryMappings[self.category]

        # url to make api call from category and difficulty preferences is generated
        url = 'https://opentdb.com/api.php?amount=10&category=' + \
            str(category_id) + '&difficulty=' + self.difficulty.lower() + \
            '&type=multiple&encode=url3986'

        # json response is saved using the request module of Python
        with request.urlopen(url) as response:
            source = response.read()
            data = json.loads(source)

        # questions, incorrect answers and the correct answers are extracted fromt he response data
        # urllib.parse is used to decode the response data (%20..etc)
        self.questions = [urllib.parse.unquote(
            q['question'], encoding='utf-8', errors='replace') for q in data['results']]
        self.correct_answers = [urllib.parse.unquote(
            q['correct_answer'], encoding='utf-8', errors='replace') for q in data['results']]

        incorrect_options = [q['incorrect_answers'] for q in data['results']]

        # loops through each question's incorrect answers and appends the correct answer to it
        # all 4 options are shuffled usind 'random' module's shuffle
        for i in range(len(incorrect_options)):
            for j in range(len(incorrect_options[i])):
                incorrect_options[i][j] = urllib.parse.unquote(
                    incorrect_options[i][j], encoding='utf-8', errors='replace')
            incorrect_options[i].append(self.correct_answers[i])
            random.shuffle(incorrect_options[i])

        self.options = []
        # the
        for i in range(len(incorrect_options)):
            self.options.append(incorrect_options[i])


if __name__ == "__main__":
    quiz().mainloop()
