import tkinter as tk
import random
import timeit

start_time = 0


def get_sentence():
    global sentence, sentence_length, sentence_words
    Reset()
    with open("./Typing-Speed-Test/sentences.txt", "r") as f:
        sentences = f.readlines()
        sentence = random.choice(sentences).rstrip()
        sentence_label.config(text=sentence)
        sentence_length = len(sentence)
        sentence_words = len(sentence.split())
        print(sentence_length)


def result():
    time_taken = round(timeit.default_timer() - start_time)
    typed_text = text.get()
    wpm = round((sentence_words/time_taken)*60)
    count = 0
    for index, char in enumerate(typed_text):
        if sentence[index] == char:
            count += 1
    accu = round((count/sentence_length)*100)

    Speed.config(text=f"Speed: {wpm} WPM")
    Accuracy.config(text=f"Accuracy: {accu}")
    Time.config(text=f"Time: {time_taken} sec")


def check(text):
    global start_time
    if start_time == 0 and len(text.get()) == 1:
        start_time = timeit.default_timer()
    elif len(text.get()) == sentence_length:
        typing_box.config(state=tk.DISABLED)
        result()


def Reset():
    global start_time
    typing_box.config(state=tk.NORMAL)
    typing_box.delete(0, tk.END)
    start_time = 0

    Speed.config(text=f"Speed: 00 WPM")
    Accuracy.config(text=f"Accuracy: 00")
    Time.config(text=f"Time: 0 sec")


window = tk.Tk()
window.geometry("900x600+300+100")
window.title("Typing Speed Test")
bg_color = "#00154D"
window.config(bg=bg_color)

tk.Label(window, text="Typing Speed Test", anchor=tk.CENTER, font=(
    "times new roman", 50, "bold"), bg=bg_color, fg="#F2BC90").pack(side=tk.TOP)

sentence_label = tk.Label(window, text="a set of words that is complete in itself, typically containing a subject and predicate, conveying a statement, question, exclamation, or command, and consisting of a main clause and sometimes one or more subordinate clauses.",
                          wraplength=700, anchor=tk.CENTER, font=("arial", 20, "bold"), bg=bg_color, fg="#ffffff", width=40, justify=tk.LEFT)
sentence_label.pack(pady=40)
text = tk.StringVar()
text.trace("w", lambda name, index, mode, text=text: check(text))
typing_box = tk.Entry(window, font=("arial", 20, "bold"),
                      width=40, textvariable=text)
typing_box.place(x=150, y=360)

reset_button = tk.Button(window, text="Reset", font=(
    "arial", 18, "bold"), width=12, command=Reset)
reset_button.place(x=120, y=450)
change_button = tk.Button(window, text="Change Text", font=(
    "arial", 18, "bold"), width=12, command=get_sentence)
change_button.place(x=360, y=450)
result_button = tk.Button(window, text="Result", font=(
    "arial", 18, "bold"), width=12, command=result)
result_button.place(x=600, y=450)

Speed = tk.Label(window, text="Speed: 00 WPM", font=(
    "arial", 15, "bold"), bg=bg_color, fg="#ffffff")
Speed.place(x=120, y=530)
Accuracy = tk.Label(window, text="Accuracy: 00", font=(
    "arial", 15, "bold"), bg=bg_color, fg="#ffffff")
Accuracy.place(x=380, y=530)
Time = tk.Label(window, text="Time: 0 sec", font=(
    "arial", 15, "bold"), bg=bg_color, fg="#ffffff")
Time.place(x=620, y=530)

get_sentence()
window.mainloop()
