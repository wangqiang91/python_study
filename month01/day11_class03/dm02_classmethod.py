"""
    类成员：
        类方法
"""

class StudyClassMethod:
    class_variable01 = 1000

    @classmethod
    def print_class_variable(cls):
        print(cls.class_variable01)
    
    def __init__(self,name,money):
        self.name = name
        self.money = money
        StudyClassMethod.class_variable01 -= self.money

tian_tan = StudyClassMethod("天坛",20)
StudyClassMethod.print_class_variable()
tian_tan.print_class_variable()
        
"""练习"""

class Wife:
    total_wife = 0
    def __init__(self,name):
        self.name = name
        Wife.total_wife += 1
    @classmethod
    def print_count(cls):
        print(f"总共娶了{cls.total_wife}个老婆。")

w01 = Wife("双儿1")
w02 = Wife("双儿2")
w03 = Wife("双儿3")
w04 = Wife("双儿4")
w05 = Wife("双儿5")
# Wife.print_count()