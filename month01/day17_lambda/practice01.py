"""
    定义函数，根据薪资对员工列表升序排列
    定义函数，根据部门对员工列表升序排列

    定义函数，判断员工列表中是否存在姓名相同的员工
    定义函数，判断员工列表中是否存在薪资相同的员工
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

def asc_as_money():
    for i in range(len(list_employees)-1):
        for j in range(i+1,len(list_employees)):
            if list_employees[i].money > list_employees[j].money:
                list_employees[i],list_employees[j] = list_employees[j],list_employees[i]

def asc_employee(iterable,condition):
    for i in range(len(iterable)-1):
        for j in range(i+1,len(iterable)):
            if condition(iterable[i]) > condition(iterable[j]):
                iterable[i],iterable[j] = iterable[j],iterable[i]

def is_name_repeat():
    for i in range(len(list_employees)-1):
        for j in range(i+1,len(list_employees)):
            if list_employees[i].name == list_employees[j].name:
                return "True"
    return "false"

# asc_employee(list_employees,lambda item:item.did)
# for item in list_employees:
#     print(item.__dict__)

def is_repeat(iterable,condition):
    for i in range(len(iterable)-1):
        for j in range(i+1,len(iterable)):
            if condition(iterable[i]) == condition(iterable[j]):
                return "True"
    return "false" 

print(is_repeat(list_employees,lambda item:item.name))
