#3
from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime


def return_time(hi):
    return datetime.utcnow()


server = SimpleXMLRPCServer(('localhost', 6789))
server.register_function(return_time, "time_now")
server.serve_forever()
