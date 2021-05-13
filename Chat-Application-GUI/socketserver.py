import socket
import threading

HOST = '127.0.0.1'
PORT=9999

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen()

clients=[]
names=[]

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handle(client):
    while True:
        try:
            msg=client.recv(1024)
            print(f'{names[clients.index(client)]} says {msg}')
            broadcast(msg)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            name=names[index]
            names.remove(name)
            break

def receive():
    while True:
        client, address=server.accept()
        print(f'Connected with {str(address)}')

        client.send('NAME'.encode('utf-8'))
        name=client.recv(1024)

        names.append(name)
        clients.append(client)

        print(f'Client connected is {name}')
        broadcast(f'{name} connected to server'.encode('utf-8'))
        client.send('Connected to server'.encode('utf-8'))

        thread=threading.Thread(target=handle,args=(client,))
        thread.start()


receive()