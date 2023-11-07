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
            print("heihh")
    def run(self):
        self.player()
if __name__ == "__main__":
    Music(3).start()