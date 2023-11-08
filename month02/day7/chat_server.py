"""
    name:ahuan
    email:xx@xx.cn
    data:20231107
    群聊聊天室服务端
"""
from socket import *
ADDR = ("0.0.0.0",8888)
name_dict = {}
def login(udp_server,addr,name):
    if name not in name_dict:
        udp_server.sendto(b"ok",addr)
        msg = "欢迎%s加入群聊"%name
        for key,value in name_dict.items():
            udp_server.sendto(msg.encode(),value)
        name_dict[name] = addr
        print(name_dict)
    else:
        udp_server.sendto(b"fail",addr)   
    
def chat():
    pass
def quit():
    pass
def main():
    udp_server = socket(AF_INET,SOCK_DGRAM)
    udp_server.bind(ADDR)
    while True:
        request,addr = udp_server.recvfrom(1024)
        data = request.decode().split(" ")
        if data[0] == "login":
            login(udp_server,addr,data[1])
        elif request == "聊天":
            chat()
        elif request == "退出":
            quit()
if __name__ == "__main__":
    main()  