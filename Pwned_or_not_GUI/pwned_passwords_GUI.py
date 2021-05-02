import tkinter as tk
import requests
import hashlib


def send_request_to_API(start_char):
    """
    The function sends request to the API.
    """
    # first 5 characters of hashed password added to the URL
    url = 'https://api.pwnedpasswords.com/range/' + start_char
    try:
        res = requests.get(url)

        # Only status code of 200 returns relevant data
        if res.status_code != 200:
            print('\nError fetching results!!!')
            return 0

        return res

	# In case connection was not even established
    except:
        print('\nConnection Error!!!')
        return 0


def get_count(res, suffix):
    """
    The function helps to obtain relevant information for the given
	hashed password
    """
    # The data has a ':' delimiter separating the hashed password and its count
    results = (line.split(':') for line in res.text.splitlines())

    for hashed, count in results:
        # Finding match for the last 5 characters of the hashed password
        if hashed == suffix:
            return count

    return 0


def password_hashing(password):
    """
    The function generates the SHA-1 hash of a UTF-8 encoded password given by
	user
    """
    sha1pass = hashlib.sha1(password.encode('utf -8')).hexdigest().upper()

    # Inorder to maintain anonymity while sending password to the API,
	# storing only the partial hash for searching
    head, tail = sha1pass[:5], sha1pass[5:]
    return head, tail


def submit_info():
	"""
	The function stores the user input password and displays the result in a
	pop up window
	"""
	# Returns the string obtained from Entry
	password = pass_var.get()

	start, end = password_hashing(password)
	res = send_request_to_API(start)

	if res:
		num = get_count(res, end)

		if num:
			Text = f'Password found {num} times in the dataset.\n Recommended to change it ASAP!'
		else:
			Text = 'Your password was not found in the dataset. \nYou have a safe password!'

	else:
		Text = 'Error fetching results'

	# Creating a popup window to display results
	global popup
	popup = tk.Toplevel()
	popup.title("Status")
	popup.geometry("400x100")

	tk.Label(popup, text = Text, font = ('DejaVu Serif',11, 'bold')).pack()
	button = tk.Button(popup, text="OK", command=popup.destroy)
	button.place(x = 175, y = 50)
	
	pass_var.set("")


def show_call():
	"""
	Call-back function for show_button to show the hidden password
	"""
	pass_entry = tk.Entry(root, textvariable = pass_var, font = ('Ubuntu',12, 'bold'), show = '', justify='center')
	pass_entry.place(x=100, y=25)


def hide_call():
	"""
	Call-back function for hide_button to hide the password
	"""
	pass_entry = tk.Entry(root, textvariable = pass_var, font = ('Ubuntu',12, 'bold'), show = '*', justify='center')
	pass_entry.place(x=100, y=25)


def main():
	"""
	Generates the main window using tkinter which takes user's password as input
	"""
	global root
	root = tk.Tk()
	root.title("Pwned or Not?")
	root.geometry("400x150")

	global pass_var
	pass_var=tk.StringVar()

	pass_label = tk.Label(root, text = 'Enter your password:', font = ('Ubuntu',12, 'bold'))
	pass_entry = tk.Entry(root, textvariable = pass_var, font = ('Ubuntu',12, 'bold'), show = '*', justify='center')

	show_button = tk.Button(root, text="Show", command=show_call) 
	hide_button = tk.Button(root,text="Hide", command=hide_call) 
	sub_btn = tk.Button(root,text = 'Submit', font = ('Ubuntu',12, 'bold'), command=submit_info)

	pass_label.place(x=100)
	pass_entry.place(x=100, y=25)

	show_button.place(x=115, y=55)
	hide_button.place(x=235, y=55)

	sub_btn.place(x=160, y=100)

	root.mainloop()


if __name__ == '__main__':
	main()

