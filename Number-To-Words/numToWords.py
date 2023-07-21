'''
Python program to convert entered number into words as shown in the example

Input = 123
Output = "One Hundred Twenty Three"
'''

# Including this library to create a gui for the program
import tkinter as tk

# Initialising some variables
digit = ["Zero", "One", "Two", "Three", "Four",
         "Five", "Six", "Seven", "Eight", "Nine"]
denominations = ["", "Thousand", "Million", "Billion", "Trillion"]
tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
        "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
ties = ["Ten", "Twenty", "Thirty", "Forty",
        "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

# Function which handles the algorithm written inside init


def convertNumberToWords():
    # Getting value from the input box of GUI
    inputValue = numberEntry.get()

    # Checking entered value is number or not
    if not inputValue.isdigit():
        resultLabel.config(text="Invalid Entered Value", fg="red")

    # Checking entered value is of length 15 or not
    elif len(inputValue) > 15:
        resultLabel.config(text="Entered number is too large", fg="yellow")

    # Finally converting the entered number into international system of numbering
    else:
        # Algorithm starts

        # This while loop is used to convert the entered number into the completed pair of 3 numbers
        # So "0" is added at the front of the number
        while len(inputValue) % 3 != 0:
            inputValue = "0" + inputValue

        inputValue = inputValue[::-1]

        # Add function is used to concatenate two string by giving space between them
        def add(s1, s2):
            if s1 and s2:
                return s1 + " " + s2
            return s1 + s2

        # Convert function will recursively call to convert the entered number with the pair of the 3 numbers
        def convert(index, level):
            if index >= len(inputValue):
                return ""

            cur = ""
            od = int(inputValue[index])
            td = int(inputValue[index + 1])
            hd = int(inputValue[index + 2])

            if hd:
                cur = add(cur, add(digit[hd], "Hundred"))

            if td:
                if td == 1:
                    cur = add(cur, tens[od])
                else:
                    cur = add(cur, ties[td - 1])
                    if od:
                        cur = add(cur, digit[od])
            elif od:
                cur = add(cur, digit[od])

            if cur:
                cur = add(cur, denominations[level])

            return add(convert(index + 3, level + 1), cur)

        result = "Zero" if inputValue == "000" else convert(0, 0)
        resultLabel.config(text=result, fg="white")


# GUI formation starts
window = tk.Tk()
window.title("Number to Words Converter")  # This is the title of the GUI
window.configure(background="black")  # Background of the GUI

numberLabel = tk.Label(window, text="Enter Number:", bg="black", fg="white")
# Getting data from the user while entering into the input box
numberEntry = tk.Entry(window)
# Result label will print answer get by the algorithm
resultLabel = tk.Label(window, text="In Words:", bg="black", fg="white")
# Calling/Trigger the function to convert the number
convertButton = tk.Button(window, text="Convert", command=convertNumberToWords)

numberLabel.grid(row=0, column=0, padx=10, pady=10)
numberEntry.grid(row=0, column=1, padx=10, pady=10)
convertButton.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
resultLabel.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

# Finally starting the GUI program
window.mainloop()
