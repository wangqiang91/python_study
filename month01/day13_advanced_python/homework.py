list_merge = [2,2,2,0]

def merge_sort(list_target):
    for i in range(-1,-(len(list_target)),-1):
        if list_target[i] == 0 :
            del list_target[i]
            list_target.append(0)

def merge_merge(list_target):
    merge_sort(list_target)
    for i in range(0,len(list_target)-1):
        if list_target[i] == list_target[i+1]:
            list_target[i] += list_target[i+1]
            del list_target[i+1]
            list_target.append(0)

merge_merge(list_merge)
print(list_merge)