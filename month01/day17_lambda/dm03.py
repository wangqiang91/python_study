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

def get_all_employee_names():
    for item in list_employees:
        yield item.name
def get_all_employee_ids():
    for item in list_employees:
        yield item.did,item.money
for item in get_all_employee_names():
    print(item)

def common(target_data,condition):
    for item in target_data:
        yield condition(item)

for item in (common(list_employees,lambda item : item.name)):
    print(item)

