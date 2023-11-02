from  socket import *
import os
class Handle:
    def __init__(self,filedir = r"month02\day06_tcp、http\static"):
        self.filedir = filedir
    def handle(self,conn):
        data = conn.recv(2048).decode()
        if data:
            info = data.split(" ")[1]
        print(info)
        self.send_response(conn,info)
    def send_response(self,conn,info):
        if info == "/":
            info = "/index.html"
        try:
            data = open(self.filedir + info,"rb")
        except:
            response = b"HTTP/1.1 404 NOT FOUND \r\n" + b"Content-Type:text/html\r\n" + b"\r\n" + b"not found"
        else:
            response = b"HTTP/1.1 200 OK \r\n" + b"Content-Type:text/html\r\n" + b"\r\n" + data.read()
        finally:
            conn.send(response)

class HttpServer:
    def __init__(self,tcp_ip="0.0.0.0",tcp_port=8884):
        self.tcp_ip = tcp_ip
        self.tcp_port = tcp_port
        self.tcp_s = self.tcp_server()
        self.handle = Handle()
    def tcp_server(self):
        tcp_ser = socket()
        tcp_ser.bind((self.tcp_ip,self.tcp_port))
        return tcp_ser
    def start(self):
        self.tcp_s.listen(5)
        while True:
            conn,addr = self.tcp_s.accept()
            self.handle.handle(conn)
            conn.close()


if __name__ == "__main__":
    HttpServer().start()
    # Handle().send_response(1,2)