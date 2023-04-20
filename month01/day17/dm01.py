"""
    lambda(匿名方法):函数只能有一条语句； 不支持赋值语句；
    lambda能定义的函数，def都可以定义；
"""
def func01(p1,p2):
    return p1 > p2
print(func01(3,5))
# 对应的匿名方法
data1 = lambda p1,p2:p1 > p2
print(data1(3,5))


def func02(p1):
    print("返回值是：",p1)
func02(230)
# 对应的匿名方法
data2 = lambda p1 : print("返回值是：",p1)
data2(230)


def fun03():
    return 100
print(fun03())
# 对应的匿名方法
data3 = lambda : 100
print(data3())


def func04():
    for i in range(20):
        print(i)
# data3 = lambda : for i in range(20) : print(i)  #错误的写法，lambda函数只能有一条语句；