import random
import tkinter as tk
from tkinter import messagebox


def choose_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    return random.choice(words)


class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.word = choose_word()
        self.guessed_letters = []
        self.attempts = 0

        self.label_word = tk.Label(master, text=self.display_word())
        self.label_word.pack()

        self.label_attempts = tk.Label(master, text="Attempts left: 6")
        self.label_attempts.pack()

        self.entry_guess = tk.Entry(master)
        self.entry_guess.pack()

        self.button_guess = tk.Button(
            master, text="Guess", command=self.make_guess)
        self.button_guess.pack()

    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter
            else:
                displayed_word += "_ "
        return displayed_word

    def make_guess(self):
        guess = self.entry_guess.get().lower()

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning(
                "Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed",
                                "You've already guessed this letter.")
            return

        self.guessed_letters.append(guess)

        if guess not in self.word:
            self.attempts += 1
            self.label_attempts.config(
                text=f"Attempts left: {6 - self.attempts}")

        self.label_word.config(text=self.display_word())

        if "_" not in self.display_word():
            messagebox.showinfo("Congratulations!",
                                f"You guessed the word: {self.word}")
            self.master.destroy()

        if self.attempts >= 6:
            messagebox.showinfo(
                "Game Over", f"Out of attempts! The word was: {self.word}")
            self.master.destroy()


def main():
    root = tk.Tk()
    root.title("Hangman Game")
    game = HangmanGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
