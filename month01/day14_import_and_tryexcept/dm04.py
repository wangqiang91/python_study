

class Wife:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 20 <= value <= 30: 
            self.__age = value
        else:
            raise Exception ("输入有误","E1001")
while True:
    try:
        age = int(input("请输入年龄："))
        print(Wife(age).__dict__)
        break
    except Exception as e:
        print(e)
 
