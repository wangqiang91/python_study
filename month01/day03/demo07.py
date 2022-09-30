'''
    容器通用操作、索引
'''

num1 = int(input("请输入整数:"))
for i in range(0,num1):
    if i == 0 or i == num1-1:
        print("$"*num1)
    else:
        # print("$"+" "*(num1-2)+"$")
        print("s%ss" %(" "*(num1-2)))

