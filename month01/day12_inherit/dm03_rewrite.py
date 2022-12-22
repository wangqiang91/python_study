"""
    重写：父类有，子类也有的方法；
    多态：父类一个方法，不同的子类有不同的行为；
     
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

# person = Person("悟空",600.8)
# print(person)
# print(int(person))


class Commodity:
    def __init__(self,cid,name,price) -> None:
        self.cid = cid 
        self.name = name 
        self.price = price
    def __str__(self) :
        return f"编号为{self.cid}的商品{self.name}的价格是{self.price}"

# c01 = Commodity(1001,"屠龙刀","400")
# print(c01)

"""算法add的重写"""  
class Vector2:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        if isinstance(other,Vector2):
            x = self.x + other.x
            y = self.y + other.y
        else:
            x = self.x + other
            y = self.y + other
        return Vector2(x,y)
pos1 = Vector2(1,4)
pos2 = Vector2(4,2)
pos3 = pos1 + 5
# print(pos3.__dict__)

class Colour:
    def __init__(self,r,g,b,a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
    def __sub__(self,other):
        if type(other) == Colour:
            r = self.r - other.r
            g = self.g - other.g
            b = self.b - other.b
            a = self.a - other.a
        else:
            r = self.r - other
            g = self.g - other
            b = self.b - other
            a = self.a - other
        return Colour(r,g,b,a)
cou1 = Colour(1,2,3,4)
cou2 = Colour(20,30,40,50)
cou3 = cou1 - cou2
print(cou3.__dict__)