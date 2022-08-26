"""
    算术运算符、增强运算符（+=、-=、*=、/=、**=）
"""

# data01 = 16
# data02 = 3
# data03 = data01**data02
# print(data03)
# print(format(data01/data02,'.2f'))
# print(data01//data02)
# print(data01%data02)

# confirmeder = int(input("请输入确诊人数："))
# curer = int(input("请输入治愈人数："))
# proportion = float(format(curer/confirmeder,'.2f'))
# print(type(proportion))
# print("治愈比例为" + str(proportion*100) + "%")

# weight = int(input("请输入总两数："))
# jin = weight // 16
# liang = weight % 16
# print("{}斤{}两".format(jin,liang))

# distance = float(input("请输入距离："))
# begin_apeed = float(input("请输入初速度："))
# time = int(input("请输入时间："))
# accelerated_speed = (distance - begin_apeed * time) * 2 / time ** 2
# print(accelerated_speed)

# number = input("输入一个整数：")
# sum = 0
# for i in number:
#     sum += int(i)
# print(sum)

number = int(input("输入一个整数："))
sum = number % 10
sum += number //10 % 10
sum += number // 100 % 10
sum += number // 1000 
print(sum)