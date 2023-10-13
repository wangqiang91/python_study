import pymysql
keargs = {"host":"localhost","port":3306,"user":"root","password":"123456","database":"stu","charset":"utf8"}
db = pymysql.connect(**keargs)
cur = db.cursor()
try:
    sql_update = "update class set score = 94 where id = 1;"
    cur.execute(sql_update)
except Exception as e:
    print(e)
    db.rollback()
else:
    db.commit()
cur.close()
db.close()
