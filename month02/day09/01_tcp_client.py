from socket import *
client = socket()
client.connect(("127.0.0.1",8881))
while True:
    msg = input(">>")
    client.send(msg.encode())
    if not msg:
        break
    data = client.recv(1024)
    print(data.decode())
client.close()