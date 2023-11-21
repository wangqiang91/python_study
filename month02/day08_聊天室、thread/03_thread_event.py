from threading import Thread,Event
from time import sleep
msg = None
e = Event()
def yzr():
    print("helloya")
    global msg
    sleep(0.1)
    msg = "test"
    e.set()  #解除下面的阻塞
t = Thread(target=yzr)
t.start()
print("请说出口号")
e.wait()  #阻塞，等待通知；
if msg == "test":
    print("对啦")
else:
    print("错误啦")
t.join()