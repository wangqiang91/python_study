"""
    重构:不改变功能,修改内部代码.
    --修改命名
    --修改结构(你想传递的思想是什么?)
    注意：隐藏实现细节,彰显程序过程
"""
goods_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_orders = []

def look_goods_message(dict_target):
    """
        查看全部商品
    """
    for key, value in dict_target.items():
        print("编号：%d,名称：%s,单价：%d。" % (key, value["name"], value["price"]))

def add_goods_to_cart():
    """
        添加到购物车,按N退出结束添加。
    """
    while True:
        cid = input("请输入商品编号(输入N退出):")
        if cid == "N":
            break
        if int(cid) in goods_info:
            count = int(input("请输入购买数量："))
            list_orders.append({"cid": int(cid), "count": count})
            print("添加购物车成功")
        else:
            print("该商品不存在")
    
def look_cart_goods(list_target):
    """
        查看购物车中的商品信息；
    """
    for item in list_target:
        goods = goods_info[item["cid"]]
        print("商品：%s,单价：%d,数量:%d." % (goods["name"], goods["price"], item["count"]))

def calculate_money(list_target):
    """
        计算购物车中商品总金额
    """
    total_money = 0
    for item in list_target:
        goods = goods_info[item["cid"]]
        total_money += goods["price"] * item["count"]
    return total_money

def pay_money():
    """
        付钱结算
    """
    total_money = calculate_money(list_orders)
    while True:
        qian = float(input(f"总价{total_money}元,请输入金额："))
        if qian >= total_money:
            print(f"购买成功,找回：{qian - total_money}元。")
            list_orders.clear()
            break
        else:
            print("金额不足,请重新输入")
def buy_goods():
    """
        查看商品=》加购物车=》显示购物车商品=》付钱结算
    """
    look_goods_message(goods_info)
    add_goods_to_cart()
    look_cart_goods(list_orders)
    if calculate_money(list_orders) > 0:
        pay_money()
    else:
        print("您没有需要付款的商品")

buy_goods()

