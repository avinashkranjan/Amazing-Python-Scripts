import socket
import subprocess
import sys
import asyncio
from datetime import datetime

subprocess.call('cls', shell=True)

# Ask for input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()


async def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    try:
        await asyncio.wait_for(
            asyncio.get_event_loop().sock_connect(sock, (remoteServerIP, port)),
            timeout=1
        )
        print("Port {}: Open".format(port))
    except (socket.timeout, ConnectionRefusedError):
        pass
    finally:
        sock.close()


async def main():
    tasks = []
    for port in range(1, 1025):
        tasks.append(scan_port(port))
    await asyncio.gather(*tasks)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

print('Scanning Completed in:', total)
