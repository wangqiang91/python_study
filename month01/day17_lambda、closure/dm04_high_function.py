"""
    内置高阶函数：map、max、sorted、filter、列表.sort();
"""
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
    Commodity(1005, "酒精工", 30)
]

for item in map(lambda item:(item.name,item.price),list_commodity_infos):
    print(item)

for item in filter(lambda item:item.price < 10000,list_commodity_infos):
    print(item.__dict__)

for item in sorted(list_commodity_infos,key=lambda item:item.price,reverse=True):
    print(item.__dict__)

print(max(([1,1],[2,2,2],[3,3,3,3]),key=lambda item:len(item)))