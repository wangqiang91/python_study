"""
    属性property:
        作用：保护数据的有效性;
        1.私有化存储数据的变量  2.提供公开的读写方法
        属性分类：
        1.读写属性：控制实例变量的读写操作；
        2.只读属性：为私有变量提供读取功能；本类里的函数可以任意使用，其他类可以读取但不可以修改；
        3.只写属性：实例变量在类外只能被修改，不能被读取；
"""
class Wife:
    def __init__(self,name="",age=0):
        self.name = name
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if value > 30: value = 30
        elif value < 20 : value = 20
        self.__age = value    
    # age = property(get_age,set_age)  #原理

# jian_ning = Wife("建宁",200)
# print(jian_ning.age)
"""属性分类"""
# 1.读写属性：控制实例变量的读写操作；
class Data:
    def __init__(self,data=0):
        self.data = data
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self,value):
        self.__data = value
# 2.只读属性：为私有变量提供读取功能；本类里的函数可以任意使用，
#             其他类可以读取但不可以修改；
class Data:
    def __init__(self,data=0):
        self.__data = data
    @property
    def data(self):
        return self.__data
# 3.只写属性：实例变量在类外只能被修改，不能被读取；
class Data:
    def __init__(self,data=0):
        self.data = data
    data = property()
    @data.setter
    def data(self,value):
        self.data = value


"""练习"""

class Enemy:
    def __init__(self,name="",attack=0,blood=0):
        self.name = name
        self.attack = attack
        self.blood = blood
    @property
    def attack(self):
        return self.__attack
    @attack.setter
    def attack(self,value):
        if value < 0 : value = 0
        elif value > 100 : value = 100
        self.__attack = value
    @property
    def blood(self):
        return self.__blood
    @blood.setter
    def blood(self,value):
        if value < 0 : value = 0
        elif value > 500 : value = 500
        self.__blood = value
enemy = Enemy(blood = 600)
print(enemy.blood)

