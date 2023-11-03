"""
    进程创建
"""

import multiprocessing as mp
from  time  import sleep

def func():
    print("开始执行一个任务")
    sleep(3)
    print("执行任务结束")
# 实例化进程对象
process = mp.Process(target=func)
# 启动进程，执行func
process.start()
