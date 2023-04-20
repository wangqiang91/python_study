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