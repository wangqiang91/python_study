"""员工信息管理系统"""

class EmployeeModel:
    def __init__(self,id=0,name="",age=0,sex="男",salary=1000):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary

class EmployeeView:
    def __init__(self):
        self.controller = EmployeeController()
    def show_menus(self):
        print("1键添加员工信息")
        print("2键查看员工信息")
        print("3键删除员工信息")
        print("4键修改员工信息")
    def select_menu(self):
        control = int(input("请选择操作:"))
        if control == 1:
            self.add_employee()
        elif control == 2 :
            self.display_employee()
        elif control == 3:
            self.delete_employee()
        elif control == 4 :
            self.update_employee()
    def add_employee(self):
        model = EmployeeModel()
        model.name = input("请输入员工姓名:")
        model.age = int(input("请输入员工年龄:"))
        model.sex = input("请输入员工性别(男/女):")
        model.salary = int(input("请输入员工工资:"))
        self.controller.add_employee_message(model)
    def display_employee(self):
        for item in self.controller.emlpoyee_list:
            print(f"编号:{item.id},姓名:{item.name},年龄{item.age},性别{item.sex},薪资{item.salary};")
    def delete_employee(self):
        impolyee_id = int(input("请输入要删除的员工ID:"))
        if self.controller.delete_empolyee_message(impolyee_id):
            print("删除成功")
        else:
            print("删除失败")
    def update_employee(self):
        model = EmployeeModel()
        model.id = int(input("请输入要修改员工的ID:"))
        model.age = int(input("请输入修改后员工的年龄:"))
        model.name = input("请输入修改后员工的名字:")
        model.sex = input("请输入修改后员工的性别:")
        model.salary = int(input("请输入修改后员工的工资:"))
        if self.controller.update_employee_message(model):
            print("修改成功")
        else:
            print("修改失败")


class EmployeeController():
    start_id = 10000
    @classmethod
    def set_employee_id(cls,model):
        model.id = cls.start_id
        cls.start_id += 1
    def __init__(self):
        self.emlpoyee_list = []
    def add_employee_message(self,model):
        """
            添加员工信息
            :param model:EmployeeModel类型入参;
        """
        EmployeeController.set_employee_id(model)
        self.emlpoyee_list.append(model)
    def delete_empolyee_message(self,impolyee_id):
        """
            删除员工信息;
            :param impolyee_id:员工ID,根据这个ID删除列表中的数据;
            :return:返回布尔类型数据给EmployeeView类的delete_employee方法;
        """
        for i in range(len(self.emlpoyee_list)):
            if self.emlpoyee_list[i].id == impolyee_id:
                del self.emlpoyee_list[i]
                return True
        return False
    def update_employee_message(self,model):
        """
            修改商品信息;
            :param model:EmployeeModel类型数据;使用__dict__修改全部信息;
        """
        for item in self.emlpoyee_list:
            if item.id == model.id:
                item.__dict__ = model.__dict__
                return True
        return False

empolyee = EmployeeView()
while True:
    empolyee.show_menus()
    empolyee.select_menu()