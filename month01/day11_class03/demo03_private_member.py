"""
    私有成员  __func、__variable:
        作用：类外无法访问，类内可以使用；
        语法：以双下划线为开头命名； 
        本质: 看上去是私有变量名__data
        实际上是单下划线+类名+双下划线+变量名/方法名(外部写成
        这种格式时可以被使用)
"""
class MyClass:
    def __init__(self,data=10):
        self.__data = data
    def __func01(self):
        print(self.__data)
    def func02(self):
        print(self.__data)
        self.__func01()

# MyClass().__func01()
# print(MyClass().__data)
print(MyClass()._MyClass__data)
MyClass()._MyClass__func01()
MyClass().func02()