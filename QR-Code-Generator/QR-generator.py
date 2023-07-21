from tkinter import *
from tkinter import messagebox
import os
import pyqrcode
import smtplib
import imghdr
from email.message import EmailMessage


my_mail = "ENTER YOUR EMAIL ID"
password = "SET PASSWORD"
# create a GUI window with Tkinter
window = Tk()
window.title("QR Code Generator APP")
global email_add


# a function to generate all widgets
def generate():
    if len(Subject.get()) != 0:
        global qr, photo
        qr = pyqrcode.create(Subject.get())
        photo = BitmapImage(data=qr.xbm(scale=8))
    else:
        messagebox.showerror("Error", "Enter subject first")
    try:
        showcode()
    except:
        pass


# a function to show the qr code on the screen
def showcode():
    imageLabel.config(image=photo)
    subLabel.config(text="QR of " + Subject.get())


# A function to save the qr code as a png file
def save():
    dir = os.getcwd()
    if not os.path.exists(os.getcwd()):
        os.makedirs(dir)
    try:
        if len(name.get()) != 0:
            qr.png(os.path.join(dir, name.get() + ".png"), scale=8)
            messagebox.showinfo("Status", "QR code saved successfully")
        else:
            messagebox.showerror("Error", "Enter file name first")
    except:
        messagebox.showerror("Error", "Generate the QR code first")


def send():
    try:
        if len(mail.get()) != 0 and os.path.exists(name.get()+".png"):
            newMessage = EmailMessage()
            newMessage['Subject'] = "QR CODE IS READY!!"
            newMessage['From'] = my_mail
            newMessage['To'] = mail.get()
            with open(f'{name.get()}.png', 'rb') as f:
                image_data = f.read()
                image_type = imghdr.what(f.name)
                image_name = f.name
            newMessage.add_attachment(
                image_data, maintype='image', subtype=image_type, filename=image_name)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(my_mail, password)
                smtp.send_message(newMessage)

            messagebox.showinfo("Status", "Mail has been sent successfully")
        else:
            messagebox.showerror(
                "Error", "Invalid Email or QR Code not generated")
    except:
        messagebox.showerror("Error", "Invalid Email")


# specifying all details for the widgets
Sub = Label(window, text="Enter URL/Subject")
Sub.grid(row=0, column=0, sticky=N + S + W + E)

FName = Label(window, text="Enter filename to save as")
FName.grid(row=1, column=0, sticky=N + S + W + E)

Mail = Label(window, text="Enter email address")
Mail.grid(row=2, column=0, sticky=N + S + W + E)

Subject = StringVar()
SubEntry = Entry(window, textvariable=Subject)
SubEntry.grid(row=0, column=1, sticky=N + S + W + E)

name = StringVar()
nameEntry = Entry(window, textvariable=name)
nameEntry.grid(row=1, column=1, sticky=N + S + W + E)

mail = StringVar()
mailEntry = Entry(window, textvariable=mail)
mailEntry.grid(row=2, column=1, sticky=N + S + W + E)

button = Button(window, text="Generate QR Code", width=15, command=generate)
button.grid(row=0, column=3, sticky=N + S + W + E)

imageLabel = Label(window)
imageLabel.grid(row=4, column=1, sticky=N + S + W + E)

subLabel = Label(window, text="")
subLabel.grid(row=3, column=1, sticky=N + S + W + E)

saveB = Button(window, text="Save as PNG File", width=15, command=save)
saveB.grid(row=1, column=3, sticky=N + S + W + E)

sendB = Button(window, text="Send QR code", width=15, command=send)
sendB.grid(row=2, column=3, sticky=N + S + W + E)

Rows = 5
Columns = 5

for row in range(Rows + 1):
    window.grid_rowconfigure(row, weight=1)

for col in range(Columns + 1):
    window.grid_columnconfigure(col, weight=1)

# let the program run forever until manually closed by the user
window.mainloop()
