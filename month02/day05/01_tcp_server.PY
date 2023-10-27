from socket import *

tcp_socket = socket(AF_INET,SOCK_STREAM)
tcp_socket.bind(("0.0.0.0",8888))
tcp_socket.listen(5)
print("等待连接")
conn,addr = tcp_socket.accept()
print("connect from",addr)
data = conn.recv(1024)
print("收到",data.decode())
conn.send(b"thanks")

conn.close()
tcp_socket.close()