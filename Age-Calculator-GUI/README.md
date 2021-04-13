# Age Calculator GUI

In this age calculator app, users can type in their date of birth, and the app will calculate and display their age. 

## Step 1:

First of all, we need to import two libraries into our code. The first one is the *tkinter* library. Then, we need the *datetime* library to work with dates.

## Step 2:

Now, let’s create a simple window for our app and name it as *Age Calculator*.

## Step 3:

Then, we are going to create four labels, each for the name, year, month, and the date, and put them in the grid.

We will create entry fields to get the user inputs corresponding to all the labels created. Put them at the right side of the corresponding labels using the *grid* method.

## Step 4:

Then, we are going to define a function, which will calculate the age of the user by subtracting the user’s birth date from today’s date. We name that function as `ageCalc()`. 

Then, we create a `Label` area that will display the age of the user as output in the function itself.

## Step 5:

Then, we are going to create a button for users to submit their input values. We link the button to the `ageCalc` function.

Finally, let’s run everything inside the window using the `mainloop()` method.
