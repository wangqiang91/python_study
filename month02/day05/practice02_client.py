from socket import *

def chat(question):
    tcp_cli = socket()
    tcp_cli.connect(("127.0.0.1",8881))
    tcp_cli.send(question.encode())
    data = tcp_cli.recv(1024).decode()
    tcp_cli.close()
    return data
    
def main():
    while True:
        question = input("请输入问题>>")
        if not question :
            break
        print(chat(question))
main()