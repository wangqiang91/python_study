class Commodity:
    def __init__(self, cid, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]

def get_name_eq_three_str():
    commodity_list = (item for item in list_commodity_infos if len(item.name) == 3 )
    for item in commodity_list:
        print(item.__dict__)
get_name_eq_three_str()

print("=========================")

def get_price_lt_100():
    commodity_list = (item for item in list_commodity_infos if item.price < 100)
    for item in commodity_list:
        print(item.__dict__)
get_price_lt_100()

print("=========================")

def get_all_price():
    all_price = 0
    for item in list_commodity_infos:
        all_price += item.price
    return all_price
print(get_all_price())
