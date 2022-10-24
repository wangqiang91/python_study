'''
    列表基础操作
    创建：  列表名 = [元素1,元素2]
            列表名 = list()
    添加：   列表名.append()
            列表名.insert(索引，元素)
    定位：  索引  列表名[整数]
            切片  列表名[整数：整数：整数]
    删除：  根据定位 del 列表名[索引/切片]
            根据元素 列表名.remove(元素)
    遍历：  for item in 列表：
            for i in range(整数，整数，整数):
'''
from re import I


list_planet = ["水星","金星","火星","木星"]
list_planet.insert(2,"地球")
list_planet.append("土星")
list_planet.append("天王星")
list_planet.append("海王星")
print(list_planet[0],list_planet[-1])
print(list_planet[0:2]) 
if "海王星" in list_planet:
    list_planet.remove("海王星")
del list_planet[3]
for i in range(len(list_planet)-1,-1,-1):
    print(list_planet[i],end=" ")
print()
for i in list_planet[len(list_planet)-1::-1]:
    print(i,end=" ")


# for i in range(3):
#     name = input("请输入账号:")
#     password = input("请输入密码:")
#     if name == "Qtx" and password == "123456":
#         print("登录成功")
#         break
#     else:
#         print("登录失败")
#         print("你还剩余%s次机会" %(2-i))
# else:
#     print("账户被锁定")

# import random
# money = 10000
# while money > 0:
#     bottom = int(input("少侠请下注:"))
#     if bottom > money:
#         print("超出了你的身家，请重新投注.")
#     else:
#         data1 = random.randint(1,6)
#         data2 = random.randint(1,6)
#         if data1 == data2:
#             print("你摇出了%s点,庄家摇出了%s点" %(data1,data2))
#             print("打平了，少侠，在来一局")
#         elif data1 > data2 :
#             money = money + bottom
#             print("你摇出了%s点,庄家摇出了%s点" %(data1,data2))
#             print("恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩%s" %(money))
#         elif data1 < data2 :
#             money = money - bottom
#             print("你摇出了%s点,庄家摇出了%s点" %(data1,data2))
#             print("少侠,你输了，身家还剩%s" %(money))
# print("哈哈哈，少侠你已经破产，无资格进行游戏")

