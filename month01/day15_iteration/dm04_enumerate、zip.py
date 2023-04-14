"""
    内置生成器:enumerate
"""
list01 = [3, 45, 34, 9, 8]
# 将列表中所有奇数设置为None

for i, item in enumerate(list01):
    if item % 2 != 0:
        list01[i] = None
# print(list01)

list02 = [3, 45, 34, 9, 8]
for i, item in enumerate(list02):
    if item % 2 == 0:
        list02[i] += 1
# print(list02)

"""
    内置生成器:zip(矩阵转置)
"""
list03 = [1, 2, 3, 4, 5]
list04 = [11, 22, 33, 44, 55]
dict1 = dict(zip(list03, list04))
# print(dict1)

map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4]
]
new_map = []
for item in zip(*map):
    new_map.append(list(item))
print(new_map)

new_map1 = [list(item) for item in zip(*map)]
print(new_map1)

# practice01：
class Student_message:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def student_list(self):
        student_list = [list(item) for item in zip(self.name,self.age,self.sex)]
        return student_list
student_name = ["姓名1","姓名2","姓名3"]
student_age = [32,23,24]
student_sex = ["男","男","女"]
result = Student_message(student_name,student_age,student_sex).student_list()
print(result)