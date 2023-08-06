import tkinter as tk
from tkinter import ttk

class PortfolioApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Portfolio")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Create a label for the title
        title_label = ttk.Label(self, text="Welcome to My Portfolio", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Create a button to go to the projects page
        projects_button = ttk.Button(self, text="View Projects", command=self.show_projects)
        projects_button.pack(pady=5)

        # Create a button to show more information
        more_info_button = ttk.Button(self, text="More Information", command=self.show_more_info)
        more_info_button.pack(pady=5)

        # Create a button to exit the app
        exit_button = ttk.Button(self, text="Exit", command=self.destroy)
        exit_button.pack(pady=5)

    def show_projects(self):
        projects_window = tk.Toplevel(self)
        projects_window.title("My Projects")
        projects_window.geometry("400x300")

        # Create a label for the projects page
        projects_label = ttk.Label(projects_window, text="List of Projects", font=("Helvetica", 16))
        projects_label.pack(pady=10)

        # Create project descriptions (you can add more as needed)
        project1_label = ttk.Label(projects_window, text="Project 1: Description of project 1.")
        project1_label.pack(pady=5)

        project2_label = ttk.Label(projects_window, text="Project 2: Description of project 2.")
        project2_label.pack(pady=5)

    def show_more_info(self):
        info_window = tk.Toplevel(self)
        info_window.title("More Information")
        info_window.geometry("400x300")

        # Create labels for more information
        info_label = ttk.Label(info_window, text="Experience, Skills, and Contact Details", font=("Helvetica", 16))
        info_label.pack(pady=10)

        # Add more labels here for additional information about yourself
        experience_label = ttk.Label(info_window, text="Experience: Describe your work experience here.")
        experience_label.pack(pady=5)

        skills_label = ttk.Label(info_window, text="Skills: List your skills here.")
        skills_label.pack(pady=5)

        contact_label = ttk.Label(info_window, text="Contact: Your contact details (email, phone, etc.).")
        contact_label.pack(pady=5)

if __name__ == "__main__":
    app = PortfolioApp()
    app.mainloop()
