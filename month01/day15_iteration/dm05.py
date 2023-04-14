"""
    生成器表达式
        列表：
            优点：反复使用，可读可写；
            缺点：占用内存较多("特别海量数据时")
        生成器：
            优点：占用内存较少("几乎不占用")
            缺点：1.生成器对象只能用一次，若需要使用多次，则要创建多个对象； 2.不支持索引和切片，也不能修改数据；
            解决方法：list()，转换为列表；
"""

list01 = [43,"a",True,6,7,89,9,"b"]
list_list = [item for item in list01 if type(item) == str]
gene_list = (item for item in list01 if type(item) == str)

for item in list_list:
    print(item)
for item in gene_list:
    print(item)