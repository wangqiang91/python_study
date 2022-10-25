'''
    容器通用操作、索引、切片
'''

# num1 = int(input("请输入整数:"))
# for i in range(0,num1):
#     if i == 0 or i == num1-1:
#         print("$"*num1)
#     else:
#         # print("$"+" "*(num1-2)+"$")
#         print("s%ss" %(" "*(num1-2)))


# str1 = "我是花果山水帘洞美猴王孙悟空"
# print(str1[4:8])
# print(str1[-7:-10:-1])
# print(str1[7:4:-1])
# print(str1[::-1])
# print(str1[-3:])

str2 = "我是京师监狱狱长金海。"
print("%s,%s,%s" %(str2[0],str2[-1],str2[len(str2)//2]))
print(str2[:3])
print(str2[-3:])
print("金海"in str2)
print("京师监狱"not in str2)
print(str2[2:-3])
print(str2[-4:1:-1])
print(str2[::3])
print(str2[::-1])
