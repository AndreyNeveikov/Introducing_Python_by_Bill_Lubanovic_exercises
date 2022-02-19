#1
from datetime import datetime
import socket


server_address = ('localhost', 6789)

print('Server started. Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen(5)
client, addr = server.accept()

now = str(datetime.utcnow())
data = now.encode('utf-8')
client.sendall(data)
print('Server sent', data)
client.close()
server.close()

