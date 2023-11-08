"""
    进程间通信
"""
from  multiprocessing import Process,Queue
import sys

def  handle(q,x,y):
    while True:
        cmd = q.get()
        if cmd == "+":
            print(f"{x} + {y} = {x+y}")
        elif cmd == "-":
            print("%d - %d = %d"%(x,y,x-y))
        else:
            sys.exit("子进程结束")
if __name__ == "__main__":
    q = Queue()
    p = Process(target=handle,args=(q,4,7))
    p.start()
    while True:
        cmd = input(">>")
        if not cmd:
            break
        q.put(cmd)

