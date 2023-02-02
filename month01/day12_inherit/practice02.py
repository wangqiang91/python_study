"""
       创建桌子类,保护数据在有效范围内
        数据：品牌,       材质,         尺寸(120,60,80)
                在[实木,板材,金属]范围之内     只读属性
                如果不在,默认第一个元素
"""
class Desk:
    def __init__(self,brand,texture):
        self.brand = brand
        self.texture = texture
        self.__size = (120,60,80)
    @property
    def texture(self):
        return self.__texture
    @texture.setter
    def texture(self,value):
        value_tuple = ("实木","板材","金属")
        if value in value_tuple:
            self.__texture = value
        else:
            self.__texture = value_tuple[0]
    @property
    def size(self):
        return self.__size
desk = Desk("哈哈品牌","板材2")
# print(desk.texture)
# print(desk.size)
# print(desk.__dict__)

"""
     父类：车(品牌，速度)
                0-120
    创建子类：电动车(电池容量,充电功率)
                          180-220
    直接打印对象,格式如下:
            xx的速度是xx
            xx的速度是xx,电池容量是xx,充电功率是xx
"""
class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self,value):
        if value < 0: value = 0
        elif value > 120 : value = 120
        self.__speed = value
    # def brand_speed(self):
    #     print(f"{self.brand}的速度是{self.speed}")
    def __str__(self):
        return  f"{self.brand}的速度是{self.speed}"

class Electrocar(Car):
    def __init__(self, brand, speed,capacity,power):
        super().__init__(brand, speed)
        self.capacity = capacity
        self.power = power
    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self,value):
        if value < 180 : value = 180
        elif value > 220 : value = 220
        self.__capacity = value
    # def message(self):
    #     print(f"{self.brand}的速度是{self.speed},电池容量是{self.capacity},充电功率是{self.power}")
    def __str__(self):
        print(super().__str__())
        return f"{self.brand}的速度是{self.speed},电池容量是{self.capacity},充电功率是{self.power}"
car = Car("小鸟",26)
print(car)
electrocar = Electrocar("小鹏",23,200,150)
# print(electrocar.brand_speed())
print(electrocar)

"""
    以面向对象思想，描述下列情景：
    情景：小明使用手机打电话
    变化：还有可能增加座机
    要求：增加新通信设备，不影响小明.
"""
class XiaoMing:
    def call_iphone(self,communication):
        print("小明打电话")
        communication.tools()
class Communication:
    def tools(self):
        pass

class Iphone(Communication):
    def tools(self):
        print("使用手机")

xm = XiaoMing()
# print(xm.call_iphone(Iphone()))
