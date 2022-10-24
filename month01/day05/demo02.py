'''
    深浅拷贝
    浅拷贝  复制第一层数据，共享深层数据
            优点：节省内存空间
            缺点：深层数据被修改互相影响；
    深拷贝  复制所有层数据，互不影响
            优点：绝对互补影响
            缺点：占用内用空间较大
'''
#浅拷贝  复制第一层数据，共享深层数据
list01 = [10,[20,30]]
list02 = list01[:] #触发浅拷贝：复制一层的数据
list01[0] = 100 #修改一层数据，不影响list02
list01[1][1] = 300 #修改二层数据，互相影响
print(list02)

#深拷贝  复制所有层数据，互不影响
import copy
list03 = [10,[20,30]]
list04 = copy.deepcopy(list03)
list03[0] = 100
list03[1][1] = 300
print(list04)

list01 = ["北京",["上海","深圳"]]
list02 = list01
list03 = list01[:]
list04 = copy.deepcopy(list01)
list04[0] = "北京04"
list04[1][1] = "深圳04"
print(list01)
list03[0] = "北京03"
list03[1][1] = "深圳03"
print(list01)
list02[0] = "北京02"
list02[1][1] = "深圳02"
print(list01)