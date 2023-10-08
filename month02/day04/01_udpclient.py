from socket import *
# 创建UDP套接字
udp_sock = socket(type=SOCK_DGRAM)
# 先发后收
while True:
    msg = input(">>")
    udp_sock.sendto(msg.encode(),("127.0.0.1",8888))
    if msg == "##":
        break
    data,addr = udp_sock.recvfrom(1024)
    print("收到：",data.decode())
udp_sock.close()
