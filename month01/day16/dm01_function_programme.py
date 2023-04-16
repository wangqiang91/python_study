"""
    函数式编程:
        适用性：多个函数，主体相同，核心算法不同；
        
"""
list01 = [43,54,54,65,67,7]

# 定义函数，查找第一个偶数
def find_first_even():
    for item in list01:
        if item % 2 == 0:
            return item

# 定义函数，查找第一个小于10的数
def find_lq_10():
    for item in list01:
        if item < 10:
            return item

# 定义函数，在列表中查找第一个奇数
def find_first_odd():
    for item in list01:
        if item % 2 != 0:
            return item
# 定义函数，在列表中查找第一个能被3或5整除的数字
def find_division_3or5():
    for item in list01:
        if item % 3 == 0 or item % 5 == 0:
            return item

def find_first_even02(item):
    return item % 2 == 0
def find_lq_10_02(item):
    return item < 10
def find_first_odd_02(item):
    return item % 2 != 0
def find_division_3or5_02(item):
    return item % 3 == 0 or item % 5 == 0
def find_single(func):
    for item in list01:
        if func(item):
            return item
print(find_single(find_division_3or5_02))