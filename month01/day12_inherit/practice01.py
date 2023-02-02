class Colour:
    def __init__(self,r,g,b,a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
    def __eq__(self,other):
        return self.__dict__ == other.__dict__
    def __lt__(self,other):
        if self.r != other.r:
            return self.r < other.r
        elif self.g != other.g:
            return self.g < other.g
        elif self.b != other.b:
            return self.b < other.b
        else:
            return self.a < other.a
        # return self.r < other.r

list1 = [
    Colour(1,1,1,2),
    Colour(2,2,1,1),
    Colour(1,1,1,3),
    Colour(4,4,4,4),
    Colour(4,5,1,1),
]
print(Colour(1,1,1,1) in list1)
print(list1.count(Colour(1,1,1,1)))
print(min(list1).__dict__)
print("=="*10)
print(max(list1).__dict__)
print("=="*10)
list1.sort(reverse=True)
for item in list1:
    print(item.__dict__)
