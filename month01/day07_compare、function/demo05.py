'''
    练习
'''

def get_social_insurance(salary):
    """
        根据工资计算社保；
        :param salary int类型
    """
    social_insurance = salary * (0.08 + 0.02 + 0.002 + 0.12) + 3
    return  social_insurance

def get_discount(account_type,money):
    """
        根据会员等级和花销计算折扣；
        :param account_type str类型  会员等级
        :param money int类型 花销
    """
    if account_type == "vip":
        if money < 500:
            return 0.85
        return 0.8
    else:
        if money > 800:
            return 0.9
        return 1

def get_list_min(list_data):
    min_data = list_data[0]
    for i in range(1,len(list_data)):
        if list_data[i] < min_data:
            min_data = list_data[i]
    return min_data

def get_stage_of_life(age):
    if age <= 6: return "童年"
    if age <= 17: return "少年"
    if age <= 40: return "青年"
    if age <= 65: return "中年"
    return "老年"

print(get_social_insurance(5000))
print(get_discount("vip",900))
print(get_list_min([3,5,3,32,4,23,-4,6,34]))
print(get_stage_of_life(80))