"""
    行为继承：
        设计顺序：先子再父； 编码顺序：先父类，再子类；
        适用性：多个类型代码上有共性，且概念统一； 
        子类可以直接使用self调用父类的构造函数和方法，但若子类和父类的方法名/构造函数名一样，
        则必须适用super()来调用。
"""

class Animal:
    def __init__(self,age):
        self.age = age
    def eat(self,name=""):
        print(f"{name}在吃东西!")

class Dog(Animal):
    def run(self,name=""):
        self.eat(name)
        return ("狗狗可以跑！")

class Bird(Animal):
    def fly(self,name=""):
        super().eat(name)
        return (f"{name}鸟可以飞！")

dog = Dog(30)
print(dog.run("大狼狗"))
# print(dog.age)

bird = Bird(60)
print(bird.fly("麻雀"))
# print(bird.age)

print(isinstance(dog,Dog))
print(isinstance(dog,Animal))
print(isinstance(dog,Bird))