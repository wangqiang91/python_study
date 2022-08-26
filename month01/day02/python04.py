"""
    数据类型  int()向下取整
"""

price = float(input("请输入商品单价："))
number = int(input("请输入商品数量："))
money = float(input("请输入支付金额："))
print("应找回：{}".format(money-price*number))