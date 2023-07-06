from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

# Creating Tkinter Scaffold
root = tk.Tk()
root.title('Langauge Translator')
root.geometry('530x330')
root.maxsize(530, 330)
root.minsize(530, 330)

# Function to translate using the translator package


def translate():
    language_1 = t1.get("1.0", "end-1c")
    cl = choose_langauge.get()

    if language_1 == '':
        messagebox.showerror('Language Translator', 'please fill the box')
    else:
        t2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(language_1, dest=cl)
        t2.insert('end', output.text)


# Function to clear the input fields
def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')


# SelectBox 1 for auto detected language
auto_detect_language = tk.StringVar()
auto_detect = ttk.Combobox(
    root,
    width=20,
    textvariable=auto_detect_language,
    state='readonly',
    font=('verdana', 10, 'bold'),
)

auto_detect['values'] = ('Auto Detect', )

auto_detect.place(x=30, y=70)
auto_detect.current(0)

# SelectBox 2 for selected language
language_selected = tk.StringVar()
choose_langauge = ttk.Combobox(root,
                               width=20,
                               textvariable=language_selected,
                               state='readonly',
                               font=('verdana', 10, 'bold'))

# List of available language options for translation
choose_langauge['values'] = (
    'Afrikaans',
    'Albanian',
    'Arabic',
    'Armenian',
    ' Azerbaijani',
    'Basque',
    'Belarusian',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    ' Catalan',
    'Cebuano',
    'Chichewa',
    'Chinese',
    'Corsican',
    'Croatian',
    ' Czech',
    'Danish',
    'Dutch',
    'English',
    'Esperanto',
    'Estonian',
    'Filipino',
    'Finnish',
    'French',
    'Frisian',
    'Galician',
    'Georgian',
    'German',
    'Greek',
    'Gujarati',
    'Haitian Creole',
    'Hausa',
    'Hawaiian',
    'Hebrew',
    'Hindi',
    'Hmong',
    'Hungarian',
    'Icelandic',
    'Igbo',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kannada',
    'Kazakh',
    'Khmer',
    'Kinyarwanda',
    'Korean',
    'Kurdish',
    'Kyrgyz',
    'Lao',
    'Latin',
    'Latvian',
    'Lithuanian',
    'Luxembourgish',
    'Macedonian',
    'Malagasy',
    'Malay',
    'Malayalam',
    'Maltese',
    'Maori',
    'Marathi',
    'Mongolian',
    'Myanmar',
    'Nepali',
    'Norwegian'
    'Odia',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Romanian',
    'Russian',
    'Samoan',
    'Scots Gaelic',
    'Serbian',
    'Sesotho',
    'Shona',
    'Sindhi',
    'Sinhala',
    'Slovak',
    'Slovenian',
    'Somali',
    'Spanish',
    'Sundanese',
    'Swahili',
    'Swedish',
    'Tajik',
    'Tamil',
    'Tatar',
    'Telugu',
    'Thai',
    'Turkish',
    'Turkmen',
    'Ukrainian',
    'Urdu',
    'Uyghur',
    'Uzbek',
    'Vietnamese',
    'Welsh',
    'Xhosa'
    'Yiddish',
    'Yoruba',
    'Zulu',
)

choose_langauge.place(x=290, y=70)
choose_langauge.current(0)

# To store Input Text
t1 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t1.place(x=10, y=100)

# To store translated Text
t2 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t2.place(x=260, y=100)

button = Button(root,
                text="Translate",
                relief=RIDGE,
                borderwidth=3,
                font=('verdana', 10, 'bold'),
                cursor="hand2",
                foreground='Green',
                command=translate)
button.place(x=150, y=280)

clear = Button(root,
               text="Clear",
               relief=RIDGE,
               borderwidth=3,
               font=('verdana', 10, 'bold'),
               cursor="hand2",
               foreground='Red',
               command=clear)
clear.place(x=280, y=280)

root.mainloop()
