from tkinter import *
import math

values = []
vec_window_count = []

def func_main():
    """ Get the Variables to calculate relations """

    global Vec_1
    global Vec_2
    global values
    
    Vals = [V1_x_val.get(), V1_y_val.get(), V1_z_val.get(),
            V2_x_val.get(), V2_y_val.get(), V2_z_val.get()]
    # Validate values
    try:
        for i in range(6):
            Vals[i] = float(Vals[i])
    except:
        SetStatusError()
        return

    DotProduct(Vals)
    CrossProduct(Vals)
    Angle(Vals)
    comp_v_on_v(Vals)
    proj_v_on_v(Vals)

    Vec_1.place(x=355, y=10)
    Vec_2.place(x=355, y=40)
    values = Vals


def DotProduct(Vals):
    """ Dot product of 2 vectors """
    res = (Vals[0]*Vals[3]) + (Vals[1]*Vals[4]) + (Vals[2]*Vals[5])
    dotproduct_entry_val.set(res)
    return res


def CrossProduct(Vals):
    """ Cross product of 2 vectors """
    res_x = (Vals[1] * Vals[5]) - (Vals[4] * Vals[2])
    res_y = (Vals[0] * Vals[5]) - (Vals[3] * Vals[2])
    res_z = (Vals[0] * Vals[4]) - (Vals[1] * Vals[3])
    crossproduct_x_val.set(res_x)
    crossproduct_y_val.set(res_y)
    crossproduct_z_val.set(res_z)


def abs_val(Vals):
    """ Absolute value of a vector |v| """
    res = (Vals[0]**2 + Vals[1]**2 + Vals[2]**2)**0.5
    return res


def Angle(Vals):
    """ Angle between both vectors """
    abs_v1 = abs_val(Vals[:3])
    abs_v2 = abs_val(Vals[3:])
    dot = DotProduct(Vals)
    try:
        ang = round(math.acos(dot / (abs_v1*abs_v2)) * 180 / math.pi, 5)
    except:
        ang = "Invalid"
    angle_val.set(ang)


def comp_v_on_v(Vals):
    """ Compnent of a vector on the other """
    dot_prod = DotProduct(Vals)
    abs_v1 = abs_val(Vals[:3])
    abs_v2 = abs_val(Vals[3:])

    try:
        res_a_on_b = round(dot_prod / abs_v2, 5)
        a_on_b_val.set(res_a_on_b)
    except:
        a_on_b_val.set("Invalid")
        
    try:
        res_b_on_a = round(dot_prod / abs_v1, 5)
        b_on_a_val.set(res_b_on_a)
    except:
        b_on_a_val.set("Invalid")


def proj_v_on_v(Vals):
    """ Projection of a vector on the other """
    dot_prod = DotProduct(Vals)
    abs_v1 = abs_val(Vals[:3])
    abs_v2 = abs_val(Vals[3:])

    try:
        res_a_on_b = round(dot_prod / abs_v2**2, 5)
        x_1 = res_a_on_b * Vals[3]
        y_1 = res_a_on_b * Vals[4]
        z_1 = res_a_on_b * Vals[5]
        a_on_b_proj_x_val.set(x_1)
        a_on_b_proj_y_val.set(y_1)
        a_on_b_proj_z_val.set(z_1)
    except:
        a_on_b_proj_x_val.set("Invalid")
        a_on_b_proj_y_val.set("Invalid")
        a_on_b_proj_z_val.set("Invalid")

    try:
        res_b_on_a = round(dot_prod / abs_v1**2, 5)
        x_2 = res_b_on_a * Vals[0]
        y_2 = res_b_on_a * Vals[1]
        z_2 = res_b_on_a * Vals[2]
        b_on_a_proj_x_val.set(x_2)
        b_on_a_proj_y_val.set(y_2)
        b_on_a_proj_z_val.set(z_2)
    except:
        b_on_a_proj_x_val.set("Invalid")
        b_on_a_proj_y_val.set("Invalid")
        b_on_a_proj_z_val.set("Invalid")

    Status["text"] = "Calculations Completed! :D "
    Status["fg"] = "green"


def SetStatusError():
    """ Sets Status bar label to error message """
    Status["text"] = "Wronge Input(s)... :\ "
    Status["fg"] = "red"


def on_closing():
    """ Closes all Instances """
    global vec_window_count
    global main

    try:
        for window in vec_window_count:
            window.destroy()
        main.destroy()
    except:
        main.destroy()


