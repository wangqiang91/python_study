"""
    二进制文件的写入和提取；
"""

import pymysql
keargs = {"host":"localhost","port":3306,"user":"root","password":"123456","database":"stu","charset":"utf8"}
db = pymysql.connect(**keargs)
cur = db.cursor()
# 写入文件
# sql = "update class set image = %s where id = 1;"
# with open(r"month02\day15\testimage.jpeg","rb") as o:
#     data = o.read()
# cur.execute(sql,[data])
# db.commit()

# 提取文件
sql1 = "select name,image from class where id = 1;"
cur.execute(sql1)
name,image = cur.fetchone()
with open("month02\day15\\"+name + ".jpeg","wb") as o:
    o.write(image)