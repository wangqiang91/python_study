import sys
class GameView:
    def __init__(self,item_list):
        self.controller = GameController()
        self.item_list = item_list
    def main(self):
        self.initialization_interface()
        self.view_menu()
        self.get_user_input()
    def initialization_interface(self):
        for item in self.item_list:
            for number in item:
                print(number,end=" ")
            print("\n")
    def view_menu(self):
        print("1.输入w向上移动;")
        print("2.输入s向下移动;")
        print("3.输入a向左移动;")
        print("4.输入d向右移动;")
        print("5.输入quit退出程序")
    def get_user_input(self):
        data = input("请输入字符：")
        if data == "w":
            self.controller.to_up_more(self.item_list)
            self.initialization_interface()
        elif data == "s":
            self.controller.to_down_more(self.item_list)
            self.initialization_interface()
        elif data == "a":
            self.controller.to_left_more(self.item_list)
            self.initialization_interface()
        elif data == "d":
            self.controller.to_right_more(self.item_list)
            self.initialization_interface()
        elif data == "quit":
            sys.exit()
        else:
            print("输入异常")
            
            
class GameController:
    def zero_to_end(self,list_target):
        for i in range(-1,-(len(list_target)+1),-1):
            if list_target[i] == 0 :
                del list_target[i]
                list_target.append(0)

    def merge_merge(self,list_target):
        self.zero_to_end(list_target)
        for i in range(len(list_target)-1):
            if list_target[i] == list_target[i+1]:
                list_target[i] += list_target[i+1]
                del list_target[i+1]
                list_target.append(0)

    def to_left_more(self,list_targets):
        for item in list_targets: 
            self.merge_merge(item)

    def to_right_more(self,list_targets):
        for item in list_targets:
            item[::-1] = item
            self.merge_merge(item)
            item[::-1] = item

    def squre_matrix_transposition(self,list_targets):
        new_list_targets = [list(item) for item in zip(*list_targets)]
        list_targets[:] = new_list_targets

    def to_up_more(self,list_targets):
        self.squre_matrix_transposition(list_targets)
        # print(list_targets)
        self.to_left_more(list_targets)
        # print(list_targets)
        self.squre_matrix_transposition(list_targets)
        # print(list_targets)

    def to_down_more(self,list_targets):
        self.squre_matrix_transposition(list_targets)
        self.to_right_more(list_targets)
        self.squre_matrix_transposition(list_targets)
    
if __name__ == "__main__":
    # merge_merge(list_merge)
    # print(list_merge)
    list_merge = [4,4,4,4]
    map = [
        [2,0,0,2],
        [4,2,0,2],
        [2,4,2,4],
        [0,4,0,4]
    ]
    GameView(map).main()