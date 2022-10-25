'''
    列表推导式
'''

# list1 = [45,5,65,7,8,9,34,6]
# new_list = [x%10 for x in list1 ]
# print(new_list)

# list2 = [x for x in range(10,31) if x % 3 ==0 or x % 5 ==0]
# print(list2)

# list3 = [x**2 for x in range(5,21)]
# print(list3)

list4 = [1,2,3]
list5 = [4,5,6]
list6 = [x+y for x in list4 for y in list5]
print(list6)