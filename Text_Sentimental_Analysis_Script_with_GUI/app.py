from tkinter import *
from tkinter import messagebox
import Model


def search():
    word = enterWordEntry.get()

    text = word.strip()
    messagebox.showinfo("Input", " Input = "+text)
    model_object = Model.model()

    if word != "" and word != " " and word is not None:
        sentiment = model_object.get_sentimental_analysis(text)
        messagebox.showinfo("Result", sentiment)

    else:
        messagebox.showerror('Error', 'Invalid Input.Please double check it.')
        enterWordEntry.delete(0, END)


root = Tk()

root.geometry("1280x720+1000+30")

root.title("Text Sentimental Analysis")

root.resizable(False, False)

image = PhotoImage(file="./Text_Sentimental_Analysis_Script_with_GUI/images/background.png")
image_label = Label(root, image=image)
image_label.place(x=0, y=0)

enterWordLabel = Label(root, text='Enter Text for Analysis', font=('castellar', 15, 'bold'), fg='black')
enterWordLabel.place(x=180, y=20)

enterWordEntry = Entry(root, font=('arial', 20, 'bold'), bd=5, justify=CENTER)
enterWordEntry.place(x=100, y=70)

enterWordEntry.focus_set()

searchImage = PhotoImage(file='./Text_Sentimental_Analysis_Script_with_GUI/images/search.png')
searchButton = Button(root, image=searchImage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=search)
searchButton.place(x=450, y=50)

root.mainloop()
