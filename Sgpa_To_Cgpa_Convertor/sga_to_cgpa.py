import tkinter as tk


# Create SGPA entries based on the total number of semesters entered by the user.
def create_sgpa_entries():
    num_semesters = int(num_semesters_entry.get())

    for i in range(num_semesters):
        sgpa_label = tk.Label(sgpa_frame, text=f"SGPA for Semester {i + 1}:")
        sgpa_label.grid(row=i + 2, column=0, padx=10, pady=5, sticky="E")

        sgpa_entry = tk.Entry(sgpa_frame)
        sgpa_entry.grid(row=i + 2, column=1, padx=10, pady=5, sticky="W")
        sgpa_entry.bind('<KeyRelease>', validate_sgpa_entries)

        sgpa_labels.append(sgpa_label)
        sgpa_entries.append(sgpa_entry)

    create_sgpa_buttons.grid_remove()
    cgpa_calc.grid(row=num_semesters + 2, column=0,
                   columnspan=2, padx=10, pady=5)


# Validate the SGPA entries to enable or disable the CGPA calculation button.
def validate_sgpa_entries():
    filled_entries = [entry.get() for entry in sgpa_entries]
    if all(filled_entries):
        cgpa_calc.configure(state="normal")
    else:
        cgpa_calc.configure(state="disabled")


def calculate_cgpa():  # It is used to calculate cgpa.
    sgpa_values = [float(sgpa_entry.get()) for sgpa_entry in sgpa_entries]

    total_sgpa = sum(sgpa_values)
    num_semesters = len(sgpa_values)
    cgpa = total_sgpa / num_semesters

    cgpa_label.configure(text=f"CGPA: {cgpa:.2f}")

    reset_button.configure(state="normal")


def reset_entries():  # This is used to reset entries after calcuting Cgpa.
    for label in sgpa_labels:
        label.destroy()
    for entry in sgpa_entries:
        entry.destroy()
    sgpa_labels.clear()
    sgpa_entries.clear()

    create_sgpa_buttons.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
    cgpa_calc.configure(state="disabled")
    cgpa_label.configure(text="CGPA: ")

    reset_button.configure(state="disabled")


root = tk.Tk()
root.title("SGPA to CGPA Converter")

sgpa_frame = tk.Frame(root)
sgpa_frame.pack(pady=10)

num_semesters_label = tk.Label(sgpa_frame, text="Total Number of Semesters:")
num_semesters_label.grid(row=0, column=0, padx=10, pady=5, sticky="E")

num_semesters_entry = tk.Entry(sgpa_frame)
num_semesters_entry.grid(row=0, column=1, padx=10, pady=5, sticky="W")

sgpa_labels = []
sgpa_entries = []

create_sgpa_buttons = tk.Button(
    sgpa_frame, text="Create SGPA Entries", command=create_sgpa_entries)
create_sgpa_buttons.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

cgpa_calc = tk.Button(sgpa_frame, text="Calculate CGPA",
                      command=calculate_cgpa, state="disabled")

cgpa_label = tk.Label(root, text="CGPA: ")
cgpa_label.pack()

reset_button = tk.Button(
    root, text="Reset", command=reset_entries, state="disabled")
reset_button.pack()

root.mainloop()
