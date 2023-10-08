from socket import *

class QueryWord:
    def __init__(self,host="0.0.0.0",port=8888):
        self.host = host
        self.port = port 
        self.sock = self.creat_sock()
        self.fr = open("D:\github_project\python_study\month02\day03\dict.txt","r")
    def creat_sock(self):
        sock = socket(AF_INET,SOCK_DGRAM)
        sock.bind((self.host,self.port))
        return sock
    def query_word(self):
        while True:
            word,addr = self.sock.recvfrom(1024)
            # if data == b"##":
            #     break
            sent_content = self.find_line(word.decode())
            print(addr,":",word.decode())
            self.sock.sendto(sent_content.encode(),addr)
    def find_line(self,word):
        self.fr.seek(0)  #注意偏移量，不然会从上次查询结束开始查起；
        for line in self.fr:
            list_line = line.split(" ")
            if list_line[0] > word:
                break
            if word == list_line[0]:
                return line
        return "not find"
    def colse(self):
        self.fr.close()
        self.sock.close()
if __name__ == "__main__":
    QueryWord().query_word()



