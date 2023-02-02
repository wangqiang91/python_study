"""
    架构设计思想
"""
"""架构师设计框架，保证新增工具时，客户端代码无需修改"""
class Person:
    def __init__(self,name="老张"):
        self.name = name
    def go_to(self,how,place="东北"):
        print(f"{self.name}{how.vehicle()}{place}")
class How:
    def vehicle(self):
        pass
"""程序员编码"""
class Car(How):
    def vehicle(self):
        return "开车去"
class Airplane(How):
    def vehicle(self):
        return "坐飞机"

person = Person()
print(person.go_to(Airplane()))


"""练习"""

class Boom:
    def hurt(self,damage):
        return (f"炸弹爆炸了，{damage.hurt()}")
class Damage:
    def hurt(self):
        pass

class people_hurt(Damage):
    def hurt(self):
        return ("玩家受伤了，闪现红屏；")
class enemy_hurt(Damage):
    def hurt(self):
        return ("敌人受伤了，掉落装备")
boom = Boom()
print(boom.hurt(people_hurt()))