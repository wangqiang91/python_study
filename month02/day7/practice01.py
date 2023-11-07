from multiprocessing import Process
from time import sleep
import os
class split_file:
    def __init__(self,file = r"month02\day7\file\20231030.jpeg"):
        self.file = file
        self.size = os.path.getsize(self.file)
    def up_file(self):
        f = open(self.file,"rb")
        w = open(r"month02\day7\file\20231030_up.jpeg","wb")
        n = self.size // 2
        while n >= 1024:
            w.write(f.read(1024))
            n = n - 1024
        w.write(f.read(n))
        f.close()
        w.close()
    def down_file(self):
        f = open(self.file,"rb")
        w = open(r"month02\day7\file\20231030_down.jpeg","wb")
        f.seek(self.size//2)
        while True:
            data = f.read(1024)
            if not data:
                break
            w.write(data)
        f.close()
        w.close()

    def main(self):
        process_list = []
        for item in [self.up_file,self.down_file]:
            pro = Process(target=item)
            process_list.append(pro)
            pro.start()
        for process in process_list:
            process.join()
        print("分割完成")
if __name__ == "__main__":
    split_file().main()