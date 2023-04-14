list_merge = [4,4,4,4]

def zero_to_end(list_target):
    for i in range(-1,-(len(list_target)+1),-1):
        if list_target[i] == 0 :
            del list_target[i]
            list_target.append(0)

def merge_merge(list_target):
    zero_to_end(list_target)
    for i in range(len(list_target)-1):
        if list_target[i] == list_target[i+1]:
            list_target[i] += list_target[i+1]
            del list_target[i+1]
            list_target.append(0)

def to_left_more(list_targets):
    for item in list_targets: 
        merge_merge(item)

def to_right_more(list_targets):
    for item in list_targets:
        item[::-1] = item
        merge_merge(item)
        item[::-1] = item

def squre_matrix_transposition(list_targets):
    new_list_targets = [list(item) for item in zip(*list_targets)]
    list_targets[:] = new_list_targets

def to_up_more(list_targets):
    squre_matrix_transposition(list_targets)
    print(list_targets)
    to_left_more(list_targets)
    print(list_targets)
    squre_matrix_transposition(list_targets)
    print(list_targets)

def to_down_more(list_targets):
    squre_matrix_transposition(list_targets)
    to_right_more(list_targets)
    squre_matrix_transposition(list_targets)
    
if __name__ == "__main__":
    # merge_merge(list_merge)
    # print(list_merge)
    map = [
        [2,0,0,2],
        [4,2,0,2],
        [2,4,2,4],
        [0,4,0,4]
    ]
    to_up_more(map)
    print(map) 
    