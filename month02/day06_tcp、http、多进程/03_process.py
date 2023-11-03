import multiprocessing as mp
from  time  import sleep
print("============")
def func():
    print("开始执行一个任务")
    sleep(3)
    print("执行任务结束")
# 实例化进程对象

# 启动进程，执行func
# process.start()

if __name__ == '__main__':
    process = mp.Process(target=func)
    process.start()
    print("又开始执行一个任务")
    sleep(4)
    print("又执行任务结束")




