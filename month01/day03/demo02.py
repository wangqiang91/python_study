'''
    选择语句, if 
'''

# sex = input("请输入性别")
# if sex == "男":
#     print("您好，先生！")
# elif sex == "女":
#     print("您好，女士！")
# else:
#     print("性别输入错误")


# number1 = int(input("请输入身高："))
# number2 = int(input("请输入身高："))
# number3 = int(input("请输入身高："))
# number4 = int(input("请输入身高："))
# max_number = number1
# if max_number < number2:
#     max_number = number2
# if max_number < number3:
#     max_number = number3
# if max_number < number4:
#     max_number = number4
# print(max_number)

#连续区间判断，可以只考虑单边;
# ma = int(input("请输入心里年龄："))
# ca = int(input("请输入实际年龄："))
# iq = ma / ca * 100
# if iq >= 140:
#     print("天才")
# elif iq >= 120:
#     print("聪慧")
# elif iq >= 110:
#     print("正常")
# elif iq >= 90:
#     print("")
# elif iq >= 80:
#     print("迟钝")
# else:
#     print("低能")



month_number = int(input("请输入月份："))
if 1 <= month_number <= 12:
    if month_number == 2:
        print("29天")
    elif month_number in (4,6,9,11):
        print("30天")
    else:
        print("31天")
else:
    print("月份有误")