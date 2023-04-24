"""
    标准装饰器
"""
def verify_permissions(fun):
    def wrapper(*args,**kargs):
        print("验证权限")
        res = fun(*args,**kargs)
        return res
    return wrapper
@verify_permissions
def insert(data):
    print(f"插入{data}成功")
@verify_permissions
def delete():
    print("删除")
    return "True"

# insert = verify_permissions(insert)
insert("data001")
print(delete())