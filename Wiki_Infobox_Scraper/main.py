from bs4 import BeautifulSoup
import requests
from tkinter import *

info_dict = {}


def error_box():
    """
    A function to create a pop-up, in case the code errors out
    """
    global mini_pop

    mini_pop = Toplevel()
    mini_pop.title('Error screen')

    mini_l = Label(mini_pop, text=" !!!\nERROR FETCHING DATA",
                   fg='red', font=('Arial', 10, 'bold'))
    mini_l.grid(row=1, column=1, sticky='nsew')
    entry_str.set("")


def wikiScraper():
    """
    Function scrapes the infobox lying under the right tags and displays 
    the data obtained from it in a new window
    """
    global info_dict

    # Modifying the user input to make it suitable for the URL
    entry = entry_str.get()
    entry = entry.split()
    query = '_'.join([i.capitalize() for i in entry])
    req = requests.get('https://en.wikipedia.org/wiki/'+query)

    # to check for valid URL
    if req.status_code == 200:
        # for parsing through the html text
        soup = BeautifulSoup(req.text, 'html.parser')

        # Finding text within infobox and storing it in a dictionary
        info_table = soup.find('table', {'class': 'infobox'})

        try:
            for tr in info_table.find_all('tr'):
                try:
                    if tr.find('th'):
                        info_dict[tr.find('th').text] = tr.find('td').text
                except:
                    pass

        except:
            error_box()

        # Creating a pop up window to show the results
        global popup
        popup = Toplevel()
        popup.title(query)

        r = 1

        for k, v in info_dict.items():
            e1 = Label(popup, text=k+" : ", bg='cyan4',
                       font=('Arial', 10, 'bold'))
            e1.grid(row=r, column=1, sticky='nsew')

            e2 = Label(popup, text=info_dict[k], bg="cyan2", font=(
                'Arial', 10, 'bold'))
            e2.grid(row=r, column=2, sticky='nsew')

            r += 1
            e3 = Label(popup, text='', font=('Arial', 10, 'bold'))
            e3.grid(row=r, sticky='s')
            r += 1

        entry_str.set("")
        info_dict = {}

    else:
        print('Invalid URL')
        error_box()


# Creating a window to take user search queries
root = Tk()
root.title('Wikipedia Infobox')

global entry_str
entry_str = StringVar()

search_label = LabelFrame(root, text="Search: ",
                          font=('Century Schoolbook L', 17))
search_label.pack(pady=10, padx=10)

user_entry = Entry(search_label, textvariable=entry_str,
                   font=('Century Schoolbook L', 17))
user_entry.pack(pady=10, padx=10)

button_frame = Frame(root)
button_frame.pack(pady=10)

submit_bt = Button(button_frame, text='Submit',
                   command=wikiScraper, font=('Century Schoolbook L', 17))
submit_bt.grid(row=0, column=0)

root.mainloop()
