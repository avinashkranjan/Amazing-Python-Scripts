import tkinter as tk

digit = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
denominations = ["", "Thousand", "Million", "Billion", "Trillion"]
tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
ties = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

def convertNumberToWords():
    inputValue = numberEntry.get()

    if not inputValue.isdigit():
        resultLabel.config(text="Invalid Entered Value", fg="red")

    elif len(inputValue) > 15:
        resultLabel.config(text="Entered number is too large", fg="yellow")

    else:

        while len(inputValue) % 3 != 0:
            inputValue = "0" + inputValue

        inputValue = inputValue[::-1]

        def add(s1, s2):
            if s1 and s2:
                return s1 + " " + s2
            return s1 + s2

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

window = tk.Tk()
window.title("Number to Words Converter")
window.configure(background="black")

numberLabel = tk.Label(window, text="Enter Number:", bg="black", fg="white")
numberEntry = tk.Entry(window)
resultLabel = tk.Label(window, text="In Words:", bg="black", fg="white")
convertButton = tk.Button(window, text="Convert", command=convertNumberToWords)

numberLabel.grid(row=0, column=0, padx=10, pady=10)
numberEntry.grid(row=0, column=1, padx=10, pady=10)
convertButton.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
resultLabel.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

window.mainloop()
