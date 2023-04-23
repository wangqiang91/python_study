"""
    闭包：必须有一个内嵌函数、内嵌函数必须引用外部函数的变量、外部函数返回值必须是内嵌函数；
"""
def func01():
    a = 10
    def func02():
        print(a)
    return func02
# func01()()

"""
    闭包--应用  逻辑连续(外部函数不释放)
"""
def give_new_year_money(money):
    print(f"得到了{money}元压岁钱")
    def child_buy(commodity,price):
        nonlocal money
        money -= price
        print(f"花了{price}元购买了{commodity}，还剩下{money}元")
    return child_buy

action = give_new_year_money(1000)
action("商品1",200)
action("商品2",200)

# practice01
def save_money(money):
    print(f"在银行存入了{money}元")
    def buy_commodity(commodity,price):
        nonlocal money
        money -= price
        print(f"购买{commodity}花了{price}元,还剩下{money}元")
    return buy_commodity
action1 = save_money(10000)
action1("商品a",300)