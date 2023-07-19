from tkinter import *
from tkinter.ttk import Progressbar
import speedtest
import time


def animate_speed(speed_value, progress_bar, scaling_factor):
    max_value = speed_value * scaling_factor
    increment = max_value / 100
    for i in range(int(max_value) + 1):
        if i > 0.9 * max_value:
            break
        progress_bar['value'] = i
        progress_bar.update()
        time.sleep(0.02)


def check_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000
    upload_speed = st.upload() / 1000000
    ping = st.results.ping
    download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
    upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
    ping_label.config(text=f"Ping: {ping:.2f} ms")
    animate_speed(download_speed, download_progress, 5)
    animate_speed(upload_speed, upload_progress, 3)
    animate_speed(ping, ping_progress, 2)


root = Tk()
root.title("Internet Speed Checker")
root.config(bg="#212121")
root.geometry("500x400")
root.resizable(False, False)

label1 = Label(root, text="Internet Speed Checker", font=(
    "Helvetica", 30, "bold"), bg="#212121", fg="#ffffff")
label1.pack()

download_label = Label(root, font=("Helvetica", 16),
                       bg="#212121", fg="#ffffff")
download_label.pack(pady=10)

download_progress = Progressbar(
    root, orient=HORIZONTAL, length=300, mode='determinate')
download_progress.pack(pady=10)

upload_label = Label(root, font=("Helvetica", 16), bg="#212121", fg="#ffffff")
upload_label.pack(pady=10)

upload_progress = Progressbar(
    root, orient=HORIZONTAL, length=300, mode='determinate')
upload_progress.pack(pady=10)

ping_label = Label(root, font=("Helvetica", 16), bg="#212121", fg="#ffffff")
ping_label.pack(pady=10)

ping_progress = Progressbar(root, orient=HORIZONTAL,
                            length=300, mode='determinate')
ping_progress.pack(pady=10)

check_speed()

button_refresh = Button(root, text="Refresh", font=(
    "Helvetica", 14, "bold"), bg="#03a9f4", fg="#ffffff", command=check_speed)
button_refresh.pack(pady=20)

root.mainloop()
