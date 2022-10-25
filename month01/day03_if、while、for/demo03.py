'''
    循环
        while True:
            循环体
            if 退出条件：
                break
        else:
        while True:
            循环体
            if 条件：
                break
        while 条件：
            循环体

'''     

# while True:
#     sex = input("请输入性别")
#     if sex == "男":
#         print("您好，先生！")
#     elif sex == "女":
#         print("您好，女士！")
#     else:
#         print("性别输入错误")
#     if input("退出请按q,继续请按任意键") == 'q':
#         break

# while True:
#     sex = input("请输入性别")
#     if sex == "男":
#         print("您好，先生！")
#     elif sex == "女":
#         print("您好，女士！")
#     else:
#         print("性别输入错误")
#     if input("输入y继续，输入其他退出") != 'y':
#         break

# num = 0
# limit = int(input("输入跑步圈数"))
# while True:
#     print("just run")
#     num += 1
#     if num == limit :
#         break

# num = 0
# limit = int(input("输入跑步圈数"))
# while num < limit:
#     print("just run")
#     num += 1

# num = -1
# while num > -6:
#     print(num,end=" ")
#     num -= 1

# num = 1
# score_all = 0
# while num < 6:
#     score = int(input("请输入成绩："))
#     num += 1
#     score_all += score
# squre = score_all/(num-1)
# print(squre)

# num = 0
# thickness = 0.00001
# while thickness < 8844.43:
#     num += 1
#     thickness *= 2
#     print(num,thickness)
# print(num)

# import random
# result = random.randint(1,100)
# num = 0
# while True:
#     num += 1
#     answer = int(input("您的猜测："))
#     if answer < result:
#         print("小了")
#     elif answer > result:
#         print("大了")
#     else:
#         print("恭喜猜对了")
#         break 
# print("总共猜了{}少次".format(num))

import random
result = random.randint(1,100)
print(result)
num = 0
while num < 3:
    num += 1
    answer = int(input("您的猜测："))
    if answer < result:
        print("小了")
    elif answer > result:
        print("大了")
    else:
        print("恭喜猜对了")
        break
else:  #循环通过break结束时，不执行else；
    print("游戏结束")
print("总共猜了{}次".format(num))