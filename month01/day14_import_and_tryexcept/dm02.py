"""
    python程序完整结构
"""
import package01.package01_01.module01 as m
from package01.package01_01.module01 import *

# m.hanshu1()

"""
    包中__init__的作用：
        当导入包时,在__init__中定义可访问成员，包中代码复杂时，可简化逻辑；
"""
import  package01.package01_01 

hanshu1()