from model import EmployeeModel

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
