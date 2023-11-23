"""
    基于多线程的网络并发模型
"""

import os
from threading import Thread
from socket import *
from time import sleep
FTP = r"E:\test\\"
class Handle(Thread):
    def __init__(self,conn):
        self.conn = conn
        super().__init__()
    def run(self):
        while True:
            request = self.conn.recv(1024).decode().split(" ",1)
            if request[0] == "list":
                self.do_list()
            elif request[0] == "get":
                self.do_get(request[1])
            elif request[0] == "put":
                filename = request[1].split("\\")[-1]
                self.do_put(filename)
            elif request[0] == "quit" or not request:
                break
        self.conn.close()
    def do_list(self):
        data = os.listdir(FTP)
        if data:
            self.conn.send(b"ok")
            data_str = "  ".join(data)
            sleep(0.1)
            self.conn.send(data_str.encode())
        else:
            self.conn.send(b"empty")
    def do_get(self,filename):
        try:
            fr = open(FTP + filename,"rb")
            self.conn.send(b"ok")
            sleep(0.1)
            while True:
                data = fr.read(1024)
                if not data:
                    break
                self.conn.send(data)
            fr.close()
            sleep(0.1)
            self.conn.send(b"##")
        except:
            self.conn.send(b"fail")
    def do_put(self,filename):
        if os.path.exists(FTP + filename):
            self.conn.send(b"exists")
        else:
            self.conn.send(b"ok")
            fr = open(FTP + filename,"wb")
            while True:
                data = self.conn.recv(1024)
                if data == b"##":
                    break
                fr.write(data)
            fr.close()

class FtpServer(Thread):
    def __init__(self,*,host="",port=0):
        self.host = host
        self.port = port
        self.ADDR = (self.host,self.port)
        self.sock = self._creat_socket()
    def _creat_socket(self):
        sock = socket()
        sock.bind(self.ADDR)
        return sock
    def main(self):
        self.sock.listen(5)
        while True:
            conn,addr = self.sock.accept()
            print("connect from :",addr)
            # t = Thread(target=self.handle,args=(conn,))
            t = Handle(conn)
            t.start()

if __name__ == "__main__":
    tt = FtpServer(host="0.0.0.0",port=8882)
    tt.main()
