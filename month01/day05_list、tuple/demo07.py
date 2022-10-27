'''
    练习
'''

list01 = [1,2,3,4,5,4,3,2,1]
for item in list01:
    print("*"*item)

total = 1
list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
for item in list02:
    total *= item
print(total)

list_area = []
while True:
    area = input("请输入地区:")
    if area == "":
        break
    if area not in list_area:
        list_area.append(area)
for i in range(len(list_area)-1,-1,-1):
    print(list_area[i])

# list_people = []
# for i in range(5):
#     peoples = int(input("请录入确诊人数"))
#     list_people.append(peoples)
list_people = [int(input("请录入确诊人数")) for i in range(5)]
print(max(list_people))
print(min(list_people))
print(sum(list_people)/len(list_people))
