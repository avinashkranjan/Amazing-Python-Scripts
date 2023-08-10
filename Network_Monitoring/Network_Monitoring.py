import ping3
import time


def ping_servers(server_list):
    while True:
        for server in server_list:
            response_time = ping3.ping(server)
            if response_time is not None:
                print(f"{server} is up (Response Time: {response_time} ms)")
            else:
                print(f"{server} is down! ALERT!")

        time.sleep(60)  # Ping every 60 seconds


if __name__ == "__main__":
    servers_to_monitor = ["google.com", "example.com", "localhost"]

    print("Network Monitoring Script")
    print("Press Ctrl+C to stop monitoring")

    try:
        ping_servers(servers_to_monitor)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
