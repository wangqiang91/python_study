"""
    基于多线程的网络并发模型
"""

from threading import Thread
from socket import *
class Handle(Thread):
    def __init__(self,conn):
        self.conn = conn
        super().__init__()
    def run(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            print(data.decode())
            self.conn.send(b"test")
        self.conn.close()
class TcpServer(Thread):
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
    tt = TcpServer(host="0.0.0.0",port=8881)
    tt.main()
