"""
    多进程
"""
from multiprocessing import Process
from time import sleep
import os

def thing(sec,do_thing):
    sleep(sec)
    print(do_thing)
    print(os.getppid(),"==>",os.getpid())
# def thing2():
#     sleep(2)
#     print("do thing2")
#     print(os.getpid(),"==>",os.getppid())
# def thing3():
#     sleep(3)
#     print("do thing3")
#     print(os.getpid(),"==>",os.getppid())
if __name__ == "__main__":
    process_list = []
    for item in [(4,"thing1"),(2,"thing2"),(3,"thing3")]:
        pro = Process(target=thing,args=(item))
        process_list.append(pro)
        pro.start()
    for process in process_list:
        process.join()
    print("全部进程都执行完了")