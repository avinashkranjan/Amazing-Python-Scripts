# import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.ttk import *
from markdown2 import Markdown
from tkhtmlview import HTMLLabel

# Function to display markdown on button click


def onKeyUp():
    markdown = Markdown()
    markdownText = markdown_editor.get("1.0", END)
    html = markdown.convert(markdownText)
    result.set_html(html)


# Creating tkinter window
window = Tk()
window.title('Markdown viewer')
window.geometry('1200x1000')
window.configure(bg='white')

# Styling font and button
myfont = font.Font(family="Helvetica", size=14)
style = Style()
style.configure('TButton', font=('calibri', 20, 'bold'),
                foreground='Blue')

# Placing widgets into Tkinter window
submit_btn = Button(text="View Markdown", command=onKeyUp, style='TButton')
submit_btn.pack(ipadx=30, ipady=6)

markdown_editor = Text(width="1", insertborderwidth=2,
                       selectborderwidth=2)
markdown_editor.insert(END, '# Add Markdown here')
markdown_editor.pack(fill=BOTH, expand=1, side=LEFT, padx=10, pady=10)
markdown_editor.configure(font=myfont)

result = HTMLLabel(width="1", html="<h1>Markdown Viewer</h1>")
result.pack(fill=BOTH, expand=1, side=RIGHT, padx=10, pady=10)


window.mainloop()
