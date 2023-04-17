"""
    使用自定义工具函数操作列表
    在common/iterable_tools.py中创建类IterableHelper；
    再创建静态方法find_single
"""
from common.iterable_tools import IterableHelper

list01 = [43, 54, 54, 65, 67, 7]


def gt_50(item):
    return item > 50


print(IterableHelper().find_single(list01, gt_50))


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

def did_eq_9001():
    for item in list_employees:
        if item.did == 9001:
            yield item
def name_eq_2():
    for item in list_employees:
        if len(item.name) == 2:
            yield item

def did_eq_9001_02(item):
    return item.did == 9001

def name_eq_2_02(item):
    return len(item.name) == 2

for item in IterableHelper.find_all(list_employees,did_eq_9001_02):
    print(item.__dict__)


