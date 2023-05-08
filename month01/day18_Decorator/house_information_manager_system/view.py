import sys
from bll import HouseManagerController
class HouseView:
    def __init__(self) -> None:
        self.housecontro = HouseManagerController()
    def main(self):
        while True:
            self.view_menu()
            self.select_meny()
    def view_menu(self):
        print("按0键退出程序")
        print("按1键查看全部房源信息")
        print("按2键显示总价最高的房源信息")
        print("按3键显示面积最小的房源信息")
        print("按4键根据总价升序显示房源信息")
        
    def select_meny(self):
        data = int(input("请输入您要操作的数字："))
        if data == 0:
            sys.exit()
        if data == 1:
            self.housecontro.view_house_lists()
        if data == 2:
            self.housecontro.view_max_price_method2()
        if data == 3:
            self.housecontro.view_min_area()
        if data == 4:
            self.housecontro.sort_lists_asc()
if __name__ == "__main__":
    HouseView().main()
    
