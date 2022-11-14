"""
    形参：
        位置形参：必填
            def 函数名(函数名1,函数名2.。。）
        默认形参：可选
            def 函数名(函数名1,形参名2=数据）
    实参:
        位置实参：按顺序对应
            函数名(数据1,数据2.。。）
        关键字实参：按名称
            函数名(形参名1 = 数据1)
"""

# def func01(p1,p2=10,p3="c"):
#     print(p1,p2,p3)

# func01(45,p3="hah")

def get_seconds(hour=0,minute=0,second=0):
    total_seconds = hour * 3600 + minute * 60 + second
    print(total_seconds)
get_seconds(1,2,23)

