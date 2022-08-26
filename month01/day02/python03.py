"""
    变量、变量语法、删除语句
    程序运行在内存中；
    程序在处理什么？  数据
"""

# data01 = "a"

data02,data03 = "a","b"

data04 = data02 + data03
data03 = "c"
print(data04)
del data02
print(data04)