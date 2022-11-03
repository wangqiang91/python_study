'''
    练习 
'''

# dict_travel_info = {
#     "北京":{
#         "景区":["长城","故宫"],
#         "美食":["烤鸭","豆汁胶圈","杂酱面"]
#     },
#     "四川":{
#         "景区":["九寨沟","峨眉山"],
#         "美食":["火锅","兔头"]
#     }
# }

# print(dict_travel_info["北京"]["景区"][0])

# print(dict_travel_info["四川"]["美食"][1])

# for key in dict_travel_info.keys():
#     print(key)

# for food in dict_travel_info["北京"]["美食"]:
#     print(food)
# print("++++++++++++++++++++++++++")

# for city in dict_travel_info.keys():
#     for food in dict_travel_info[city]["美食"]:
#         print(food)
from unicodedata import name


dicy_commodity_infos = {
    1001:{"name":"屠龙刀","price":10000},
    1002:{"name":"倚天剑","price":10000},
    1003:{"name":"金箍棒","price":52000},
    1004:{"name":"口罩","price":20},
    1005:{"name":"酒精","price":30}
}
list_orders = [
    {"cid":1001,"count":1},
    {"cid":1002,"count":3},
    {"cid":1005,"count":2}
]
for item in list_orders:
    print(f"商品编号{item['cid']},购买数量{item['count']}")

for item in list_orders:
    cid = dicy_commodity_infos[item["cid"]]
    print(f"商品名称{cid['name']},商品单价{cid['price']},数量{item['count']}")

max_data = list_orders[0]
for i in range(1,len(list_orders)):
    if max_data["count"] < list_orders[i]["count"]:
        max_data = list_orders[i]
print(max_data)

for i in range(len(list_orders)-1):
    for j in range(i+1,len(list_orders)):
        if list_orders[i]["count"] < list_orders[j]["count"]:
            list_orders[i],list_orders[j] = list_orders[j],list_orders[i]
print(list_orders)