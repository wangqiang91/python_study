"""
    跨类调用
"""

class Person:
    def __init__(self,name=""):
        self.name = name
        # 写法2 只创建一次，开同一辆车 ：
        # self.car = Car()
    def go_to(self,car):  #写法1  通过参数传递对象，比较灵活
        # 写法3 直接创建对象，每次开新车：
        # car = Car()
        print(f"{self.name}{car.run()}去东北")
class Car:
    def run(self):
        return "坐汽车"

a = Person("大牛")
print(a.go_to(Car()))


"""练习"""

class Name:
    def __init__(self,name):
        self.name = name
        # self.how = How()  # 每次都是同一个保洁打扫
    def clean_room(self,how):
        # how = How()   #每次用新的保洁打扫
        print(f"{self.name}{how.clean_keeping()}打扫卫生")
class How:
    def clean_keeping(self):
        return "请保洁阿姨"

Name("老王").clean_room(How())

class Game:
    def __init__(self,gamer):
        self.gamer = gamer
        self.reduce = Reduce_blood()
    def attack(self,enemy,attack_stren):
        print(f"{self.gamer}攻击敌人,{enemy.reduce_blood()}\
({enemy.description(attack_stren)})")
    def attack_user(self,user,blood):
        print(f"敌人攻击{self.gamer},{user.description_user(blood)}")
class Reduce_blood:
    def reduce_blood(self):
        return "敌人受伤"
    def description(self,blood):
        return (f"玩家攻击力{blood},敌人丢失{blood}点血")
    def description_user(self,blood):
        return (f"玩家丢失{blood//2}点血")
Game("阿豆").attack(Reduce_blood(),60)
Game("阿豆").attack_user(Reduce_blood(),60)

class GetMoney:
    def __init__(self,master):
        self.master = master
    def teach_gonfu(self,apprentices,gongfu):
        print(f"{self.master}教{apprentices}{gongfu}")
    def get_money(self,money):
        print(f"{self.master}赚了{money}元")
GetMoney("张无忌").teach_gonfu("赵敏","九阳神功")
GetMoney("张无忌").get_money(5000)
    