# import socket library 
import socket 

# import threading library 
import threading 

# Choose a port that is free 
PORT = 5000

# An IPv4 address is obtained 
# for the server. 
SERVER = socket.gethostbyname(socket.gethostname()) 

# Address is stored as a tuple 
ADDRESS = (SERVER, PORT) 

# the format in which encoding 
# and decoding will occur 
FORMAT = "utf-8"

# Lists that will contains 
# all the clients connected to 
# the server and their names. 
clients, names = [], [] 

# Create a new socket for 
# the server 
server = socket.socket(socket.AF_INET, 
					socket.SOCK_STREAM) 

# bind the address of the 
# server to the socket 
server.bind(ADDRESS) 

# function to start the connection 
def startChat(): 
	
	print("server is working on " + SERVER) 
	
	# listening for connections 
	server.listen() 
	
	while True: 
		
		# accept connections and returns 
		# a new connection to the client 
		# and the address bound to it 
		conn, addr = server.accept() 
		conn.send("NAME".encode(FORMAT)) 
		
		# 1024 represents the max amount 
		# of data that can be received (bytes) 
		name = conn.recv(1024).decode(FORMAT) 
		
		# append the name and client 
		# to the respective list 
		names.append(name) 
		clients.append(conn) 
		
		print(f"Name is :{name}") 
		
		# broadcast message 
		broadcastMessage(f"{name} has joined the chat!".encode(FORMAT)) 
		
		conn.send('Connection successful!'.encode(FORMAT)) 
		
		# Start the handling thread 
		thread = threading.Thread(target = handle, 
								args = (conn, addr)) 
		thread.start() 
		
		# no. of clients connected 
		# to the server 
		print(f"active connections {threading.activeCount()-1}") 

# method to handle the 
# incoming messages 
def handle(conn, addr): 
	
	print(f"new connection {addr}") 
	connected = True
	
	while connected: 
		# recieve message 
		message = conn.recv(1024) 
		
		# broadcast message 
		broadcastMessage(message) 
	
	# close the connection 
	conn.close() 

# method for broadcasting 
# messages to the each clients 
def broadcastMessage(message): 
	for client in clients: 
		client.send(message) 

# call the method to 
# begin the communication 
startChat() 
