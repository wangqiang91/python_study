"""
    复制客户端传输过来的内容到指定位置；
"""
from socket import *

def file_dispose(conn):
    img_write = open(r"month02\day05\20231030.jpeg","wb")
    while True:
        data = conn.recv(1024)
        if not data or data == b"##":
            break
        img_write.write(data)
    img_write.close()
def main():
    tcp_server = socket()
    tcp_server.bind(("0.0.0.0",8887))
    tcp_server.listen(5)
    print("等待连接")
    conn,addr = tcp_server.accept()
    file_dispose(conn)
    conn.send("上传成功".encode())
    conn.close()
    tcp_server.close()

main()
    


    