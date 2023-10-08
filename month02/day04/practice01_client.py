from  socket import *
udp_sock = socket(type=SOCK_DGRAM)
while True:
    word = input(">>")
    udp_sock.sendto(word.encode(),("127.0.0.1",8888))
    if word == "##":
        break
    data,addre = udp_sock.recvfrom(1024)
    print(data.decode())
udp_sock.close()