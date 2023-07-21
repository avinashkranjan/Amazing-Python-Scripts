import time
from plyer import notification


def drink_water_reminder():
    """Sends a notification to the user to drink water."""
    title = "Drink Water Reminder"
    message = "It's time to drink some water!"
    notification.notify(title, message)


def main():
    """Runs the drink water reminder function every hour."""
    while True:
        time.sleep(1200)
        drink_water_reminder()


if __name__ == "__main__":
    main()
