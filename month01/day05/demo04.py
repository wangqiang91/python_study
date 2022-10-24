'''
    字符串转换为列表
    列表 = 字符串.split(分隔符)
'''

str1 = "To have a government that is of people by people for people"
list1 = str1.split(" ")
list1 = list1[::-1]
str2 = " ".join(list1)
print(str2)

list2 = str1.split(" ")
for i in range(len(list2)//2):
    list2[i],list2[-(i+1)] = list2[-(i+1)],list2[i]
str3 = " ".join(list2)
print(str3)
