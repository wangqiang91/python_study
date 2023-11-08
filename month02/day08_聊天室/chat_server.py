"""
    name:ahuan
    email:xx@xx.cn
    data:20231107
    群聊聊天室服务端
"""
from socket import *
from multiprocessing import *
ADDR = ("0.0.0.0",8888)
name_dict = {}
def login(udp_server,addr,name):
    """
    判断用户名是否重复,不重复则允许用户加入群聊并把用户信息加入到name_dict中;
    """
    if name not in name_dict:
        udp_server.sendto(b"ok",addr)
        msg = "欢迎%s加入群聊"%name
        for key,value in name_dict.items():
            udp_server.sendto(msg.encode(),value)
        name_dict[name] = addr
        print(name_dict)
    else:
        udp_server.sendto(b"fail",addr)   
    
def chat(sock,name,message):
    msg = "%s : %s"%(name,message)
    for key,value in name_dict.items():
        if name != key:
            sock.sendto(msg.encode(),value)
def quit():
    pass
def do_request(udp_server):
    while True:
        request,addr = udp_server.recvfrom(1024)
        data = request.decode().split(" ")
        if data[0] == "login":
            login(udp_server,addr,data[1])
        elif data[0] == "chat":
            chat(udp_server,data[1],data[2])
        elif request == "退出":
            quit()
def main():
    udp_server = socket(AF_INET,SOCK_DGRAM)
    udp_server.bind(ADDR)
    p = Process(target=do_request,args=(udp_server,))
    p.start()
    
if __name__ == "__main__":
    main()  