# practice01:
# 定义函数，在列表中找出所有偶数；
list1 = [43,34,54,56,76,87,98]
# method1
def find_even_number1(item_list):
    even_list = []
    for item in item_list:
        if item % 2 == 0:
            even_list.append(item)
    return even_list
result = find_even_number1(list1)
for item in result:
    print(item)
print("======================")

# method2
def find_even_number2(item_list):
    for item in item_list:
        if item % 2 == 0:
            yield item
result = find_even_number2(list1)
for item in result:
    print(item)
print("=======================")

# practice02:定义函数，在列表中找出所有数字
list2 = [43,"悟空",True,56,"八戒",87.5,98]
def find_number(item_list):
    for item in item_list:
        if type(item) in (int,float):
            yield item
result2 = find_number(list2)
for item in result2:
    print(item)