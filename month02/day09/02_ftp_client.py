import sys
from  socket import *
from time import sleep
ADDR = ("127.0.0.1",8882)
class Error_Message:
    def __init__(self):
        self.message = {
            "fail":"文件不存在",
            "file_error":"目标路径不存在",
            "exists":"文件已存在",
            "none":"文件不存在"
        }
class Ftp_Client:
    def __init__(self):
        self.handle = Handle()
    def _client_view(self):
        print("""
        ====================FTP====================
           1.查看文件 2.下载文件 3.上传文件 0.退出
        ===========================================
        """)
    def user_select(self):
        user_sel = input("请输入您的选择：")
        if user_sel == "1":
            print(self.handle.list())
        elif user_sel == "2":
            filename = input("请输入文件名称：")
            self.handle.get(filename)
        elif user_sel == "3":
            filepath = input("请输入文件名称：")
            self.handle.put(filepath)
        elif user_sel == "0":
            self.handle.quit()
        else:
            print("您的输入有误，请重新输入")

    def main(self):
        while True:
            self._client_view()
            self.user_select()
class Handle:
    def __init__(self):
        self.sock = self._connect()
        self.msg = Error_Message()
    def _connect(self):
        sock = socket()
        sock.connect(ADDR)
        return sock
    def list(self):
        self.sock.send(b"list ")
        res = self.sock.recv(1024).decode()
        if res == "ok":
            data = self.sock.recv(1024*1024).decode()
            return data
        else:
            print(self.msg.message.get(res))
    def get(self,filename):
        request = "get " +  filename
        self.sock.send(request.encode())
        res = self.sock.recv(1024).decode()
        if res == "ok":
            f = open(r"F:\GitHub_projects\python_study\month02\day09\file\\" + filename,"wb")
            while True:
                data = self.sock.recv(1024)
                if data == b"##":
                    break
                f.write(data)
            f.close()
        else:
            print(self.msg.message.get(res))
    def put(self,filepath):
        file = r"F:\GitHub_projects\python_study\month02\day09\file\\" + filepath 
        try:
            f = open(file,"rb")
        except:
            print(self.msg.message.get("none"))
            return
        request = "put " + file
        self.sock.send(request.encode())
        res = self.sock.recv(1024).decode()
        if res == "ok":
            while True:
                data = f.read(1024)
                if not data :
                    break
                self.sock.send(data)
            f.close()
            sleep(0.1)
            self.sock.send(b"##")
        else:
            print(self.msg.message.get(res))
    def quit(self):
        self.sock.send(b"quit ")
        self.sock.close()
        sys.exit()
if __name__ == "__main__":
    Ftp_Client().main()