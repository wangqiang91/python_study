"""
    直接打印自定义对象，显示的是内存地址；
    使用__str__，返回字符串，打印自定义对象，显示的是对应字符串；
"""

class Person:
    def __init__(self,name="",age=1):
        self.name = name
        self.age = age
    def __str__(self):
        #返回值必须是字符串
        return f"{self.name}的年龄是{self.age}"
    def __int__(self):
        return int(self.age)

person = Person("悟空",600.8)
print(person)
print(int(person))


class Commodity:
    def __init__(self,cid,name,price) -> None:
        self.cid = cid 
        self.name = name 
        self.price = price
    def __str__(self) :
        return f"编号为{self.cid}的商品{self.name}的价格是{self.price}"

c01 = Commodity(1001,"屠龙刀","400")
print(c01)