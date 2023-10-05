# 读方式，文件必须存在；
# fr1 = open("month02/day02/demo01.py","r")

# 写方式打开；
# fr2 = open("month02/day03/demo11.txt","w")

# 追加方式；
# fr3 = open("month02/day03/demo11.txt","a")

fr4 = open("month02/day03/demo11.txt","r")
while True:
    data = fr4.read(5)
    if data == "":
        break
# 读取文件内容：read()
    print(data,end="")

# 关闭文件：close()
fr4.close()

# 读取单行内容；
# line1 = fr4.readline()
# print(line1)

# 读取多行内容，并以列表形式返回数据；
# line2 = fr4.readlines(8)
# print(line2)

# 迭代取值，每次取一行；
# for line in fr4:
#     print(line)