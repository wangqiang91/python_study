"""
    列表（创建 添加  定位 删除  遍历 ）
"""

# list1 = list("测试呀")
# list2 = [1,2,3]
# print(list1)

# list2.append(4)
# print(list2)

# list2.insert(1,"哈哈")
# print(list2)

list_area = ["香港", "云南", "广东"]
list_new = [3,4,5]
list_now = [500,600,300]
# list_area.append("上海")
# list_area.insert(0, "台湾")
# print(list_area)

# print(list_area[2])
# del list_area[0]
# list_area[:2] = ["小港", "小南"]
# if "小南" in list_area:
#     list_area.remove("小南")
# print(list_area)

# print("%s地区新增%s人现存%s人" %(list_area[0],list_new[0],list_now[0]))
# print(f"{list_area[0]}地区新增{list_new[0]}人现存{list_now[0]}人")

# list_area[1:] = ["GD","SH"]
# print(list_area)
# if "香港" in list_area:
#     list_area.remove("香港")
# del list_new[0]
# del list_now[:2]

# print(list_area,list_new,list_now)

# for i in range(len(list_area)-1,-1,-1):
#     print(list_area[i])


a = [1,2,3,4,5,6,7,2,1,23,34,423,2,2,1]
dict1 = {}
for i in a:
    if i not in dict1.keys():
        number = a.count(i)
        dict1[i] = number
print(dict1)

