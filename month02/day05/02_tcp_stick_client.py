from  socket import *
from time import sleep
tcp_client = socket()
tcp_client.connect(("127.0.0.1",8880))
data = ["qq","ww","ee","rr","tt"]
for item in data:
    tcp_client.send(item.encode())
sleep(0.1)
tcp_client.send("##".encode())
tcp_client.close()