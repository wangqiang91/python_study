'''
    字典：由一系列键值对组成的可变散列容器；
    列表：由一系列变量组成的可变序列容器；
'''
#创建
dict_01 = {"name":"wanghuan","age":20,"sex":"girl"}
# print(dict_01)
# list_name = ["wang","zhang","li"]
# list_age = [30,40,30]
# dict_02 = dict(zip(list_name,list_age))
# print(dict_02)

#添加/修改
# dict_02["liu"] = 60
# dict_02["wang"] = 33
# print(dict_02)

#删除
# del dict_02["liu"],dict_02["wang"]
# print(dict_02)

#遍历
# for key in dict_01.keys() :
#     print(key)

# for value in dict_01.values():
#     print(value)

# for key,value in dict_01.items():
#     print(key)
#     print(value)

#dict --> list
# print(list(dict_01))
# print(list(dict_01.values()))
# print(list(dict_01.items()))

dict_03 = {"name":"wanghuan","age":20,"sex":"girl","score":20}
for key in dict_03.keys():
    if dict_03[key] == 20:
        print(key)

for key,value in dict_03.items():
    if value == 20:
        print(key)