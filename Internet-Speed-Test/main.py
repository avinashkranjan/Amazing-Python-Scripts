from speedtest import Speedtest
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

PRIMARY_COLOR = "#4287f5"
SECONDARY_COLOR = "#ffffff"

speed = Speedtest()


def measure_internet_speed():
    print("Running speed test...")

    download_speed = speed.download()
    # To Convert to Mbps
    download_speed = download_speed / 1024 / 1024
    print(f"Download Speed: {download_speed:.2f} Mbps")
    download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")

    upload_speed = speed.upload()
    # To Convert to Mbps
    upload_speed = upload_speed / 1024 / 1024
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")

    ping_latency = speed.results.ping
    print(f"Ping latency: {ping_latency:.2f} ms")
    ping_label.config(text=f"Latency: {ping_latency:.2f} ms")

    server = speed.get_best_server()
    print(f"Server: {server['sponsor']} ({server['name']})")
    server_label.config(text=f"Server: {server['sponsor']} ({server['name']})")


window = tk.Tk()
window.title("Internet Speed Test")
window.geometry("500x250")


style = ThemedStyle(window)
style.theme_use('clam')
style.configure("TLabel", foreground=PRIMARY_COLOR, background=SECONDARY_COLOR)
style.configure("TButton", foreground=SECONDARY_COLOR,
                background=PRIMARY_COLOR)


download_label = ttk.Label(
    window, text="Download Speed: ", font=("TkDefaultFont", 15, "bold"))
download_label.pack(pady=10)

upload_label = ttk.Label(window, text="Upload Speed: ",
                         font=("TkDefaultFont", 15, "bold"))
upload_label.pack(pady=10)

ping_label = ttk.Label(window, text="Latency: ",
                       font=("TkDefaultFont", 15, "bold"))
ping_label.pack(pady=10)

server_label = ttk.Label(window, text="Server: ",
                         font=("TkDefaultFont", 15, "bold"))
server_label.pack(pady=10)

measure_button = tk.Button(window, text=" Run Speed Test ", command=measure_internet_speed,
                           fg=SECONDARY_COLOR, bg=PRIMARY_COLOR, font=("TkDefaultFont", 12, "bold"))
measure_button.pack(pady=10)

window.mainloop()
