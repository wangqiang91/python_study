"""
    重写-比较: 
        判断是否相等(==):__eq__
        比较大小(<或>)：__lt__
"""

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __eq__(self,other):
        return self.__dict__ == other.__dict__
    def __lt__(self,other):
        if self.x != other.x:
            return self.x < other.x
        else:
            return self.y < other.y

v01 = Vector(6,4)
v02 = Vector(6,4)
print(v01 == v02)

v03 = Vector(5,2)
v04 = Vector(5,8)
print(v03 > v04)