from threading import Lock,Thread

a = b = 1
lock = Lock()
def value():
    while True:
        lock.acquire()  #上锁
        if a != b:
            print(f"a={a},b={b}")
        lock.release()
t = Thread(target=value)
t.start()
while True:
    lock.acquire()
    a += 1
    b += 1
    lock.release()