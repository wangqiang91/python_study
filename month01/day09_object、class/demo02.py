"""
    实例成员：对象.成员名
        实例变量:表达不同个体的不同信息
            对象.变量名
        实例方法：对象.方法名(参数)
"""
class Wife:
    def __init__(self,age,name=""):
        self.name = name
        self.age = age
    # 实例变量尽量都写到init中，不建议在方法中再定义变量；
    def set_name(self,sex):
        self.sex = sex

# jian_ning = Wife(18,"heih")
# print(jian_ning.name)
# jian_ning.name = "lala"
# print(jian_ning.name)
# print(jian_ning.__dict__)

class Dog:
    def __init__(self,variety,name,length,weight=1):
        self.variety = variety
        self.name = name
        self.length = length
        self.weight = weight
    def eat_food(self):
        print("吃饭啦")
        self.weight += 1
mixiu = Dog("拉多","小米",0)
mixiu.eat_food()
print(mixiu.weight)