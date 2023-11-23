"""
month01-day13:商品管理系统；
month02-day03:学生管理系统,数据存储到txt文件中;
month02-day08:聊天室,运用udp和多进程,创建聊天功能，多进程网络并发；
month02-day09:ftp文件传输,运用tcp和多线程,创建文件传输功能，多线程网络并发；
"""

def n01_find_number():
    for i in range(2000,3201):
        if i % 7 == 0 and i % 5 != 0:
            print(i,end=",")

def n02_factorial():
    num = int(input())
    fac = 1
    for i in range(1,num+1):
        fac = fac * i
    print(fac)


if __name__ == "__main__":
    n02_factorial()
