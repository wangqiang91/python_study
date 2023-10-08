# udp特点: 可能出现数据丢失的情况，传输简单，实现容易；
# 数据以数据包形式传输；传输效率高；

from socket import *
udp_sock = socket(AF_INET,SOCK_DGRAM)


# 绑定ip
# 方法1：本机测试IP
udp_sock.bind(("172.0.0.1",8888))

# 方法2：本机网络IP
# udp_sock.bind(("192.168.101.10",8888))

# 方法3：自动识别IP
# udp_sock.bind(("0.0.0.0",8888))

# 服务端先收后发
while True:
    data,addr = udp_sock.recvfrom(1024)
    if data == b"##":
        break
    print(addr,":",data.decode())
    udp_sock.sendto(b"thanks",addr)
udp_sock.close()

# def find_word():
#     udp_sock = socket(AF_INET,SOCK_DGRAM)
#     udp_sock.bind(("0.0.0.0",8888))
#     fr = open("D:\github_project\python_study\month02\day03\dict.txt")
#     while True:
#         data,addr = udp_sock.recvfrom(1024)
#         if data == b"##":
#             break
#         fr.seek(0)
#         for line in fr:
#             line_list = line.split(" ",1)
#             if data.decode() == line_list[0]:
#                 return udp_sock.sendto(line.encode(),addr)
#         udp_sock.sendto(b"not find",addr)        
#     # udp_sock.close()
# find_word()