# <----- Single Vector Properties GUI-Backend Code Block Start ----->
def Show_Vec_Frame(vec_num, values):
    """ Shows the properties of a single vector """
    global vec_window_count
    
    if vec_num == 1:
        values = values[:3]
        title = "Vector A Properties"
    else:
        values = values[3:]
        title = "Vector B Properties"

    vec_window = Tk()
    vec_window.title(title)
    vec_window.geometry("300x250")
    vec_window_count.append(vec_window)

    # Modulus
    Modulus = round(( values[0]**2 + values[1]**2 + values[2]**2 )**0.5, 5)
    Modulus_lbl = Label(vec_window, text="Modulus > ", anchor=E, font=("Calibri", 8))
    Modulus_val = Text(vec_window, height=1, borderwidth=0)
    Modulus_val.insert(1.0, str(Modulus))
    Modulus_lbl.place(x=10, y=10)
    Modulus_val.place(x=70, y=11, width=80)

    # Unit Vectors
    try:
        uv_x = round(values[0]/Modulus, 5)
        uv_y = round(values[1]/Modulus, 5)
        uv_z = round(values[2]/Modulus, 5)
    except:
        uv_x = "Invalid"
        uv_y = "Invalid"
        uv_z = "Invalid"

    Unit_Vector_lbl = Label(vec_window, text="Unit Vector: ", anchor=E, font=("Calibri", 8))
    uv_x_lbl = Label(vec_window, text="X > ", anchor=E, font=("Calibri", 8))
    uv_x_val = Text(vec_window, height=1, borderwidth=0)
    uv_x_val.insert(1.0, str(uv_x))
    uv_y_lbl = Label(vec_window, text="Y > ", anchor=E, font=("Calibri", 8))
    uv_y_val = Text(vec_window, height=1, borderwidth=0)
    uv_y_val.insert(1.0, str(uv_y))
    uv_z_lbl = Label(vec_window, text="Z > ", anchor=E, font=("Calibri", 8))
    uv_z_val = Text(vec_window, height=1, borderwidth=0)
    uv_z_val.insert(1.0, str(uv_z))
    Unit_Vector_lbl.place(x=10, y=30)
    uv_x_lbl.place(x=25, y=50)
    uv_x_val.place(x=50, y=51, width=80)
    uv_y_lbl.place(x=25, y=70)
    uv_y_val.place(x=50, y=71, width=80)
    uv_z_lbl.place(x=25, y=90)
    uv_z_val.place(x=50, y=91, width=80)

    if uv_x != "Invalid":
        alpha = round(math.acos(uv_x) * 180 / math.pi, 5)
        beta = round(math.acos(uv_y) * 180 / math.pi, 5)
        gamma  = round(math.acos(uv_z) * 180 / math.pi, 5)
    else:
        alpha = "Invalid"
        beta = "Invalid"
        gamma = "Invalid"
    Cosine_lbl = Label(vec_window, text="Cosine Angles: ", anchor=E, font=("Calibri", 8))
    alpha_lbl = Label(vec_window, text="X > ", anchor=E, font=("Calibri", 8))
    alpha_val = Text(vec_window, height=1, borderwidth=0)
    alpha_val.insert(1.0, str(alpha))
    beta_lbl = Label(vec_window, text="Y > ", anchor=E, font=("Calibri", 8))
    beta_val = Text(vec_window, height=1, borderwidth=0)
    beta_val.insert(1.0, str(beta))
    gamma_lbl = Label(vec_window, text="Z > ", anchor=E, font=("Calibri", 8))
    gamma_val = Text(vec_window, height=1, borderwidth=0)
    gamma_val.insert(1.0, str(gamma))
    Cosine_lbl.place(x=10, y=120)
    alpha_lbl.place(x=25, y=140)
    alpha_val.place(x=50, y=141, width=80)
    beta_lbl.place(x=25, y=160)
    beta_val.place(x=50, y=161, width=80)
    gamma_lbl.place(x=25, y=180)
    gamma_val.place(x=50, y=181, width=80)
    
    vec_window.mainloop()
# <----- Single Vector Properties GUI-Backend Code Block End ----->


# <----- GUI Code Block Start ----->
# Main Window
main = Tk()
main.title("Vector Calculator")
main.geometry("460x310")
main.protocol("WM_DELETE_WINDOW", on_closing)

