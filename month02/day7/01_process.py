from  multiprocessing import Process
from time import sleep

def worker(sec,name):
    for i in range(3):
        print("i am %s"%name)
        sleep(sec)
if __name__ == "__main__":
    # 两种传参方式
    # p = Process(target=worker,args=(2,"jerry"))
    p = Process(target=worker,kwargs={"name":"jerry","sec":2})
    p.start()