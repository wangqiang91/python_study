import sys
from model import GoodsModel
from bll import GoodsController

class GoodsView:
    def __init__(self):
        self.controller = GoodsController()
    def main(self):
        while True:
            self.__view_menu()
            self.__select_menu()
    def __view_menu(self):
        print("1键录入商品信息")
        print("2键查看商品信息")
        print("3键删除商品信息")
        print("4键修改商品信息")
        print("0键退出系统")
    def __select_menu(self):
        data = int(input("请选择操作"))
        if data == 1:
            self.__input_message()
        elif data == 2:
            self.__display_message()
        elif data == 3:
            self.__delete_message()
        elif data == 4:
            self.__update_message()
        elif data == 0 :
            print("已退出程序")
            sys.exit()
    def __input_message(self):
        goodsmodel = GoodsModel()
        goodsmodel.name = input("输入商品名称：")
        goodsmodel.price = input("输入商品价格：")
        self.controller.add_goods(goodsmodel)
    def __display_message(self):
        for item in self.controller.goods_list:
            print(item)
    def __delete_message(self):
        goods_id = int(input("请输入要删除的商品ID:"))
        if self.controller.remove_goods(goods_id):
            print("删除成功")
        else:
            print("删除失败")
    def __update_message(self):
        model = GoodsModel()
        model.goods_id = int(input("请输入要修改的商品ID:"))
        model.name = input("请输入修改后的名称:")
        model.price = int(input("请输入修改后的价格:"))
        if self.controller.update_goods(model):
            print("修改成功")
        else:
            print("修改失败")