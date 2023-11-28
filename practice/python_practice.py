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

# 输入逗号分割的二进制数，输出可被5整除的二进制数，以逗号分割；
def n11():
    data = input(">>").split(",")
    list_data = []
    for item in data:
        if int(item,2) % 5 == 0:
            list_data.append(item)
    print(",".join(list_data))

def n12():
    values = []
    for i in range(1000, 3001):
        s = str(i)
        if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
            values.append(s)
    print (",".join(values))

def n13():
    str_data = input(">>")
    num = re.findall('[0-9]',str_data)
    alp = re.findall('[a-zA-Z]',str_data)
    print("字母",len(alp))
    print("数字",len(num))

def n14():
    str_data = input(">>")
    lower = re.findall('[a-z]',str_data)
    upper = re.findall('[A-Z]',str_data)
    print("大写实例",len(upper))
    print("小写实例",len(lower))

def n15():
    num = input(">>")
    total = int(num) + int(num*2) + int(num*3) + int(num*4)
    print(total)

def n16():
    data = input(">>").split(",")
    data_list = [x for x in data if int(x) % 2 != 0]
    print(",".join(data_list))

def n17():
    sum = 0
    while True:
        data = input(">>")
        num = data.split(" ")
        if not data :
            break
        if num[0] == "D":
            sum += int(num[1])
        else:
            sum -= int(num[1])
    print(sum)

def n18():
    data = input(">>").split(",")
    pwd = []
    for item in data:
        if len(item) < 6 or len(item) > 12:
            continue
        if len(re.findall('[a-z]',item)) > 0 and len(re.findall('[A-Z]',item)) > 0 and len(re.findall('[0-9]',item)) > 0 and len(re.findall('[$#@]',item)) > 0:
            pwd.append(item)
    print(",".join(pwd))

def n19():
    from operator import itemgetter
    l = []
    print("请输入：")
    while True:
        s = input()
        if not s:
            break
        l.append(tuple(s.split(",")))
    print (sorted(l, key=itemgetter(0,1,2)))

# 使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字
def n20(n):
    data = 0
    while data < n:
        if data % 7 == 0:
            yield data
        data += 1
for i in n20(100):
    print(i)

if __name__ == "__main__":
    for i in n20(100):
        print(i)

