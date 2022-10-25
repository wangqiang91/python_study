'''
    元祖：由一系列变量组成的不可变序列容器； 存储计算结果的数据（节省内存）；
    列表：由一系列变量组成的可变序列容器； 存储计算过程的数据；
    可变数据类型：列表、字典、集合
    不可变数据类型：字符串、int、元祖
'''

day_of_month = (31,29,31,30,31,30,31,31,30,31,30,32)
input_month = int(input("请输入月份:"))
input_day = int(input("请输入天数:"))
total_days = input_day
# for i in range(input_month-1):
#     total_days+= day_of_month[i]
total_days += sum(day_of_month[:input_month-1])
print(total_days)

