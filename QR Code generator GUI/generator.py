# pip install qrcode[pil]

import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def generate_qr_code(data, filename='qr_code.png', scale=10):

    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=scale,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save(filename)

        return filename

    except Exception as e:
        print(f"Error generating QR code: {e}")
        return None


def generate_qr_button_click():
    qr_data = qr_data_entry.get()
    qr_image = generate_qr_code(qr_data)
    if qr_image:
        img = Image.open(qr_image)
        photo = ImageTk.PhotoImage(img)

        qr_label.config(image=photo)
        qr_label.image = photo

        result_label.config(text="QR code generated successfully.")
    else:
        result_label.config(text="Failed to generate the QR code.")


def save_qr_button_click():
    qr_data = qr_data_entry.get()
    qr_filename = filedialog.asksaveasfilename(defaultextension=".png",
                                               filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])
    if qr_filename:
        qr_image = generate_qr_code(qr_data, qr_filename)
        if qr_image:
            result_label.config(text=f"QR code image saved to: {qr_image}")
        else:
            result_label.config(text="Failed to save the QR code.")
    else:
        result_label.config(text="QR code download canceled.")


root = tk.Tk()
root.title("QR Code Generator")


root.configure(bg='#1E1E1E')
root.option_add('*foreground', 'white')
root.option_add('*activeForeground', 'white')
root.option_add('*background', '#1E1E1E')
root.option_add('*activeBackground', '#444444')
root.option_add('*highlightBackground', '#444444')
root.option_add('*selectBackground', '#444444')
root.option_add('*selectForeground', 'white')
root.option_add('*font', 'Helvetica 12')


qr_data_label = tk.Label(root, text="Enter the data for QR code:")
qr_data_label.pack(pady=5)

qr_data_entry = tk.Entry(root, width=40)
qr_data_entry.pack(pady=5)

generate_qr_button = tk.Button(
    root, text="Generate QR Code", command=generate_qr_button_click)
generate_qr_button.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

save_qr_button = tk.Button(root, text="Save QR Code",
                           command=save_qr_button_click)
save_qr_button.pack(pady=5)

result_label = tk.Label(root, text="", fg="white")
result_label.pack(pady=5)


root.mainloop()
