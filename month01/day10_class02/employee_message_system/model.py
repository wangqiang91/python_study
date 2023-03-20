class EmployeeModel:
    def __init__(self,id=0,name="",age=0,sex="男",salary=1000):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary
    """设置工资最少5000"""
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,value):
        if value < 5000: value = 5000
        self.__salary = value
    def __str__(self):
        return f"编号:{self.id},姓名:{self.name},年龄{self.age},性别{self.sex},薪资{self.salary};"
    def __eq__(self, other) :
        return self.id == other.id