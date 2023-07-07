# import modules
from tkinter import *
from tkinter import filedialog
from wallpaper import set_wallpaper

# user define function


def change_wall():

    # set your photo
    try:
        set_wallpaper(str(path.get()))
        check = "success"

    except:

        check = "Wallpaper not found !"
    result.set(check)


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    path.set(filename)

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    return filename


# object of tkinter
# and background set for red
master = Tk()
master.configure(bg='light grey')

# Variable Classes in tkinter
result = StringVar()
path = StringVar()


label_file_explorer = Label(
    master, text="Select a image", width=100, fg="blue")


# Creating label for each information
# name using widget Label
Label(master, text="Select image : ", bg="light grey").grid(row=0, sticky=W)
Label(master, text="Status :", bg="light grey").grid(row=3, sticky=W)


# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=result,
      bg="light grey").grid(row=3, column=1, sticky=W)

# creating a button using the widget
# Button that will call the submit function
b = Button(master, text="Open", command=browseFiles, bg="white")
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)

label_file_explorer.grid(column=1, row=1)

c = Button(master, text="Apply", command=change_wall, bg="white")
c.grid(row=2, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)

mainloop()
