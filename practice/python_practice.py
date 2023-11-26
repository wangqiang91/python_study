"""
month01-day13:商品管理系统；
month02-day03:学生管理系统,数据存储到txt文件中;
month02-day08:聊天室,运用udp和多进程,创建聊天功能，多进程网络并发；
month02-day09:ftp文件传输,运用tcp和多线程,创建文件传输功能，多线程网络并发；
"""
# https://blog.csdn.net/weixin_40547993/article/details/88928075
import re

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

def n03():
    num = int(input())
    print({i:i*i for i in range(1,num+1)})

def n04():
    data = input()
    list1 = data.split(",")
    res_list = []
    for item in list1:
        res = re.sub(r"\D","",item)
        res_list.append(res)
    print(res_list)
    print(tuple(res_list))

class Print_05:
    def __init__(self):
        self.input_str = self.getString()
    def getString(self):
        data = input(">>")
        return data
    def printString(self):
        print(self.input_str.upper())

def n06():
    num_list = input(">>").split(",")
    for D in range(0,len(num_list)):
        Q = (2 * 50 * float(num_list[D]) / 30) ** 0.5 
        if D == len(num_list)-1:
            print(round(Q))
            return
        print(round(Q),end=",")

def n07():
    data_list = input(">>").split(",")
    i = int(data_list[0])
    j = int(data_list[1])
    response = []
    for x in range(0,i):
        list1 = []
        for y in range(0,j):
            list1.append(x * y)
        response.append(list1)
    print(response)
    
# 接收一个逗号分割的单词序列作为输入，按字母顺序排序后按逗号分割打印。
def n08():
    data = input(">>").split(",")
    data.sort()
    print(",".join(data))

#接收一个序列，将元素大写后输出；
def n09():
    data_list = []
    while True:
        data = input(">>")
        if not data:
            break
        data_list.append(data.upper())
    print('\n'.join(data_list))

#输入空格分割的单词，删除重复的单词后，按a-z排序后以空格分割打印单词；
def n10():
    data = input(">>").split(" ")
    data = list(set(data))
    print(" ".join(sorted(data)))
    
if __name__ == "__main__":
    n10()
