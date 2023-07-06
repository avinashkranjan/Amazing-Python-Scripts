from tkinter import *
# import os
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage

# QR Code Generator | Designed by Jay Gohel


class Qr_Genrator():
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry('900x500+200+50')
        self.root.resizable(False, False)

        title = Label(self.root, text="  QR Code Genrator", font=(
            "time new roman", 40), bg="#F96900", fg="white", anchor="w").place(x=0, y=0, relwidth=1)

        # Variable
        self.var_emp_code = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_designation = StringVar()

        # Employee detail window design
        emp_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        emp_Frame.place(x=50, y=100, width=500, height=380)

        emp_title = Label(emp_Frame, text="  Employee Details", font=(
            "goudy old style", 20), bg="#FB9316", fg="white").place(x=0, y=0, relwidth=1)
        lbl_emp_code = Label(emp_Frame, text="  Employee ID", font=(
            "time new roman", 15), bg="white").place(x=20, y=60)
        lbl_emp_name = Label(emp_Frame, text="  Name", font=(
            "time new roman", 15), bg="white").place(x=20, y=100)
        lbl_emp_dept = Label(emp_Frame, text="  Department", font=(
            "time new roman", 15), bg="white").place(x=20, y=140)
        lbl_emp_designation = Label(emp_Frame, text="  Designation", font=(
            "time new roman", 15), bg="white").place(x=20, y=180)

        text_emp_code = Entry(emp_Frame, font=(
            "time new roman", 15), textvariable=self.var_emp_code, bg="lightyellow").place(x=200, y=60)
        text_emp_name = Entry(emp_Frame, font=(
            "time new roman", 15), textvariable=self.var_name, bg="lightyellow").place(x=200, y=100)
        text_emp_dept = Entry(emp_Frame, font=(
            "time new roman", 15), textvariable=self.var_department, bg="lightyellow").place(x=200, y=140)
        text_emp_designation = Entry(emp_Frame, font=(
            "time new roman", 15), textvariable=self.var_designation, bg="lightyellow").place(x=200, y=180)

        btn_genrator = Button(emp_Frame, text="QR Genrator", command=self.genrate, font=(
            "time new roman", 15, "bold"), bg="#2196f3", fg="white").place(x=90, y=250, width=180, height="30")
        btn_clear = Button(emp_Frame, text="Clear", command=self.clear, font=(
            "time new roman", 15, "bold"), bg="#2196f3", fg="white").place(x=290, y=250, width=120, height="30")

        self.msg = ""
        self.lbl_msg = Label(emp_Frame, text=self.msg, font=(
            "time new roman", 15), bg="white", fg="green")
        self.lbl_msg.place(x=0, y=320, relwidth=1)

        # Qr Code window design
        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        qr_Frame.place(x=600, y=100, width=250, height=380)

        emp_title = Label(qr_Frame, text="Employee QR code", font=(
            "goudy old style", 15), bg="#FB9316", fg="white").place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_Frame, text="No QR\n available", font=(
            "time new roman", 15), bg="#D76C02", fg="white", bd=1, relief=RIDGE)
        self.qr_code.place(x=35, y=100, width=180, height=180)

    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg = ""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def genrate(self):
        if self.var_emp_code.get() == '' or self.var_name.get() == '' or self.var_department.get() == '' or self.var_designation.get() == '':
            self.msg = "All filed required !!!"
            self.lbl_msg.config(text=self.msg, fg="red")

        else:
            qr_data = (
                f"Employee Id:{self.var_emp_code.get()}\nEmployee Name:{self.var_name.get()}\nDepartment:{self.var_department.get()}\nDesignation:{self.var_designation.get()}")
            qr_code = qrcode.make(qr_data)
            # print(qr_code)
            qr_code = resizeimage.resize_cover(qr_code, [180, 180])
            qr_code.save('./QR-code-Genrator/employee_qr/emp_' +
                         str(self.var_emp_code.get()+'.png'))
            # qr code img update
            self.im = ImageTk.PhotoImage(
                file='../QR-code-Genrator/employee_qr/emp_'+str(self.var_emp_code.get()+'.png'))
            self.qr_code.config(image=self.im)

            # updating noti
            self.msg = "QR genrated Successful!!"
            self.lbl_msg.config(text=self.msg, fg="green")


root = Tk()
obj = Qr_Genrator(root)
root.mainloop()
