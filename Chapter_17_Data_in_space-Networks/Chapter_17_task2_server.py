#2
from datetime import datetime
import zmq


host = '127.0.0.1'
port = 6789
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://%s:%s" % (host, port))
print("Server started")
while True:
    server.recv()
    reply_str = "Now is: %s" % datetime.utcnow()
    reply_bytes = bytes(reply_str, 'utf-8')
    server.send(reply_bytes)
