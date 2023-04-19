from common.iterable_tools import IterableHelper
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

def commodity_price_gteq_1000(item):
    return item.price >= 10000
data1 = IterableHelper().find_all(list_commodity_infos,commodity_price_gteq_1000)
for item in data1:
    print(item.__dict__)
print("=============================")

def commodity_name_len_3(item):
    return len(item.name) == 3
data2 = IterableHelper().find_all(list_commodity_infos,commodity_name_len_3)
for item in data2:
    print(item.__dict__)
print("=============================")

def commodity_cid_eq_1003(item):
    return item.cid == 1003
print(IterableHelper().find_single(list_commodity_infos,commodity_cid_eq_1003).__dict__)
print("=============================")

def delete_all_price_lt_100(item):
    return item.price < 100
# IterableHelper.delete_all(list_commodity_infos,delete_all_price_lt_100)
# for item in list_commodity_infos:
#     print(item.__dict__)
# print("=============================")

def delete_cid_eq_1005(item):
    return item.cid == 1005
# IterableHelper.delete_single(list_commodity_infos,delete_cid_eq_1005)
# for item in list_commodity_infos:
#     print(item.__dict__)
# print("=============================")

def count_len_name_eq_2(item):
    return len(item.name) == 2
print(IterableHelper.get_count(list_commodity_infos,count_len_name_eq_2))

def sum_price(item):
    return item.price
print(IterableHelper.sum(list_commodity_infos,sum_price))