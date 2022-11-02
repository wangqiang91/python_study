'''
    练习
'''

# colour = {"R":"红色","G":"绿色","B":"蓝色","A":"透明度"}
# data = input("请输入颜色")
# if data in colour.keys():
#     print(colour[data])
# else:
#     print("颜色无效！")

list02 = [5,1,4,6,7,4,6,8,5]
count = list02[0]
for i in range(1,len(list02)):
    count -= list02[i]
print(count)

dict_employees = {
    1001: {"did": 9002, "name": "师父", "money": 60000},
    1002: {"did": 9001, "name": "孙悟空", "money": 50000},
    1003: {"did": 9002, "name": "猪八戒", "money": 20000},
    1004: {"did": 9001, "name": "沙僧", "money": 30000},
    1005: {"did": 9001, "name": "小白龙", "money": 15000},
}

for sid,message in dict_employees.items():
    print(f"{message['name']}的员工编号是{sid}，部门编号是{message['did']}，月薪是{message['money']}元；")

for sid,message in dict_employees.items():
    if message['money'] > 20000:
        print(f"{message['name']}的员工编号是{sid}，部门编号是{message['did']}，月薪是{message['money']}元；")

import random
list_ball = []
while len(list_ball) < 6:
    num = random.randint(1,33)
    if num not in list_ball:
        list_ball.append(num)
list_ball.append(random.randint(1,16))
print(list_ball)
for item in list_ball:
    print(item,end="")
