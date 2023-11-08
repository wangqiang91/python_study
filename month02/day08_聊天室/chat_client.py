from socket import *
from multiprocessing import Process
ADDR = ("127.0.0.1",8888)
def login(sock):
    """
        输入用户昵称，并进入聊天室；
    """
    while True:
        name = input("请输入昵称")
        request = "login " + name 
        sock.sendto(request.encode(),ADDR)
        rev,addr = sock.recvfrom(1024)
        if rev == b"ok":
            print("您已进入聊天室")
            return name
        else:
            print("昵称已重复")
def chat(sock,name):
    """
    父进程负责发送消息
    """
    while True:
        message = input("请输入消息")
        if not message:
            continue
        if message == "quit":
            break
        request = "chat " + name + " :" + message 
        sock.sendto(request.encode(),ADDR)     
def recv_msg(sock):
    """
    子进程负责接收消息
    """
    while True:
        data,addr = sock.recvfrom(1024)
        print(data.decode(),end="\n")
def quit():
    pass
def main():
    sock = socket(AF_INET,SOCK_DGRAM)
    name = login(sock)
    p = Process(target=recv_msg,args=(sock,),daemon=True)
    p.start()
    chat(sock,name)
    quit()
if __name__ == "__main__":
    main()