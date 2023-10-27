from socket import *
tcp_client = socket()
addr_server = ("127.0.0.1",8888)
tcp_client.connect(addr_server)
msg = input(">>")
tcp_client.send(msg.encode())
data = tcp_client.recv(1024)
print("from server",data.decode())
tcp_client.close()