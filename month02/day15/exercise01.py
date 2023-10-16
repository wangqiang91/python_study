# 将dict.txt中的数据，写入表words中；
import pymysql
class insert_word:
    def __init__(self):
        self.con = self.con_mysql()
        self.cur = self.con.cursor()
    def con_mysql(self):
        con = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="123456",
            database="dict",
            charset="utf8"
            )
        return con
    def get_dict_data(self):
        open_dict = open(r"month02\day03\dict.txt",encoding="utf-8")
        values_list = []
        for line in open_dict:
            tmp = line.split(" ",1)
            values_list.append((tmp[0],tmp[1].strip()))
        open_dict.close()
        return values_list
    def insert_data(self):
        sql_insert = "insert into words (word,mean) values (%s,%s);"
        try:
            self.cur.executemany(sql_insert,self.get_dict_data())
        except Exception as e:
            print(e)
            self.con.rollback()
        else:
            self.con.commit()
    def close(self):
        self.con.close()
        self.cur.close()

if __name__ == "__main__":
    insert_word().insert_data()
    insert_word().close()
