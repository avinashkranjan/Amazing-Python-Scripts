# pylint: disable=invalid-name

"""
This module is imported to create a modern GUI.
"""

import customtkinter


class FeedBack(customtkinter.CTk):
    """
    A class representing a feedback GUI.

    This class inherits from customtkinter.CTk and provides a graphical user interface
    for collecting user feedback.

    Attributes:
        textbox (customtkinter.CTkTextbox): The text box widget for displaying instructions.
        feedback (customtkinter.CTkEntry): The entry widget for collecting user feedback.
        button (customtkinter.CTkButton): The button widget for submitting the feedback.

    Methods:
        __init__(): Initializes the FeedBack class.
        button_callback(): Callback function for the button click event.
    """

    def __init__(self):
        super().__init__()

        self.geometry("300x200")
        self.title("User FeedBack")
        self.minsize(300, 200)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.textbox = customtkinter.CTkTextbox(master=self)
        self.textbox.grid(row=0, column=0, padx=10,
                          pady=(10, 0), sticky="nsew")
        text = (
            "         Please enter your valuable Feedback  \n"
            " We are sorry you have to delete your account  \n"
            "                     Help us to improve\n"
        )
        self.textbox.insert("1.0", text)

        self.feedback = customtkinter.CTkEntry(
            master=self, placeholder_text="FeedBack")
        self.feedback.grid(row=1, column=0, padx=10, pady=5, sticky='ew')

        self.button = customtkinter.CTkButton(
            master=self, command=self.button_callback, text="Done")
        self.button.grid(row=2, column=0, padx=10, pady=(0, 20), sticky="ew")

    def button_callback(self):
        """
        Callback function for the button click event.

        This function is triggered when the user clicks the "Done" button.
        It retrieves the user feedback from the input field and writes it to a file.
        """
        def writing_feedback():
            fdbck = self.feedback.get()
            with open('CustomTkinter-GUI/Feedback_GUI/FeedbackGUI', 'w', encoding="utf-8") as feedbck:
                feedbck.write(str(fdbck))
        writing_feedback()
        self.destroy()


if __name__ == "__main__":
    app = FeedBack()
    app.mainloop()
