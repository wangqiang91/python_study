"""
    基于多进程的并发网络模型
"""
from multiprocessing import Process
from socket import *
host = "0.0.0.0"
port = 8880
ADDR = (host,port)
def handle(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode())
        conn.send(b"test")
    conn.close()
def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    #循环等待客户端链接
    while True:
        try:
            conn,addr = sock.accept()
            print("connect from:",addr)
        except KeyboardInterrupt:
            sock.close()
            break
        # 为链接进来的客户端创建进程,daemon=True设置主线结束，分支线随之结束；
        p = Process(target=handle,args=(conn,),daemon=True)
        p.start()
if __name__ == "__main__":
    main()