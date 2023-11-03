"""
    http请求、响应,
"""
# 访问网址，返回图片
from socket import *
tcp_ser = socket()
tcp_ser.bind(("0.0.0.0",8883))
tcp_ser.listen(5)
with open(r"month02\day06_tcp、http\20231030.jpeg","rb") as img:
    data = img.read()
while True:
    conn,addr = tcp_ser.accept()
    print(f"接受到{addr}的数据：",conn.recv(1024).decode())
    response = b"HTTP/1.1 200 OK \r\n" + b"Content-Type:image/jpeg\r\n" + b"\r\n" + data
    conn.send(response)
    conn.close()
tcp_ser.close()