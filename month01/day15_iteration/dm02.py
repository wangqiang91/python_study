class StudentNext:
    def __init__(self,item):
        self.item = item
        self.index = -1
    def __next__(self):
        if self.index >= len(self.item)-1:
            raise StopIteration
        self.index += 1
        return (self.item[self.index])

class StudentController:
    def __init__(self):
        self.student_list = []
    def __iter__(self):
        return StudentNext(self.student_list)

stucon = StudentController()
stucon.student_list.append("姓名1")
stucon.student_list.append("姓名2")
stucon.student_list.append("姓名3")

iterator = stucon.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

# practice 01 
class CommodityNext:
    def __init__(self,data):
        self.data = data
        self.index = -1
    def __next__(self):
        if self.index >= len(self.data)-1:
            raise StopIteration
        self.index += 1
        return self.data[self.index]

class CommodityController:
    def __init__(self):
        self.commodity = []
    def add_commodity(self,data):
        self.commodity.append(data)
    def __iter__(self):
        return CommodityNext(self.commodity)

controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")

for item in controller:
    print(item)