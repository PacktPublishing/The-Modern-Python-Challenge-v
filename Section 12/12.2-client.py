# client

import socket

HOST = '127.0.0.1'
PORT = 2001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

packet = client.recv(1024)
print(packet.decode('utf-8'))






