class CommodityInfos:
    def __init__(self,cid,name,price):
        self.cid = cid
        self.name = name
        self.price = price
class Orders:
    def __init__(self):
        pass
list_commodity_infos = {
    CommodityInfos(101,"屠龙刀",10000),
    CommodityInfos(102,"倚天剑",10000),
    CommodityInfos(103,"九阴白骨爪",8000),
    CommodityInfos(104,"九阳神功",9000),
    CommodityInfos(105,"降龙十八掌",8000),
    CommodityInfos(106,"乾坤大挪移",10000),
}

def print_single_commodity(list_item):
    print(f"编号：{list_item.cid},名称：{list_item.name}")
