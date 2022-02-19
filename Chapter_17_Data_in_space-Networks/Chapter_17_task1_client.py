#1
import socket

address = ('localhost', 6789)
max_size = 1000

print('Client started')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

data = client.recv(max_size)
print('Server send ', data)
client.close()
