from socket import *
answer_dict = {"你好":"你也好呀","几岁":"我两岁啦","男女":"我是男宝宝"}
def chat(conn,addr):
    data = conn.recv(1024)
    print(f"收到{addr}问题：",data.decode())
    for item in answer_dict.keys():
        if (data.decode() in item) or (item in data.decode()):
            conn.send(f"回答：{answer_dict[item]}".encode())
            break
    else:
        conn.send("我还太小了，不知道答案".encode())
def main():
    tcp_serv = socket()
    tcp_serv.bind(("0.0.0.0",8881))
    tcp_serv.listen(5)
    while True:
        conn,addr = tcp_serv.accept()
        chat(conn,addr)
        conn.close()
main()
