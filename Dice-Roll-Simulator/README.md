# Dice Rolling Simulator

## Description
We all know about dice. It’s a simple cube with numbers from 1 to 6 written on its face. But what is simulation? It is making a computer model. Thus, a dice simulator is a simple computer model that can roll a dice for us.

</br>

### Step 1: Importing the required modules
</br>

We will import the following modules:
- Tkinter: Imported to use Tkinter and make GUI applications.
- Image, Imagetk: Imported from PIL, i.e. Python Imaging Library. We use it to perform operations involving images in our UI.
- Random: Imported to generate random numbers.

</br>

### Step 2: Building a top-level widget to make the main window for our application
</br>

In this step, we will build the main window of our application, where the buttons, labels, and images will reside. We also give it a title by title() function.

</br>

### Step 3: Designing the buttons
</br>

Now, just think, what we need to roll a die? Just our hands!

Here, we use **pack()** to arrange our widgets in row and column form. The ‘BlankLine’ label is to skip a line, whereas we use ‘HeadingLabel’ label to give a heading.

- **root** – the name by which we refer to the main window of the application
- **text** – text to be displayed in the HeadingLabel
- **fg** – the colour of the font used in HeadingLabel
- **bg** – background colour of the HeadingLabel
- **font** – used to give customised fonts to the HeadingLabel text
- **.pack()** – Used to pack the widget onto the root window

</br>

### Step 4: Forming a list of images to be randomly displayed
</br>

‘dice’ is the list of names of images kept in same folder, which are chosen randomly according to the random number generated.
</br>

‘DiceImage’ is used to store an image of dice which is chosen by randomly generated numbers.

</br>

### Step 5: Constructing a label for image, adding a button and assigning functionality
</br>

‘ImageLabel’ is to place an image in the window. The parameter expands declared as True so that even if we resize the window, image remains in the center.
</br>

Major function:

‘rolling_dice’ function is a function that is executed every time a button is clicked. This is attained through the ‘command=rolling_dice’ parameter while defining a button.

</br>

### Step 6: Forming a list of images to be randomly displayed
</br>

‘root.mainloop()’ is used to open the main window. It acts as the main function of our program.