from threading import  Thread
from time  import  sleep
import time

class MyThread(Thread):
    def __init__(self,song):
        self.song = song
        super().__init__()
    def run(self):
        print(time.time())
        for i in range(3):
            sleep(3)
            print(f"播放歌曲{self.song}")
        print(time.time())
t = MyThread("喜欢你")
t.start()
