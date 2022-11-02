'''
    排序
'''

list_num = [3,6,65,45,3,4242,43,564,42,43,5]
#取数据
for i in range(0,len(list_num)-1):
    #做比较
    for j in range(i+1,len(list_num)):
        #找更大
        if list_num[i] < list_num[j]:
            #做交换
            list_num[i],list_num[j] = list_num[j],list_num[i]
print(list_num)