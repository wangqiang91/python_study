"""练习"""

class Gamer:
    def __init__(self,gamer,blood,attacker):
        self.gamer = gamer
        self.blood = blood
        self.attacker = attacker
    
    def surplus_blood(self,enemy_attacker):
        self.blood -= enemy_attacker

    def attack_enemy(self,enemy):
        print(f"{self.gamer}攻击敌人,敌人受伤了")
        enemy.surplus_blood(self.attacker)
        print(f"敌人减少了{self.attacker}点血量,敌人还剩余{enemy.blood}血量")
        

class Enemy:
    def __init__(self,blood,attacker):
        self.blood = blood
        self.attacker = attacker
    def surplus_blood(self,gamer_attacker):
        self.blood -= gamer_attacker
    def attack_gamer(self,gamer):
        print(f"敌人攻击{gamer.gamer},玩家受伤了")
        gamer.surplus_blood(self.attacker)
        print(f"{gamer.gamer}减少了{self.attacker}点血量,玩家还剩余{gamer.blood}血量")

gamer = Gamer("大奶",20000,700)
enemy = Enemy(20000,100)
for i in range(100):
    gamer.attack_enemy(enemy)
    if enemy.blood <= 0:
        print("敌人死亡了，掉落装备")
        break
    enemy.attack_gamer(gamer)
    if gamer.blood <= 0:
        print("玩家死亡，游戏结束")
        break 