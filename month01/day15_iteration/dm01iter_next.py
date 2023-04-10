"""
    迭代器
"""
message = "测试输入输出呀"
# for 循环原理
# 1.获取迭代器对象
iterator = message.__iter__()
# 2.获取下一个元素
while True:
    try:
        item = iterator.__next__()
        # print(item)
    except StopIteration:
        break

# 练习1   
list1 = ["a","b",123,"ceshi"]
iter_list1 = list1.__iter__()
while True:
    try:
        item_list1 = iter_list1.__next__()
        print(item_list1)
    except:
        break
# 练习2
dict1 = {"a":1,"b":2,"c":3}
iter_dict1 = dict1.__iter__()
while True:
    try:
        item_dict1 = iter_dict1.__next__()
        print(f"{item_dict1}:{dict1[item_dict1]}")
    except:
        break