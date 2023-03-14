"""员工信息管理系统"""

import sys

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

class EmployeeView:
    def __init__(self):
        self.__controller = EmployeeController()
    def main(self):
        while True:
            self.__show_menus()
            self.__select_menu()
        
    def __show_menus(self):
        print("1键添加员工信息")
        print("2键查看员工信息")
        print("3键删除员工信息")
        print("4键修改员工信息")
        print("0键退出")

    def __select_menu(self):
        control = int(input("请选择操作:"))
        if control == 1:
            self.__add_employee()
        elif control == 2 :
            self.__display_employee()
        elif control == 3:
            self.__delete_employee()
        elif control == 4 :
            self.__update_employee()
        elif control == 0 :
            print("已退出程序")
            sys.exit()

    def __add_employee(self):
        model = EmployeeModel()
        model.name = input("请输入员工姓名:")
        model.age = int(input("请输入员工年龄:"))
        model.sex = input("请输入员工性别(男/女):")
        model.salary = int(input("请输入员工工资:"))
        self.__controller.add_employee_message(model)

    def __display_employee(self):
        #employee_list设置只读属性后，引用时无需用__；
        for item in self.__controller.employee_list:
            print(item)
    
    def __delete_employee(self):
        impolyee_id = int(input("请输入要删除的员工ID:"))
        if self.__controller.delete_empolyee_message(impolyee_id):
            print("删除成功")
        else:
            print("删除失败")

    def __update_employee(self):
        model = EmployeeModel()
        model.id = int(input("请输入要修改员工的ID:"))
        model.age = int(input("请输入修改后员工的年龄:"))
        model.name = input("请输入修改后员工的名字:")
        model.sex = input("请输入修改后员工的性别:")
        model.salary = int(input("请输入修改后员工的工资:"))
        if self.__controller.update_employee_message(model):
            print("修改成功")
        else:
            print("修改失败")


class EmployeeController():
    """设置开始编号为类变量，多人引用时，存的数据也是有且只有一个；"""
    __start_id = 10000
    @classmethod
    def set_employee_id(cls,model):
        model.id = cls.__start_id
        cls.__start_id += 1

    """设置employee_list为只读属性"""
    def __init__(self):
        self.__employee_list = []
    @property  
    def employee_list(self):
        return self.__employee_list

    def add_employee_message(self,model):
        """
            添加员工信息
            :param model:EmployeeModel类型入参;
        """
        EmployeeController.set_employee_id(model)
        self.__employee_list.append(model)

    def delete_empolyee_message(self,impolyee_id):
        """
            删除员工信息;
            :param impolyee_id:员工ID,根据这个ID删除列表中的数据;
            :return:返回布尔类型数据给EmployeeView类的delete_employee方法;
        """
        # for i in range(len(self.__employee_list)):
        #     if self.__employee_list[i].id == impolyee_id:
        #         del self.__employee_list[i]
        #         return True
        # return False

        model = EmployeeModel(id=impolyee_id)
        if model in self.__employee_list:
            self.__employee_list.remove(model)
            # 由于remove和in内容调用的都是__eq__，所以要重写EmployeeModel的__eq__；
            return True
        return False
    def update_employee_message(self,model):
        """
            修改员工信息;
            :param model:EmployeeModel类型数据;使用__dict__修改全部信息;
        """
        for item in self.__employee_list:
            if item.id == model.id:
                item.__dict__ = model.__dict__
                return True
        return False

empolyee = EmployeeView()
empolyee.main()
