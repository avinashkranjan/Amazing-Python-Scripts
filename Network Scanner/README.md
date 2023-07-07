# Network Scanner

This is a simple Python script that uses the Scapy library to scan the local network and find connected devices.

## Usage

1. Install the Scapy library. You can install it using pip:

   ```shell
   pip install scapy

2. Run the script by executing the following command:

   ```shell
   python network-scanner.py

3. When prompted, enter the target IP address or IP range in the format "ip_address/24". For example, "192.168.1.0/24".

4. The script will send ARP requests to the specified IP range and display the list of available devices along with their IP and MAC addresses.
