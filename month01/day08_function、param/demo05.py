"""
    函数参数-形式参数1(*args,p1,p2):
        实参必须是关键字实参；
    函数参数-形式参数2(*,p1,p2):
        *不用管,但p1、p2一定要用关键字实参，增加代码可读性；
"""

def func01(*args,p1,p2=0):
    print(args)

func01(p1=3)

#如 print
print("我的年龄是",30,"!!",sep="")

