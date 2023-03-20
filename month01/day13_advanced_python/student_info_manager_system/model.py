class GoodsModel:
    def __init__(self,goods_id=1,name="",price=0):
        self.goods_id = goods_id
        self.name = name
        self.price = price
    def __str__(self):
        return f"编号{self.goods_id}的商品名称是{self.name},价格是{self.price}"
    def __eq__(self,other):
        return self.goods_id == other.goods_id