"""
    继承-数据
        1.子类没有构造函数，可以直接使用父类的构造函数；
        2.子类有构造函数，子类必须通过super().__init__(data1,data2)调用父类构造函数；
"""
class Person:
    def __init__(self,name="",age=0):
        self.name = name 
        self.age = age
    #自定义对象 输出成 字符串
    def __str__(self):
        return f"我的名字是{self.name},年龄是{self.age}"

class Student1(Person):
    def message(self):
        print(f"学生姓名是:{self.name};学生年龄是:{self.age}")

class Student2(Person):
    def __init__(self,score,name="", age=1):
        super().__init__(name, age)
        self.score = score

stu2 = Student2(100,"张三",38)
print(stu2)
# print(stu2.age)

"""练习"""
class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
class ElectroCar(Car):
    def __init__(self, brand, speed,battery=0,power=0):
        super().__init__(brand,speed)
        self.battery = battery
        self.power = power

# elc = ElectroCar("xiaoniu",300,60,40)
# print(elc.__dict__)