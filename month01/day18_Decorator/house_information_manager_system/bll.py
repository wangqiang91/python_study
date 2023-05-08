"""
    业务逻辑层
""" 
from dal import HouseDao


class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()
    def view_house_lists(self):
        for item in self.__list_houses:
            print(item.__dict__)

    def view_max_price(self):
        print(max(self.__list_houses,key=lambda item : item.total_price).__dict__)

    def view_max_price_method2(self):
        print(max(self.__list_houses).__dict__)

    def view_min_area(self):
        print(min(self.__list_houses,key=lambda item : item.area).__dict__)
        
    def sort_lists_asc(self):
        new_house_list = sorted(self.__list_houses,key=lambda item:item.total_price)
        for item in new_house_list:
            print(item.__dict__)
    

