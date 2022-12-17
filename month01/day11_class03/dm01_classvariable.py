"""
    类成员:
        类变量：1.随类的加载而加载； 2.存在优先于对象； 
"""
global_variable = 1000  #全局变量
class ICBC():
    total_money = 1000000   #类变量，通过类名访问；自增/自减 时互相影响；
    def __init__(self,name="",money=0):
        #实例变量,通过对象访问；自增/自减时互不影响；
        self.name = name
        self.money = money
        ICBC.total_money -= self.money
    def func01(self):
        fun_variable = 200 #方法变量，只能方法内部使用

fenhang1 = ICBC("fenhang1",100000)
print(ICBC.total_money)
fenhang2 = ICBC("fenhang2",300000)
print(ICBC.total_money)