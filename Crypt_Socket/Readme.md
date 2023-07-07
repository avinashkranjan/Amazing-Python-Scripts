# Secure Encrypted Socket Connection using SSL/TLS

This code demonstrates how to establish a secure encrypted socket connection to a server using SSL/TLS in Python.

## Description

The script establishes a secure encrypted socket connection to a server using SSL/TLS. It allows you to communicate securely with the server over a network.

## Features

- Establishes an SSL/TLS encrypted socket connection
- Sends data to the server over the secure connection
- Receives data from the server over the secure connection
- Handles SSL/TLS errors and socket errors gracefully

## Prerequisites

- Python 3.x

## Usage

1. Modify the `server_host` and `server_port` variables in the code to match the hostname and port of the server you want to connect to.
2. Run the Python script using the following command:


## Code Explanation

1. The `ssl` module is imported to provide SSL/TLS functionality.
2. The `socket` module is imported to create a TCP socket.
3. The `server_host` and `server_port` variables hold the hostname and port of the server you want to connect to.
4. A socket is created using `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`.
5. The socket is wrapped with SSL/TLS using `ssl.wrap_socket(sock)`, which returns an SSL/TLS socket object.
6. The SSL/TLS socket is connected to the server using `ssl_sock.connect((server_host, server_port)`.
7. Data can be sent to the server using `ssl_sock.send()`.
8. Data received from the server can be retrieved using `ssl_sock.recv()`.
9. Exceptions related to SSL/TLS errors or socket errors are caught and handled gracefully.
10. Finally, the SSL/TLS socket is closed using `ssl_sock.close()`.


