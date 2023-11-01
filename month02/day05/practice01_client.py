from socket import *
from time import sleep
def read_image(tcp_client):
    img = open(r"C:\Users\Administrator\Pictures\微信图片_20220920152942.jpg","rb")
    while True:
        data = img.read(2048)
        if not data:
            sleep(0.1)
            tcp_client.send(b"##")
            break 
        tcp_client.send(data)
    img.close()
def main():
    tcp_client = socket()
    tcp_client.connect(("127.0.0.1",8887))
    read_image(tcp_client)
    print(tcp_client.recv(1024).decode())
    tcp_client.close()
main()


