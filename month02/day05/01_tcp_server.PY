from socket import *

tcp_socket = socket(AF_INET,SOCK_STREAM)
tcp_socket.bind(("0.0.0.0",8886))
tcp_socket.listen(5)
while True:
    print("等待连接。。。")
    conn,addr = tcp_socket.accept()
    print("connect from",addr)
    while True:
        data = conn.recv(5)
        if not data or (data.decode() == "##"):
            break
        print("收到",data.decode())
        conn.send(b"thanks")
    conn.close()
tcp_socket.close()