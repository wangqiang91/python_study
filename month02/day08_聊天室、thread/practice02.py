from threading import Thread,Lock
lock1 = Lock()
lock2 = Lock()
def print_num():
    for i in range(1,53,2):
        lock1.acquire()
        print(i)
        print(i+1)
        lock2.release()
def print_alph():
    for i in range(65,91):
        lock2.acquire()
        print(chr(i))
        lock1.release()

n = Thread(target=print_num)
a = Thread(target=print_alph)
lock2.acquire()
n.start()
a.start()
n.join()
a.join()


