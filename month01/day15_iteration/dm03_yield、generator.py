"""
    生成器 = 可迭代对象(__iter__) + 迭代器(__next__)
    生成器函数(generator):
        函数中有yield;
        优点：生成海量数据也不占很多内存；
    yield:
        将yield之前的代码定义在__next__函数中;
        将yield之后的代码做为__next__函数的返回值; 
    适用性：函数返回多个结果，使用yield，返回单个结果，使用return；
"""
list01 = [34,53,232,4355,3454,322]

# 传统思维做法：创建容器，存储数据；
def get_number_gt_1001():
    item_list = []
    for item in list01:
        if item > 100:
            item_list.append(item)
    return item_list
result = get_number_gt_1001()
for number in result:
    print(number)
print("==============================")
# 迭代器思维做法：循环一次，计算一次，返回一次； 
def get_number_gt_1002():
    for item in list01:
        if item > 100:
            yield item
result = get_number_gt_1002()
for number in result:
    print(number)