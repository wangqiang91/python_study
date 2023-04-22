"""
    闭包：必须有一个内嵌函数、内嵌函数必须引用外部函数的变量、外部函数返回值必须是内嵌函数；
"""
def func01():
    a = 10
    def func02():
        print(a)
    return func02
func01()()
