'''
    容器种类与特点：
        字符串：存储字符编码，不可变，序列；
        列表：存储变量，可变，序列；
        元祖：存储变量，不可变，序列；
        字典：存储键值对（键唯一且是不可变数据），可变，散列；
'''

for i in range(4):
    for j in range(i+1):
        print("$",end="")
    print()

for i in range(3):
    for j in range(5):
        print(i,end="")
        print(j,end="\t")
    print()

dict_hobbies = {
    "yuqian":["抽烟","喝酒","烫头"],
    "guodegang":["说","学","逗","唱"]
}
for item in dict_hobbies["yuqian"]:
    print(item)

print(len(dict_hobbies["guodegang"]))

for item in dict_hobbies:
    print(item)

for item in dict_hobbies.values():
    for data in item:
        print(data)