'''
    if语句的练习
'''

#  猜对了
#  大于3

if int(input("坐电梯人数")) <= 10 and int(input("总重量")) <= 1000:  #注意短路逻辑，如果第一个参数不满足第二个参数可不传；
    print("电梯正常运行")
else:
    print("超载")


age = int(input("请输入年龄"))
if age > 65:
    print("老年")
elif age >= 41:
    print("中年")
elif age >= 18:
    print("青年")
elif age >= 7:
    print("少年")
elif age >= 0:
    print("童年")


account = input("输入账户类型")
money = int(input("输入消费金额"))

if account == "vip":
    if money > 500:
        print("8折")
    else:
        print("85折")
else:
    if money >= 800:
        print("9折")
    else:
        print("原价")

student1 = int(input("请输入第1个同学体重:"))
student2 = int(input("请输入第2个同学体重:"))
student3 = int(input("请输入第3个同学体重:"))
student4 = int(input("请输入第4个同学体重:"))
lighter = student1
if lighter > student2:
    lighter = student2
if lighter > student3:
    lighter = student3
if lighter > student4:
    lighter = student4
print(lighter)