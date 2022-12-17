"""
    MVC(Model,View,Controller):
        是一种软件架构设计思想
        View(视图),负责处理界面逻辑：输入/输出;
        Model(模型),包装多个数据：商品模型;
        Controller(控制器),负责核心业务逻辑：存储;
"""
class GoodsModel:
    def __init__(self,goods_id=1,name="",price=0):
        self.goods_id = goods_id
        self.name = name
        self.price = price

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
    def __input_message(self):
        goodsmodel = GoodsModel()
        goodsmodel.name = input("输入商品名称：")
        goodsmodel.price = input("输入商品价格：")
        self.controller.add_goods(goodsmodel)
    def __display_message(self):
        for item in self.controller.goods_list:
            print(f"编号{item.goods_id}的商品名称是{item.name},价格是{item.price}")
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
class GoodsController:
    start = 1000
    @classmethod
    def set_goods_id(cls,new_goods):
        new_goods.goods_id = cls.start
        cls.start += 1
    def __init__(self):
        self.goods_list = []
    def add_goods(self,new_goods):
        """
            添加商品信息; 
            :param:new_goods:GoodsModel类型数据
        """
        GoodsController.set_goods_id(new_goods)
        self.goods_list.append(new_goods)
    def remove_goods(self,goods_id):
        """
            删除商品信息：
            :param goods_list:要删除的商品编号,int类型;
        """
        for i in range(len(self.goods_list)):
            if self.goods_list[i].goods_id == goods_id:
                del self.goods_list[i]
                return True
        return False
    def update_goods(self,model): 
        """
            修改商品信息;
            :param model:GoodsModel类型数据;使用__dict__修改全部信息;
        """
        for item in self.goods_list:
            if item.goods_id == model.goods_id:
                item.__dict__ = model.__dict__
                return True
        return False

goods = GoodsView()
goods.main()