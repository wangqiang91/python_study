"""
    实参 *:将一个序列拆分为多个参数，按顺序对应；
    实参 **：将一个字典拆分为多个参数,按名称对应;
"""
def func01(p1,p2,p3):
    print(p1)
    print(p2)
    print(p3)
list1 = [1,2,3]
func01(*list1)
tuple1 = [4,5,6]
func01(*tuple1)
str1 = "孙悟空"
func01(*str1)

dict01 = {"p2":234,"p1":23,"p3":9878}
func01(*dict01)
func01(**dict01)