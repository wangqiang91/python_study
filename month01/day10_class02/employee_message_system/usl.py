import sys
from bll import EmployeeController
from model import EmployeeModel

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

    def __get_number(self,description):
        """
            用户手动输入，防止输入错误，若输入错误，给出提示； 
        """
        while True:
            try:
                number = int(input(description))
                return number
            except:
                print("输入异常，请重新输入")

    def __select_menu(self):
        control =self.__get_number("请选择操作:")
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
        model.age = self.__get_number("请输入员工年龄:")
        model.sex = input("请输入员工性别(男/女):")
        model.salary = self.__get_number("请输入员工工资:")
        self.__controller.add_employee_message(model)

    def __display_employee(self):
        #employee_list设置只读属性后，引用时无需用__；
        for item in self.__controller.employee_list:
            print(item)
    
    def __delete_employee(self):
        impolyee_id = self.__get_number("请输入员工编号：")
        if self.__controller.delete_empolyee_message(impolyee_id):
            print("删除成功")
        else:
            print("删除失败")

    def __update_employee(self):
        model = EmployeeModel()
        model.id = self.__get_number("请输入要修改员工的ID:") 
        # model.age = int(input("请输入修改后员工的年龄:"))
        model.age = self.__get_number("请输入修改后员工的年龄:") 
        model.name = input("请输入修改后员工的名字:")
        model.sex = input("请输入修改后员工的性别:")
        model.salary = int(input("请输入修改后员工的工资:"))
        if self.__controller.update_employee_message(model):
            print("修改成功")
        else:
            print("修改失败")
