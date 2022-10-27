'''
    字典推导式：根据可迭代对象，简单的构建新字典；
'''

dict_result = {number:number**2 for number in range(10) if number % 2 == 0}
print(dict_result)
list_name = ["张无忌","赵敏","周芷若"]
list_room = [101,102,103,54]
dict01 = {list_room[i]:list_name[i] for i in range(min(len(list_room),len(list_name)))}
print(dict01)
dict02 = {value:key for key,value in dict01.items()}
#键值颠倒会有数据丢失的可能性(因为之前的值可能相同)
print(dict02)