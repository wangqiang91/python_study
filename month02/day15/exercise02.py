import pymysql
con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database="exercise",
        charset="utf8"
    )
cur = con.cursor()
def user_check(func):
    def wrapper(*args,**kwargs):
        sql01 = "select id from user where username = %s and password = %s;"
        cur.execute(sql01,["hh1","123456"])
        if cur.fetchone():
            func(*args,**kwargs)
        else:
            print("请先注册或登录账号")
    return wrapper
def browse():
    print("浏览商品")

@user_check
def shopping():
    print("开始购物")

@user_check
def buy():
    print("开始付款")


if __name__ == "__main__":
    browse()
    shopping()
    buy()