# Entry Titles
x_lbl = Label(main, text="X", font=("Calibri", 8))
y_lbl = Label(main, text="Y", font=("Calibri", 8))
z_lbl = Label(main, text="Z", font=("Calibri", 8))
x_lbl.place(x=110, y=15)
y_lbl.place(x=170, y=15)
z_lbl.place(x=230, y=15)

# Vector 1
V1_lbl = Label(main, text="Vector A > ", anchor=E, font=("Calibri", 8))
V1_x_val = StringVar()
V1_x = Entry(main, textvariable=V1_x_val, font=("Calibri", 8))
V1_y_val = StringVar()
V1_y = Entry(main, textvariable=V1_y_val, font=("Calibri", 8))
V1_z_val = StringVar()
V1_z = Entry(main, textvariable=V1_z_val, font=("Calibri", 8))
V1_lbl.place(x=20,y=35)
V1_x.place(x=90, y=36, width=50)
V1_y.place(x=150, y=36, width=50)
V1_z.place(x=210, y=36, width=50)

# Vector 2
V2_lbl = Label(main, text="Vector B > ", anchor=E, font=("Calibri", 8))
V2_x_val = StringVar()
V2_x = Entry(main, textvariable=V2_x_val, font=("Calibri", 8))
V2_y_val = StringVar()
V2_y = Entry(main, textvariable=V2_y_val, font=("Calibri", 8))
V2_z_val = StringVar()
V2_z = Entry(main, textvariable=V2_z_val, font=("Calibri", 8))
V2_lbl.place(x=20,y=65)
V2_x.place(x=90, y=66, width=50)
V2_y.place(x=150, y=66, width=50)
V2_z.place(x=210, y=66, width=50)

# Calculate Button
Calculate = Button(main, text="Calculate", font=("Calibri", 8), command=func_main)
Calculate.place(x=270, y=48, width=70)

# Results Frame ----->
frame = Frame(main, bg="#708090")
frame.place(x=20, y=90, width=420, height=197)

# Dot Product
dotproduct_lbl = Label(frame, text="Dot Product:", anchor=W, bg="#708090", fg="black", font=("Calibri", 8))
dotproduct_lbl.place(x=10, y=10)
dotproduct_entry_val = StringVar()
dotproduct_entry = Entry(frame, textvariable=dotproduct_entry_val, font=("Calibri", 8))
dotproduct_entry.configure(state='readonly')
dotproduct_entry.place(x=80, y=11, width=50)

# Cross Product
crossproduct_lbl = Label(frame, text="Cross Product:", anchor=W, bg="#708090", fg="black", font=("Calibri", 8))
crossproduct_lbl.place(x=10, y=40)
crossproduct_x_lbl = Label(frame, text="X (i) > ", anchor=E, bg="#708090", fg="black", font=("Calibri", 8))
crossproduct_y_lbl = Label(frame, text="Y (j) > ", anchor=E, bg="#708090", fg="black", font=("Calibri", 8))
crossproduct_z_lbl = Label(frame, text="Z (k) > ", anchor=E, bg="#708090", fg="black", font=("Calibri", 8))
crossproduct_x_lbl.place(x=30, y=60)
crossproduct_y_lbl.place(x=30, y=90)
crossproduct_z_lbl.place(x=30, y=120)
crossproduct_x_val = StringVar()
crossproduct_y_val = StringVar()
crossproduct_z_val = StringVar()
crossproduct_x = Entry(frame, textvariable=crossproduct_x_val, font=("Calibri", 8))
crossproduct_x.configure(state='readonly')
crossproduct_x.place(x=65, y=61, width=50)
crossproduct_y = Entry(frame, textvariable=crossproduct_y_val, font=("Calibri", 8))
crossproduct_y.configure(state='readonly')
crossproduct_y.place(x=65, y=91, width=50)
crossproduct_z = Entry(frame, textvariable=crossproduct_z_val, font=("Calibri", 8))
crossproduct_z.configure(state='readonly')
crossproduct_z.place(x=65, y=121, width=50)

# Angle between both vectors
angle_lbl = Label(frame, text="Angle:", anchor=W, bg="#708090", fg="black", font=("Calibri", 8))
angle_lbl.place(x=10, y=160)
angle_val = StringVar()
angle = Entry(frame, textvariable=angle_val, font=("Calibri", 8))
angle.configure(state='readonly')
angle.place(x=50, y=161, width=80)

