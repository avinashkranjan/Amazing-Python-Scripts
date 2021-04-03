import socket
import threading

host = "127.0.0.1"
port = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()

nicknames = []
clients = []


def broadcast(message):
    '''
    This function will send the data from our local server to the clients
    '''
    for client in clients:
        client.send(message)


def handle(client):
    '''
    This fuction will handle the client connect and transmit data/message
    '''
    while True:
        try:
            message = client.recv(1024)  # reciving client's message
            print(f'{nicknames[clients.index(client)]} says {message}')
            broadcast(message)
        except BaseException:
            # fetching the index of the client from the clients list
            index = clients.index(client)
            clients.remove(client)  # Removing client from client list
            client.close()  # Closing Client's connection with our server
            nickname = nicknames[index]  # Fectching nickname of the client
            # Removing nickname form the the nickname list
            nicknames.remove(nickname)
            break


def Receive():
    while True:
        client, address = server.accept()           # gets server address
        print(f"Connected to {str(address)}")

        # sending encoded message to ask nickname
        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024)  # recieving nick name eith 1024 bytes

        nicknames.append(nickname)  # updating nicknames list
        clients.append(client)  # updating clients list

        print(f"Nickname of the client is {nickname}")
        broadcast(f"Welcome {nickname} you are connected to the server!!\n".encode(
            'utf-8'))  # Broadcasting to everyone
        # sending msg to a perticular connected client
        client.send("connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))      
        thread.start()


print("Server Status : Running ...")
Receive()
