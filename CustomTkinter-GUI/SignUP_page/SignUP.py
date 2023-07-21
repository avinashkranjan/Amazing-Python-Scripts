import tkinter as tk
import tkinter.messagebox
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter.font import Font
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")


def check_credentials(username, password):
    # Read the stored usernames and passwords from text files
    with open('File Path Where username is stored', 'r') as f_username, open('File Path where password is stored', 'r') as f_password:
        stored_usernames = f_username.read().splitlines()
        stored_passwords = f_password.read().splitlines()

    # Check if the entered credentials match any of the stored values
    for stored_username, stored_password in zip(stored_usernames, stored_passwords):
        if username == stored_username and password == stored_password:
            return True

    return False


class Login(customtkinter.CTk):
    width = 1240  # helps in image width
    height = 1080  # helps in image height

    def __init__(self):
        super().__init__()

        # OPENEING WINDOW SIZE
        self.title("Login")
        self.geometry(f"{1240}x{720}")
        # IMAGE ADDITION IN BACKGROUND
        # self.bg_image = customtkinter.CTkImage(Image.open("Image Path"),size=(self.width, self.height))
        # self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        # self.bg_image_label.grid(row=0, column=0)

        # LOGIN FRAME INSIDE WINDOW
        # TEXT : "Welcome!\nUnified Travelling & Transport System"
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=15)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Welcome!\nTo lOIGN pAGE", font=customtkinter.CTkFont(
            size=24, weight="bold", slant="roman", family="Helvetica"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        # TEXT : LOGIN PAGE
        self.login_label_2 = customtkinter.CTkLabel(
            self.login_frame, text="Login Page", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.login_label_2.grid(row=1, column=0, padx=30, pady=(50, 15))

        # TEXT : USERNAME
        self.username_entry = customtkinter.CTkEntry(
            self.login_frame, width=300, placeholder_text="Username")
        self.username_entry.grid(row=2, column=0, padx=30, pady=(15, 15))

        # TEXT : PASSWORD
        self.password_entry = customtkinter.CTkEntry(
            self.login_frame, width=300, show="*", placeholder_text="Password")
        self.password_entry.grid(row=3, column=0, padx=30, pady=(0, 15))

        # TEXT : LOGIN BUTTON TEXT
        self.login_button = customtkinter.CTkButton(
            self.login_frame, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=4, column=0, padx=30, pady=(15, 15))

    def login_event(self):

        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        QueryCheckForPassword = sql.Query_LoginCheck(
            entered_username, entered_password)

        if QueryCheckForPassword:
            self.destroy()

        else:
            print("error")
            return messagebox.showerror('Error', 'Incorrect Username or Password')

        print("Login pressed - username:", entered_username,
              "password:", entered_password)


if __name__ == "__main__":
    app9 = Login()
    app9.mainloop()