# Components
component_lbl = Label(frame, text="Components:", anchor=W, bg="#708090", fg="black", font=("Calibri", 8))
component_lbl.place(x=170, y=10)
a_on_b_lbl = Label(frame, text="A on B:", anchor=W, bg="#708090", fg="black", font=("Calibri", 8))
a_on_b_val = StringVar()
a_on_b_ent = Entry(frame, textvariable=a_on_b_val, font=("Calibri", 8))
a_on_b_ent.configure(state='readonly')
b_on_a_lbl = Label(frame, text="B on A:", anchor=W, bg="#708090", fg="black", font=("Calibri", 8))
b_on_a_val = StringVar()
b_on_a_ent = Entry(frame, textvariable=b_on_a_val, font=("Calibri", 8))
b_on_a_ent.configure(state='readonly')
a_on_b_lbl.place(x=190, y=30)
a_on_b_ent.place(x=230, y=31, width=50)
b_on_a_lbl.place(x=190, y=60)
b_on_a_ent.place(x=230, y=61, width=50)

# Projection
comp_per_lbl = Label(frame, text="Projection:", anchor=W, bg="#708090", fg="black", font=("Calibri", 8))
a_on_b_proj_lbl = Label(frame, text="A on B:", anchor=W, bg="#708090", fg="black", font=("Calibri", 8))
b_on_a_proj_lbl = Label(frame, text="B on A:", anchor=W, bg="#708090", fg="black", font=("Calibri", 8))
res_x_lbl = Label(frame, text="X", anchor=W, bg="#708090", fg="black", font=("Calibri", 8))
res_y_lbl = Label(frame, text="Y", anchor=W, bg="#708090", fg="black", font=("Calibri", 8))
res_z_lbl = Label(frame, text="Z", anchor=W, bg="#708090", fg="black", font=("Calibri", 8))
comp_per_lbl.place(x=170, y=90)
a_on_b_proj_lbl.place(x=190, y=130)
b_on_a_proj_lbl.place(x=190, y=160)
res_x_lbl.place(x=250, y=110)
res_y_lbl.place(x=310, y=110)
res_z_lbl.place(x=370, y=110)
a_on_b_proj_x_val = StringVar()
a_on_b_proj_x = Entry(frame, textvariable=a_on_b_proj_x_val, font=("Calibri", 8))
a_on_b_proj_x.configure(state='readonly')
a_on_b_proj_y_val = StringVar()
a_on_b_proj_y = Entry(frame, textvariable=a_on_b_proj_y_val, font=("Calibri", 8))
a_on_b_proj_y.configure(state='readonly')
a_on_b_proj_z_val = StringVar()
a_on_b_proj_z = Entry(frame, textvariable=a_on_b_proj_z_val, font=("Calibri", 8))
a_on_b_proj_z.configure(state='readonly')
a_on_b_proj_x.place(x=230, y=131, width=50)
a_on_b_proj_y.place(x=290, y=131, width=50)
a_on_b_proj_z.place(x=350, y=131, width=50)

b_on_a_proj_x_val = StringVar()
b_on_a_proj_x = Entry(frame, textvariable=b_on_a_proj_x_val, font=("Calibri", 8))
b_on_a_proj_x.configure(state='readonly')
b_on_a_proj_y_val = StringVar()
b_on_a_proj_y = Entry(frame, textvariable=b_on_a_proj_y_val, font=("Calibri", 8))
b_on_a_proj_y.configure(state='readonly')
b_on_a_proj_z_val = StringVar()
b_on_a_proj_z = Entry(frame, textvariable=b_on_a_proj_z_val, font=("Calibri", 8))
b_on_a_proj_z.configure(state='readonly')
b_on_a_proj_x.place(x=230, y=161, width=50)
b_on_a_proj_y.place(x=290, y=161, width=50)
b_on_a_proj_z.place(x=350, y=161, width=50)

# Single vector button entry point
Vec_1 = Button(main, text="Vec A Properties", font=("Calibri", 9), command= lambda: Show_Vec_Frame(1, values))
Vec_2 = Button(main, text="Vec B Properties", font=("Calibri", 9), command= lambda: Show_Vec_Frame(2, values))

# Status Bar
Status = Label(main, text="Hello!! :D", fg="green", font=("Calibri", 8), bd=1, relief=SUNKEN, anchor=W, padx=3)
Status.pack(side=BOTTOM, fill=X)

main.mainloop()
# <----- GUI Code Block End ----->
