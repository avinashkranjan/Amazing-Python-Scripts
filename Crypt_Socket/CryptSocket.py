import ssl
import socket

# Server information
server_host = 'example.com'
server_port = 443

# Create an SSL context
ssl_context = ssl.create_default_context()

# Verify the server's certificate
ssl_context.verify_mode = ssl.CERT_REQUIRED
ssl_context.check_hostname = True
ssl_context.load_default_certs()

try:
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the socket with the SSL context
    ssl_sock = ssl_context.wrap_socket(sock, server_hostname=server_host)

    # Connect to the server
    ssl_sock.connect((server_host, server_port))
    print("Connected to the server.")

    # Send data to the server
    ssl_sock.send(b"Hello, server!")

    # Receive data from the server
    response = ssl_sock.recv(4096)
    print("Received:", response.decode())

except ssl.SSLError as e:
    print("SSL/TLS connection error:", str(e))

except socket.error as e:
    print("Socket error:", str(e))

finally:
    # Close the connection
    ssl_sock.close()
