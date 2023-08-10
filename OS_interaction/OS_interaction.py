import psutil
import time
import os


def monitor_cpu_threshold(threshold):
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"Current CPU Usage: {cpu_percent}%")

        if cpu_percent > threshold:
            print("CPU usage exceeds threshold!")
            # You can add more actions here, such as sending an email or notification.
            # For simplicity, we'll just print an alert message.
            # macOS command to speak the message
            os.system("say 'High CPU usage detected!'")

        time.sleep(10)  # Wait for 10 seconds before checking again


if __name__ == "__main__":
    threshold_percent = 80  # Define the CPU usage threshold in percentage
    monitor_cpu_threshold(threshold_percent)
