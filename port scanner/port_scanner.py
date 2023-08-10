import sys
import socket
import argparse
from datetime import datetime

def scan_ports(target, ports):
    open_ports = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports



def main():
    parser = argparse.ArgumentParser(description="Simple port scanner.")
    parser.add_argument("target", help="Target IP address to scan.")
    parser.add_argument("-p", "--ports", type=str, default="1-100", help="Port range to scan (e.g., '1-100').")
    args = parser.parse_args()

    target = socket.gethostbyname(args.target)
    port_range = args.ports.split("-")
    start_port = int(port_range[0])
    end_port = int(port_range[1])

    print(f"Scanning Target: {target}")
    print(f"Scanning started at: {datetime.now()}")
    print("-" * 50)

    try:
        open_ports = scan_ports(target, range(start_port, end_port + 1))
        if open_ports:
            print("Open Ports:")
            for port in open_ports:
                print(f"Port {port} is open")
        else:
            print("No open ports found in the specified range.")
    except KeyboardInterrupt:
        print("\nExiting Program!")
        sys.exit()
    except socket.gaierror:
        print("Hostname Could Not Be Resolved!")
        sys.exit()
    except socket.error:
        print("Server not responding!")
        sys.exit()

if __name__ == "__main__":
    main()
