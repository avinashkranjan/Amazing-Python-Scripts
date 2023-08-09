import tkinter as tk
from tkinter import ttk
from threading import Thread
import time
from datetime import datetime, timedelta
import winsound


class NotificationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notification App")
        self.geometry("400x250")
        self.configure(bg="black")

        style = ttk.Style(self)
        style.configure("TLabel", foreground="white",
                        background="black", font=("Helvetica", 12))
        style.configure("TButton", foreground="black",
                        background="white", font=("Helvetica", 12))

        self.label_days = ttk.Label(self, text="Days:")
        self.label_days.pack(pady=5)

        self.entry_days = ttk.Entry(self)
        self.entry_days.pack()

        self.label_hours = ttk.Label(self, text="Hours:")
        self.label_hours.pack(pady=5)

        self.entry_hours = ttk.Entry(self)
        self.entry_hours.pack()

        self.label_minutes = ttk.Label(self, text="Minutes:")
        self.label_minutes.pack(pady=5)

        self.entry_minutes = ttk.Entry(self)
        self.entry_minutes.pack()

        self.label_seconds = ttk.Label(self, text="Seconds:")
        self.label_seconds.pack(pady=5)

        self.entry_seconds = ttk.Entry(self)
        self.entry_seconds.pack()

        self.label_message = ttk.Label(
            self, text="Enter notification message:")
        self.label_message.pack(pady=5)

        self.entry_message = ttk.Entry(self)
        self.entry_message.pack()

        self.button_set = ttk.Button(
            self, text="Set Notification", command=self.schedule_notification)
        self.button_set.pack(pady=10)

        self.label_time_left = ttk.Label(
            self, text="Time left: 0 days, 0:00:00")
        self.label_time_left.pack(pady=5)

    def show_notification(self):
        message = self.entry_message.get() or "This is a sample notification."
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notification_window = tk.Toplevel(self)
        notification_window.title("Notification")
        notification_window.geometry("300x150")
        notification_window.configure(bg="black")

        notification_label = ttk.Label(notification_window, text=f"{message}\n\nCurrent time: {now}", font=(
            "Helvetica", 12), foreground="white", background="black")
        notification_label.pack(pady=10)

        # Play notification sound
        try:
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        except:
            pass

    def get_delay_time(self):
        try:
            days = int(self.entry_days.get())
            hours = int(self.entry_hours.get())
            minutes = int(self.entry_minutes.get())
            seconds = int(self.entry_seconds.get())

            if days < 0 or hours < 0 or minutes < 0 or seconds < 0:
                messagebox.showerror(
                    "Error", "All values must be non-negative.")
                return None

            total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds
            return total_seconds
        except ValueError:
            messagebox.showerror(
                "Error", "Invalid input. Please enter numeric values.")
            return None

    def schedule_notification(self):
        delay = self.get_delay_time()
        if delay is None:
            return

        self.button_set.config(state=tk.DISABLED)
        notification_thread = Thread(
            target=self._wait_and_notify, args=(delay,))
        notification_thread.start()

    def _wait_and_notify(self, delay):
        while delay > 0:
            time.sleep(1)
            delay -= 1

            delta = timedelta(seconds=delay)
            time_left = f"{delta.days} days, {delta.seconds // 3600:02d}:{(delta.seconds % 3600) // 60:02d}:{delta.seconds % 60:02d}"
            self.label_time_left.config(text=f"Time left: {time_left}")
            self.update()

        self.show_notification()
        self.button_set.config(state=tk.NORMAL)


if __name__ == "__main__":
    app = NotificationApp()
    app.mainloop()
