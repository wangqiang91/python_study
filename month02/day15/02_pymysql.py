import pymysql
keargs = {"host":"localhost","port":3306,"user":"root","password":"123456","database":"stu","charset":"utf8"}
db = pymysql.connect(**keargs)
cur = db.cursor()
data = [("li",23,"w",78),("lei",14,"w",95),("ma",19,"w",108),("ha",23,"w",71)]
try:
    sql_update = "update class set score = 95 where id = 1;"
    cur.execute(sql_update)
    sql_update2 = "update class set score = %s where name = %s;"
    cur.execute(sql_update2,[80,"王三欢"])
    # 使用execute的传值功能时，sql语句需要传入的值不管什么类型都用%s代替，然后在execute传入一个列表或元祖代表这些值就可以；
    sql_insert = "insert into class (name,age,sex,score) values (%s,%s,%s,%s);"
    cur.executemany(sql_insert,data)  #相当于for循环执行execute；
except Exception as e:
    print(e)
    db.rollback()
else:
    db.commit()
cur.close()
db.close()
