from socket import *
from threading import Thread

def handle_client(client: socket,addr):
    request = None
    client.send((str(addr)+'\n'*2).encode())
    while request != "close":
        request = client.recv(15).decode()
        response = str(request.upper()) + '\n'
        client.send(response.encode())

    client.close()



serverPort = 2222
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(20)

try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        Thread(target=handle_client, args=(connectionSocket,addr,)).start()
except KeyboardInterrupt:
    serverSocket.close()    
