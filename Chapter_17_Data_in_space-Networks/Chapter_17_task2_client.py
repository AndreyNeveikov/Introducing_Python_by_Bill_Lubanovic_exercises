#2
import zmq


host = '127.0.0.1'
port = 6789
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://%s:%s" % (host, port))
print("Client started")

while True:
    client.send(b"hi")
    reply = client.recv()
    print("Server send %s" % reply)

