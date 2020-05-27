import socket

print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))
print(socket.gethostbyname('google.com'))

"""
Useful Methods
accept -- accepts connection
bind -- socket to address
close -- close socket
connect -- make a connection
listen -- sets number of possible connection
recv -- recv whatever is nin argument
send -- send packet
sendall -- serialized  
"""