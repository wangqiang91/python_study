from socket import *
from multiprocessing import Process
ADDR = ("127.0.0.1",8888)
def login(sock):
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
    while True:
        message = input("请输入消息")
        if not message:
            continue
        if message == "quit":
            break
        request = "chat " + name + " " + message 
        sock.sendto(request.encode(),ADDR)
        # rev,addr = sock.recvfrom(1024)

def quit():
    pass
def main():
    sock = socket(AF_INET,SOCK_DGRAM)
    name = login(sock)
    chat(sock,name)
    quit()
if __name__ == "__main__":
    main()