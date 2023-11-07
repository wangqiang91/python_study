from multiprocessing import Process
import os

class FileCopy():
    def __init__(self):
        self.file = r"month02\day7\file\\"
        self.copyto_file = r"month02\day7\copy_file\\"
        # super().__init__()
    def getdir(self):
        dirs = os.listdir(self.file)
        return dirs
    def copy_data(self,filename):
        f = open(self.file + filename,"rb")
        w = open(self.copyto_file + filename,"wb")
        while True:
            data = f.read(1024)
            if not data:
                break
            w.write(data)
        f.close()
        w.close()
    def main(self):
        process_list = []
        for item in self.getdir():
            pro = Process(target=self.copy_data,kwargs={"filename":item})
            process_list.append(pro)
            pro.start()
        for process in process_list:
            process.join()
        print("复制完成")
if __name__ == "__main__":
    FileCopy().main()