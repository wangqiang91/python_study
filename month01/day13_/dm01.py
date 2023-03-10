"""
    封装、继承、多态
"""

class CalculateEmployeeSalary:
    def __init__(self) :
        self.employee_list = []
    def add_employee(self,emp):
        self.employee_list.append(emp)
    def calculate_total_salary(self):
        total_salary = 0
        for item in self.employee_list:
            total_salary += item.get_salary()
        return total_salary

class EmployeeSalary:
    def __init__(self,basepay):
        self.basepay = basepay
    def get_salary(self):
        return self.basepay

class Programmer(EmployeeSalary):
    def __init__(self,basepay,program_money):
        self.program_money = program_money
        super().__init__(basepay)
    def get_salary(self):
        salary = super().get_salary() + self.program_money
        return salary

class Tester(EmployeeSalary):
    def __init__(self,basepay,bugs):
        self.bugs = bugs
        super().__init__(basepay)
    def get_salary(self):
        salary = super().get_salary() + self.bugs * 50
        return salary

# ces = CalculateEmployeeSalary()
# ces.add_employee(Programmer(3000,30000))
# ces.add_employee(Tester(3000,50))
# ces.add_employee(Programmer(4000,30000))
# total_salary = ces.calculate_total_salary()
# print(total_salary)

class DeagramManager:
    def __init__(self) :
        self.deagram_list = []
    def add_deagram(self,dea):
        self.deagram_list.append(dea)
    def calculate_area(self):
        total_area = 0
        for item in self.deagram_list:
            total_area += item.get_area()
        return total_area

class Deagram:
    def get_area(self):
        pass

class Circle(Deagram):
    def __init__(self,radius):
        self.radius = radius
    def get_area(self):
        area = 3.14 * (self.radius ** 2)
        return area
class Rectangle(Deagram):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def get_area(self):
        area = self.length * self.width
        return area

dm = DeagramManager()
dm.add_deagram(Circle(10))
dm.add_deagram(Rectangle(20,30))
print(dm.calculate_area())