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
        msg = "\n" + "欢迎%s加入群聊"%name + "\n"
        for key,value in name_dict.items():
            udp_server.sendto(msg.encode(),value)
        name_dict[name] = addr
        print(name_dict)
    else:
        udp_server.sendto(b"fail",addr)   
    
def chat(sock,name,message):
    """
    父进程，把某一用户的消息发送给其他用户；
    """
    msg ="\n" + "%s : %s"%(name,message) + "\n"
    for key,value in name_dict.items():
        if name != key:
            sock.sendto(msg.encode(),value)
def quit(sock,name):
    """
    退出群聊并通知其他用户，并删除用户信息
    """
    if name in name_dict:
        del name_dict[name]
    msg = "%s 退出了聊天室"%name
    for key,value in name_dict.items():
        sock.sendto(msg.encode(),value)
def do_request(udp_server):
    """
    子进程，接收消息，并做对应处理
    """
    while True:
        request,addr = udp_server.recvfrom(1024)
        data = request.decode().split(" ",2)
        if data[0] == "login":
            login(udp_server,addr,data[1])
        elif data[0] == "chat":
            chat(udp_server,data[1],data[2])
        elif data[0] == "quit":
            quit(udp_server,data[1])
        else:
            print("消息有误")
def main():
    udp_server = socket(AF_INET,SOCK_DGRAM)
    udp_server.bind(ADDR)
    p = Process(target=do_request,args=(udp_server,))
    p.start()
    while True:
        """父进程，以管理员给全部成员发送消息，给到子进程"""
        message = input("superman:")
        if not message:
            break
        msg = "chat superman " + message
        udp_server.sendto(msg.encode(),ADDR)

if __name__ == "__main__":
    main()  