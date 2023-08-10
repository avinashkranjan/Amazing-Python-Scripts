import socket

hostname = input("Enter the URL: ")

try:
    ip_address = socket.gethostbyname(hostname)
    print(ip_address)
except:
    print('Invalid URL')
