import re


list1 = [[40, 5], [6, 17], [8, 9], [2, 3], [5, 6]]
# list2 = [item for item in ()]
print(str(list1))

list1 = re.findall('[0-9]+',str(list1))
print(list1)