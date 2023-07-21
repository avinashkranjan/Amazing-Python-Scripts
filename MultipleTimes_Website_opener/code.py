import webbrowser  # Import the webbrowser module

n = int(input('enter how many times you want to open website?'))  # Prompt user for the number of times to open the website

for e in range(n):  # Loop 'n' times
    webbrowser.open_new_tab('https://github.com/avinashkranjan/Amazing-Python-Scripts')  # Open the specified website in a new tab
