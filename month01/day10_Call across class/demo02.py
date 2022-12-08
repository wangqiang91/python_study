"""
    MVC(Model,View,Controller):
        是一种软件架构设计思想
        View(视图)，负责处理界面逻辑：输入/输出；
        Model(模型)，包装多个数据：商品模型；
        Controller(控制器)，负责核心业务逻辑：存储；
"""
class GoodsModel:
    def __init__(self,goods_id=1,name="",price=0):
        self.goods_id = goods_id
        self.name = name
        self.price = price

class GoodsView:
    def __init__(self):
        self.controller = GoodsController()
    def view_menu(self):
        print("1键录入商品信息")
        print("2键查看商品信息")
        print("3键修改商品信息")
        print("4键录入商品信息")
    def select_menu(self):
        data = int(input("请选择操作"))
        if data == 1:
            self.input_message()
    def input_message(self):
        goodsmodel = GoodsModel()
        goodsmodel.name = input("输入商品名称：")
        goodsmodel.price = input("输入商品价格：")
        self.controller.add_goods(goodsmodel)
class GoodsController:
    def add_goods(self,new_goods):
        print("添加商品成功")

goods = GoodsView()
while True:
    goods.view_menu()
    goods.select_menu()