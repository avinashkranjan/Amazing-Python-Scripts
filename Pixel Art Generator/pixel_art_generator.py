import turtle
import tkinter as tk
from tkinter import colorchooser, simpledialog, messagebox

turtle.setup(width=800, height=600)
turtle.speed(0)
turtle.title("Pixel Art Generator")


def draw_pixel(x, y, color, size):
    turtle.penup()
    turtle.goto(x - size // 2, y - size // 2)
    turtle.pendown()
    turtle.dot(size, color)


def draw_square(x, y, color, size, fill=False):
    turtle.penup()
    turtle.goto(x - size // 2, y - size // 2)
    turtle.pendown()
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    if fill:
        turtle.end_fill()


def draw_circle(x, y, color, size, fill=False):
    turtle.penup()
    turtle.goto(x, y - size // 2)
    turtle.pendown()
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    turtle.circle(size // 2)
    if fill:
        turtle.end_fill()


def draw_triangle(x, y, color, size, fill=False):
    turtle.penup()
    turtle.goto(x, y - size // 2)
    turtle.pendown()
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    if fill:
        turtle.end_fill()


def draw_diamond(x, y, color, size, fill=False):
    turtle.penup()
    turtle.goto(x, y - size // 2)
    turtle.pendown()
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    for _ in range(2):
        turtle.forward(size)
        turtle.left(45)
        turtle.forward(size)
        turtle.left(135)
    if fill:
        turtle.end_fill()


def draw_heart(x, y, color, size, fill=False):
    turtle.penup()
    turtle.goto(x, y - size // 2)
    turtle.pendown()
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    turtle.left(50)
    turtle.forward(size)
    turtle.circle(size // 2, 180)
    turtle.right(140)
    turtle.circle(size // 2, 180)
    turtle.forward(size)
    if fill:
        turtle.end_fill()


def draw_polygon(x, y, color, size, sides, fill=False):
    turtle.penup()
    turtle.goto(x, y - size // 2)
    turtle.pendown()
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(size)
        turtle.left(angle)
    if fill:
        turtle.end_fill()


def draw_line(x, y, color, size, thickness):
    turtle.penup()
    turtle.goto(x - size // 2, y)
    turtle.pendown()
    turtle.pensize(thickness)
    turtle.pencolor(color)
    turtle.forward(size)


def draw_star(x, y, color, size, points, fill=False):
    turtle.penup()
    turtle.goto(x, y - size // 2)
    turtle.pendown()
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    for _ in range(points):
        turtle.forward(size)
        turtle.right(144)
    if fill:
        turtle.end_fill()


def draw_spiral(x, y, color, size, loops):
    turtle.penup()
    turtle.goto(x, y - size // 2)
    turtle.pendown()
    turtle.pencolor(color)
    for _ in range(loops * 36):
        turtle.forward(size / 20)
        turtle.right(10)


def set_background_color():
    color = colorchooser.askcolor(title="Choose a background color")
    if color[1] is not None:
        turtle.bgcolor(color[1])


def set_pen_style():
    pen_style = simpledialog.askstring(
        "Pen Style", "Enter the pen style (solid/dashed/dotted):")
    if pen_style in ['solid', 'dashed', 'dotted']:
        turtle.pensize(1)
        if pen_style == 'dashed':
            turtle.pendown()
            turtle.pendown(1, 3)
        elif pen_style == 'dotted':
            turtle.pendown()
            turtle.pendown(1, 1)


def get_color():
    color = colorchooser.askcolor(title="Choose a color")
    if color[1] is not None:
        return color[1]
    else:
        return None


def get_size():
    size = simpledialog.askinteger(
        "Size", "Enter the size (5-50):", minvalue=5, maxvalue=50)
    return size


def get_thickness():
    thickness = simpledialog.askinteger(
        "Thickness", "Enter the thickness (1-10):", minvalue=1, maxvalue=10)
    return thickness


def get_sides():
    sides = simpledialog.askinteger(
        "Sides", "Enter the number of sides (3-10):", minvalue=3, maxvalue=10)
    return sides


def main():
    turtle.speed(0)
    turtle.title("Pixel Art Generator")
    turtle.setup(800, 600)

    canvas = turtle.Screen()
    canvas.bgcolor("white")

    while True:
        pattern = tk.simpledialog.askstring(
            "Pattern", "Choose a pattern (square/circle/triangle/diamond/heart/polygon/line/star/spiral/clear/save/background/pen_style/exit):")
        if pattern == 'exit':
            break

        if pattern == 'clear':
            turtle.clear()
            canvas.update()
            continue
        elif pattern == 'save':
            file_path = tk.filedialog.asksaveasfilename(
                defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                canvas.getcanvas().postscript(file=file_path + ".eps")
                canvas.update()
                messagebox.showinfo(
                    "Saved", f"Pixel art saved as {file_path}.png")
            continue
        elif pattern == 'background':
            set_background_color()
            continue
        elif pattern == 'pen_style':
            set_pen_style()
            continue

        color = get_color()
        if color is None:
            break

        size = get_size()
        if not size:
            break

        if pattern == 'square':
            fill = messagebox.askyesno("Fill", "Fill the square with color?")
            draw_func = draw_square
        elif pattern == 'circle':
            fill = messagebox.askyesno("Fill", "Fill the circle with color?")
            draw_func = draw_circle
        elif pattern == 'triangle':
            fill = messagebox.askyesno("Fill", "Fill the triangle with color?")
            draw_func = draw_triangle
        elif pattern == 'diamond':
            fill = messagebox.askyesno("Fill", "Fill the diamond with color?")
            draw_func = draw_diamond
        elif pattern == 'heart':
            fill = messagebox.askyesno("Fill", "Fill the heart with color?")
            draw_func = draw_heart
        elif pattern == 'polygon':
            sides = get_sides()
            if not sides:
                break
            fill = messagebox.askyesno("Fill", "Fill the polygon with color?")
            draw_func = draw_polygon
        elif pattern == 'line':
            thickness = get_thickness()
            if not thickness:
                break
            draw_func = draw_line
            canvas.onclick(lambda x, y: draw_func(
                x, y, color, size, thickness))
            continue
        elif pattern == 'star':
            points = simpledialog.askinteger(
                "Points", "Enter the number of points (5-20):", minvalue=5, maxvalue=20)
            if not points:
                break
            fill = messagebox.askyesno("Fill", "Fill the star with color?")
            draw_func = draw_star
        elif pattern == 'spiral':
            loops = simpledialog.askinteger(
                "Loops", "Enter the number of loops (1-20):", minvalue=1, maxvalue=20)
            if not loops:
                break
            draw_func = draw_spiral

        if pattern != 'line' and pattern != 'star' and pattern != 'spiral':
            canvas.onclick(lambda x, y: draw_func(x, y, color, size, fill))
        else:
            canvas.onclick(lambda x, y: draw_func(
                x, y, color, size, points if pattern == 'star' else loops))

    turtle.done()


if __name__ == "__main__":
    main()
