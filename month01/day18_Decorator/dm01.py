"""
    装饰器：在不改变旧功能前提下，为其增加新功能；
"""
def verify_permissions(fun):
    def wrapper():
        print("验证权限")
        fun()
    return wrapper
@verify_permissions
def insert():
    print("插入")
@verify_permissions
def delete():
    print("删除")

# insert = verify_permissions(insert)
insert()
delete()