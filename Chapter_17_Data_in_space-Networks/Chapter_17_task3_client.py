#3
import xmlrpc.client


proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
hi = 'hi'
result = proxy.time_now(hi)
print("It's %s" % result)