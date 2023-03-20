from model import GoodsModel

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
        # for i in range(len(self.goods_list)):
        #     if self.goods_list[i].goods_id == goods_id:
        #         del self.goods_list[i]
        #         return True
        # return False

        item = GoodsModel(goods_id=goods_id)
        if item in self.goods_list:
            self.goods_list.remove(item)
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