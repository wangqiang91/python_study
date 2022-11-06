'''
    函数、函数设计思想
        如果没有返回值,默认返回空None;
        return后续的代码不再执行;
        函数中return可以退出多层循环嵌套;
'''
# def print_single_list(list_target):
#     for item in list_target:
#         print(item)

# list01 = [5,546,6,56,76]
# print_single_list(list01)

# def add(num1,num2):
#     result = num1 + num2
#     return result
# data = add(3,7)
# print(data) 

def func01():
    """
        函数的说明
    """
    print("func01 is done")
    return 100
data01 = func01()
print(data01)
