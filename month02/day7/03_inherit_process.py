"""
    继承进程
"""

from time  import sleep
from multiprocessing import Process
class Music(Process):
    def __init__(self,value):
        self.value = value
        super().__init__()
    def player(self):
        for i in range(self.value):
            sleep(2)
            print(i)
    def run(self):
        self.player()
if __name__ == "__main__":
    for i in range(1,10,3):
        Music(i+3).start()