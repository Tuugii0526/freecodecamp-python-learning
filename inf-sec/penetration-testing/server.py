#!user/bin/env python3
import socket 
serversocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 3000
serversocket.bind(('127.0.0.1',port))
serversocket.listen(3)
while True:
    clientsocket,address=serversocket.accept()
    print(f"received connection from {address}")
    message="thank you for connecting to the server"
    clientsocket.send(message.encode("ascii"))
    clientsocket.close()
    