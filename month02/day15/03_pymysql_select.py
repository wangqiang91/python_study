# mysql查询数据

import pymysql
keargs = {"host":"localhost","port":3306,"user":"root","password":"123456","database":"stu","charset":"utf8"}
db = pymysql.connect(**keargs)
cur = db.cursor()
sql01 = "select name,age,score from class where score > %s;"
cur.execute(sql01,[70])
# 获取数据方法1:for循环迭代cur，每次返回一条记录； 
for row in cur:
    print(row)
# 获取数据方法2：使用函数fetchone()获取一条，使用函数fetchmany(n)获取n条，使用fetchall()获取所有数据；返回一条数据是元祖，多条是元祖套元祖；
print(cur.fetchone())
print(cur.fetchmany(5))
print(cur.fetchall())