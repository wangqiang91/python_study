'''
    for循环, continue 短路思想
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
sum_value = 0
for item in range(0,101):
    if item % 3 != 0:
        continue
    sum_value += item
print(sum_value)