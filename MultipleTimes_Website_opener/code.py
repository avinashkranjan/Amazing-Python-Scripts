import webbrowser  # Import the webbrowser module

# Prompt user for the number of times to open the website
n = int(input('enter how many times you want to open website?'))

for e in range(n):  # Loop 'n' times
    # Open the specified website in a new tab
    webbrowser.open_new_tab(
        'https://github.com/avinashkranjan/Amazing-Python-Scripts')
