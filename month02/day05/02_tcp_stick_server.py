from socket import *
tcp_sock = socket()
tcp_sock.bind(("0.0.0.0",8880))
tcp_sock.listen(5)
print("等待连接")
conn,addr = tcp_sock.accept()
print("已连接：",addr)
while True:
    data = conn.recv(1024)
    if data == b"##":
        break
    print(data.decode())
conn.close()
tcp_sock.close()

