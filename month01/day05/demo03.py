'''
    列表转换为字符串
    字符串 = 连接符.join(列表)
'''

# list01 = ["a", "b", "c", "d"]
# result = "_".join(list01)
# print(result)

# list02 = [str(x) for x in range(10)]
# result02 = "".join(list02)
# print(result02)

list_input = []
while True:
    str1 = input("请输入内容: ")
    if str1 == "":
        break
    list_input.append(str1)
str_input = "_".join(list_input)
print(str_input)
