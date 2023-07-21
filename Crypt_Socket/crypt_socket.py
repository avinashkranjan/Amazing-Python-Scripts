import socket
import ssl

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(('localhost', 12345))

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening...')

# Accept a connection from a client
client_socket, client_address = server_socket.accept()

print('Connected to:', client_address)

# Wrap the socket with SSL/TLS encryption
ssl_socket = ssl.wrap_socket(
    client_socket, server_side=True, ssl_version=ssl.PROTOCOL_TLS)

while True:
    # Receive data from the client
    data = ssl_socket.recv(1024)

    # Decode and print the received data
    print('Received:', data.decode())

    # If the client sends 'quit', close the connection
    if data.decode() == 'quit':
        break

# Close the SSL/TLS socket
ssl_socket.close()

# Close the server socket
server_socket.close()
