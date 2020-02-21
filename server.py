
import socket

serverSocket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 444

serverSocket.bind(('192.168.1.255', port))

serverSocket.listen(3)

while True:
    clientSocket, address = serverSocket.accept()
    print("received connection from " % str(address))
    message = 'thank you' + "\r\n"
    client.socket.send(message.encode('ascii'))
    clientSocket.close()