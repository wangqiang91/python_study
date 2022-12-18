"""
    行为继承：
        设计顺序：先子再父； 编码顺序：先父类，再子类；
        适用性：多个类型代码上有共性，且概念统一； 
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
        self.eat(name)
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