'''
    列表内存分布
'''

list01 = [10,20,30,40]

del list01[1]  #删除时后面的元素向前移动； 【优先】使用
list01.remove(30) #删除时先定位位置，再后面的元素向前移动；


list02 = ["北京","上海","深圳"]
#list03和list02传递的是列表地址,同一个列表地址，互相影响；
list03 = list02
#insert 元素向后移动
list03.insert(0,"天津")
#del元素向后移动
del list02[1]
print(list03)