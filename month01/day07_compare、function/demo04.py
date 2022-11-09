'''
    函数定义
            函数定义时，可以不考虑每个函数的顺序；
    函数调用
            函数调用一般放在函数定义的下面，要考虑执行顺序；
    多函数嵌套调用
'''

def get_feb_days(year):
    if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
        return 29
    return 28
def get_year_days(year,month,day): 
    feb = get_feb_days(year)
    days_of_month = (31,feb,31,30,31,30,31,31,30,31,30,31)
    total_days = sum(days_of_month[:month-1]) + day
    return total_days

data = get_year_days(2021,12,7)
print(data)