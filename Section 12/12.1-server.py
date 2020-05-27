import socket

HOST = '127.0.0.1'
PORT = 2001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

while True:
    clientsocket, address = server.accept()
    print(f"connected to client on {address}")
    clientsocket.send("This is a test server".encode("utf-8"))

server.shutdown()
server.close()    