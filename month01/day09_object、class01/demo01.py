"""
    类:
    class 类名_首字母大写,无需下划线：
       文档说明
       def __init__(self,参数):
            self.实例变量 = 参数
        方法成员
    实例化对象：
    变量 = 类名(参数)
"""
class Wife:
    def __init__(self,name,height,face_score):
        self.name = name
        self.height = height
        self.face_score = face_score
    def work(self):
        print(f"{self.name}在工作")


wife = Wife("ake",170,80)
wife.work()

class MobilePhone:
    def __init__(self,brand,price,colour):
        self.brand = brand
        self.price = price
        self.colour = colour
    def communicate_by_phone(self):
        print(f"{self.brand}接听电话")
        print(f"{self.brand}拨打电话")

phone1 = MobilePhone("华为",6000,"red")
phone2 = MobilePhone("苹果",8000,"blue")
phone1.communicate_by_phone()
phone2.communicate_by_phone()