import socket
clientSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host= socket.gethostname()
port= 3000
clientSocket.connect(('127.0.0.1',port))
message= clientSocket.recv(1024)
clientSocket.close()
print(message.decode('ascii'))