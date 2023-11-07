import multiprocessing as mp
from  time  import sleep
print("============")
def func():
    print("开始执行一个任务")
    sleep(5)
    print("执行任务结束")
# 实例化进程对象

# 启动进程，执行func
# process.start()

if __name__ == '__main__':
    # daemon = True,子进程随父进程结束而结束；
    process = mp.Process(target=func,daemon=True)
    process.start()
    print("又开始执行一个任务")
    sleep(2)
    print("又执行任务结束")




