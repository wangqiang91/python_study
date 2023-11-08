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
            break
        else:
            print("昵称已重复")
def chat():
    pass
def quit():
    pass
def main():
    sock = socket(AF_INET,SOCK_DGRAM)
    login(sock)
    chat()
    quit()
if __name__ == "__main__":
    main()