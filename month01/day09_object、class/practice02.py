class Employees:
    def __init__(self,eid,did,name,money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money
class Departments:
    def __init__(self,did,title):
        self.did = did
        self.title = title

list_employees = [
    Employees(1001,9002,"师父",60000),
    Employees(1002,9001,"孙悟空",50000),
    Employees(1003,9002,"猪八戒",20000),
    Employees(1004,9001,"沙僧",30000),
    Employees(1005,9001,"小白龙",15000),
]
list_departments = [
    Departments(9001,"教学部"),
    Departments(9002,"销售部")
]

dict_departments = {item.did:item.title for item in list_departments}

def employees_message(em_item):
    print(f"{em_item.name}的员工编号是{em_item.eid},\
    部门编号是{em_item.did},月薪{em_item.money}元")
def money_gt2(em_item):
    if em_item.money > 20000:
        print(f"{em_item.name}的员工编号是{em_item.eid},\
        部门编号是{em_item.did},月薪{em_item.money}元")
def employees_department(em_item):
    print(f"{em_item.name}的部门是{dict_departments[em_item.did]},月薪{em_item.money}元")
def least_money(list_em):
    least = list_em[0].money
    for i in range(1,len(list_em)):
        if least > list_em[i].money:
            least = list_em[i].money
    print(least)

def money(list_em):
    for i in range(len(list_em)-1):
        for j in range(i+1,len(list_em)):
            if list_em[i].money > list_em[j].money:
                list_em[i],list_em[j] = list_em[j],list_em[i]
    for item in list_employees:
        print(item.__dict__)  #类的变量本质上以字典的形式存储值，故可以用__dict__显示类的变量和变量值；
def total_money(em_item):
    total_money = 0
    for item in em_item:
        total_money += item.money
    print(total_money)
money(list_employees)
total_money(list_employees)
