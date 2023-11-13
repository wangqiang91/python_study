import os
from threading import Thread
from time import sleep
a = 1
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放音乐01")
    global a
    print("a:",a)
    a = 10000
t = Thread(target=music)
t.start()
for i in range(4):
        sleep(1)
        print(os.getpid(),"播放音乐02")
t.join()
print("a的最终值：",a)

# 视频看到1231pm  未开始观看
