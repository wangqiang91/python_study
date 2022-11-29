"""
    形参 * args:将多个位置实参合并为一个元祖；
    形参 ** kwargs :将多个关键字实参合并为一个字典；
    价值:让调用者不必自定构建容器存储多个参数,而让python自动构建元祖合并多个参数;
"""

# def  func01(*p):
#     print(p)
# func01()
# func01(1)
# func01(1,2)
# func01(p1=23,p2=45) #不支持关键字实参

# def  func02(**p):
#     print(p)
# func02()
# func02(1,2)  #不支持位置实参
# func02(p1=23,p2=45)

def  func03(p1,p2=5,*args,**kwargs):
    print(p1)
    print(p2)
    print(args)
    print(kwargs)
func03(p1=23)
func03(2,3,5,b1=23,b2=45)  #先写位置实参，再写关键字实参


# def get_multiplication_result(*args):
#     total = 1
#     for item in args:
#         total *= item
#     return total
# print(get_multiplication_result(4,5,8,))