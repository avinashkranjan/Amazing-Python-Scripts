# Weight Converter GUI

## Description

I have created a GUI based weight converter that accepts a kilogram input value and converts that value to Carat, Gram, Ounce, Pound, Quintal and Tonne (i.e. in decreasing order) when the user clicks the Convert button.

</br>

## Step 1: Creating a window Using Tk

The first step of any GUI is to create a window on which to begin placing components.

We first import everything from the `tkinter` module. We then create a variable called root which is of type `Tk()`. This will be the main window on which we place components later on. The title of the window is then set by calling the `title` function. Finally, the `mainloop()` function is called on root.

</br>

## Step 2: Adding a widget using grid

We can now start adding components, or widgets, to the window. The first widget we shall add will be `Label` widget. The basic construction of a `Label` widget is:

```
Label(<parent>, text=<text>)
```

Where `<parent>` is the parent object and `<text>` is a string which will be the text displayed. We will also need to add the `Label` to the grid and provide a column and row on which to place the widget on the grid.

```
l1.grid(row = 1, column = 1)
```

Now that we want to start placing widgets on a grid, the `Label` we have just created needs to be at column 1, row 1. Thus, when we place the Label on the grid, we provide the attributes column = 1 and row = 1.

This might not look as one would expect. The `Label` we have created is on the far left. The reason for this is because when the widgets are placed on the grid, any empty columns and rows are left empty without any indication of their existence. This means that, although the `Label` is actually in column 2, row 0, this will not be visually apparent until we add more widgets in the surrounding area.

</br>

## Step 3: Spanning widgets over multiple rows and columns

We can span several rows and columns of the grid. To achieve this behaviour, use the columnspan and rowspan attributes when placing a widget on the grid.

```
button.grid(row = 2, column = 2, columnspan = 2, rowspan = 2)
```

This code will place `Button` on the grid with the top corner at (2, 2) and spanning 2 columns, and 2 rows.

</br>

## Adding More Widgets

The `tkinter` module provides 11 different widgets, and there are an additional 6 widgets in the [tkinter.ttk](https://docs.python.org/3/library/tkinter.ttk.html) module. We will only need a few of these to complete our GUI, but the basic use of these widgets is the same.

</br>

### Entry

The `Entry` widget is used to allow the user to enter text. We will use the Entry widget for both the user input, and the output.

Basic `Entry` widgets are created in the following form:

```
Entry(<parent>, textvariable=<variable>)
```

Where `<parent>` is the container of the widget, and `<variable>` is a variable which will be bound to the widget. Not all widgets have the option to bind a variable to them.

When a variable is bound to an `Entry` widget, that variable will always be the value of the text inside the widget and hence the user's input. There are 4 possible types of variable which can be bound to widgets, `StringVar()`, `IntVar()`, `DoubleVar()` and `BooleanVar()`. Of which, not all types can always be used for all widgets.

```
t1.configure(state='disabled')
```

However, we will pass an additional attribute to the constructor of Entry, called `state`. The `state` attribute can take several forms including "active", "disabled", "pressed" and "selected", which define the current state of a widget. For the output Entry we will set its state to "disabled" to prevent the user from editing its contents.

```
t1.configure(state = 'normal')
```

This code would go in the callback for the event that will cause the Button to be enabled.

```
t1.delete("1.0", END)
```

This will delete from postion 0 till end.

</br>

### Button

Next we will add a Button to our GUI. Button widgets are constructed in the following way:

```
Button(<parent>, text=<text>, command=<function>)
```

Where <function> in the command attribute is the action taken when the Button is pressed.

</br>

## Additional feature:

### Exception Handling -

The `try` block lets you test a block of code for errors. The `except` block lets you handle the error.

Here, whenever a user enters any other value (i.e. alphabets, symbols etc.) instead of the interger or float(decimal) value than it will show a message saying "Invalid input" in the textbox.

</br>

## Output:

![wc](https://user-images.githubusercontent.com/73488906/112635679-1f6b5880-8e62-11eb-9b6b-8779f303defd.png)
