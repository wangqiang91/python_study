"""
    定义函数，在员工列表中累加所有员工的薪资；
    定义函数，在员工列表中累加所有员工的部门；

    定义函数，在员工列表中计算部门是9002的员工数量
    定义函数，在员工列表中计算薪资大于20000的员工数量

    定义函数，在员工列表中删除员工编号是1003的员工
    定义函数，在员工列表中删除姓名是小白龙的员工

    定义函数，在员工列表中删除部门是9001的所有员工
    定义函数，在员工列表中删除姓名是3个字的所有员工
"""
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
    Employee(1005, 9001, "小白龙", 15000)
]

from common.iterable_tools import IterableHelper

def sum_money(item):
    return item.money
print(IterableHelper.sum(list_employees,sum_money))

def sum_did(item):
    return item.did
print(IterableHelper.sum(list_employees,sum_did))

def count_9002(item):
    return item.did == 9002
print(IterableHelper.get_count(list_employees,count_9002))

def count_gt_20000(item):
    return item.money > 20000
print(IterableHelper.get_count(list_employees,count_gt_20000))

def delete_1003(iter):
    return iter.eid == 1003
# print(IterableHelper.delete_single(list_employees,delete_1003))
# for item in list_employees:
#     print(item.__dict__)
# print("=======================") 

def delete_xiaobai(iter):
    return iter.name == "小白龙"
# IterableHelper.delete_single(list_employees,delete_xiaobai)

def delete_all_9001(iter):
    return iter.did == 9001
print(IterableHelper.delete_all(list_employees,delete_all_9001))
for item in list_employees:
    print(item.__dict__)
