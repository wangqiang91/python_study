"""
    lambda应用：
        作为函数的实参；
"""
import os
path1 = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import sys
sys.path.append(path1)

from month01.day16.common.iterable_tools import IterableHelper
list01 = [43,54,54,65,67,7]
def find_first_even02(item):
    return item % 2 == 0
def find_lq_10_02(item):
    return item < 10
print(IterableHelper.find_single(list01,find_first_even02))
print(IterableHelper.find_single(list01,find_lq_10_02))

print(IterableHelper.find_single(list01,lambda item:item % 2 == 0))
print(IterableHelper.find_single(list01,lambda item:item < 10))

# practice01:
class Commodity:
    def __init__(self, cid, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精工", 30),
]

for item in (IterableHelper.find_all(list_commodity_infos,lambda item:item.price >= 10000)):
    print(item.__dict__)
print("============================")

for item in (IterableHelper.find_all(list_commodity_infos,lambda item:len(item.name) == 3)):
    print(item.__dict__)
print("============================")

print(IterableHelper.find_single(list_commodity_infos,lambda item:item.cid == 1003).__dict__)
print("============================")

IterableHelper.delete_all(list_commodity_infos,lambda item : item.price < 100)
for item in list_commodity_infos:
    print(item.__dict__)
print("============================")

IterableHelper.delete_single(list_commodity_infos,lambda item:item.cid == 1002)
for item in list_commodity_infos:
    print(item.__dict__)


