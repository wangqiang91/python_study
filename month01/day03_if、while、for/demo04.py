'''
    for循环, continue 短路思想
        while/for:
            if  条件1：
                continue
            if 条件2:
                break
            循环体
'''

# num = input("请输入整数")
# sum = 0
# for item in  num:
#     sum += int(item)
# print(sum)

# sum = 0
# for i in range(8,3,-1):
#     sum += i
# print(sum)

# 当条件比较多时(满足XX条件不做)，可以用continue或者break，减少程序的嵌套；
# sum_value = 0
# for item in range(0,101):
#     if item % 3 != 0:
#         continue
#     sum_value += item
# print(sum_value)

sum1 = 0
for i in range(10,61):
    if i % 10 not in (3,5,8):
        sum1 += i
print(sum1)

sum2 = 0
for i in range(10,61):
    if i % 10 in (3,5,8):
        continue
    sum2 += i
print(sum2)
