"""
    练习
"""

#执行结果 [1,2,3]  (1,2,3)   (1,2,3){"a":4,"b":5,"c":6}  10,20,30,{"p5":40}

list_employees = [
    {"eid": 1001, "did": 9002, "name": "师父", "money": 60000},
    {"eid": 1002, "did": 9001, "name": "孙悟空", "money": 50000},
    {"eid": 1003, "did": 9002, "name": "猪八戒", "money": 20000},
    {"eid": 1004, "did": 9001, "name": "沙僧", "money": 30000},
    {"eid": 1005, "did": 9001, "name": "小白龙", "money": 15000},
]
def get_employees_message(dict_target):
    for item in dict_target:
        print(f'{item["name"]}的员工编号是{item["eid"]},部门编号是{item["did"]},月薪{item["money"]}元.')
# get_employees_message(list_employees)

def get_employees_gt_two(list_target):
    for item in list_target:
        if item["money"] > 20000:
            print(f'{item["name"]}的员工编号是{item["eid"]},部门编号是{item["did"]},月薪{item["money"]}元.')
# get_employees_gt_two(list_employees)

def get_lowest_salary(list_target):
    lowest_salary = list_target[0]["money"]
    for item in list_target:
        if lowest_salary > item["money"]:
            lowest_salary = item["money"]
    return lowest_salary
print(get_lowest_salary(list_employees))

def sort_for_money_asc(list_target):
    for i in range(0,len(list_target)-1):
        for j in range(i+1,len(list_target)):
            if list_target[i]["money"] > list_target[j]["money"]:
                list_target[i],list_target[j] = list_target[j],list_target[i]
    print(list_target)
sort_for_money_asc(list_employees)