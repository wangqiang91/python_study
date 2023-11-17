import json
import unittest
import requests
from time import sleep
from parameterized import parameterized 
import pymysql
# 存放测试数据方式1: 直接写在变量中；
data_list = [("237","成功"),("x237","")]
# 存放测试数据方式2：读取数据库的值；
def build_data_mysql():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="school",
        charset="utf8"
    )
    cur = conn.cursor()
    sql = "select tabid,message from login_data;"
    cur.execute(sql)
    return cur.fetchall()
# 存放测试数据方式3：读取json文件的值；
def build_data():
    data_list = []
    with open(r"month04\0309\data\search.json","r",encoding="utf8") as f:
        data = f.read()
        data = json.loads(data)
        for item in data:
            data_list.append((item["id"],item.get("message")))
    return data_list
class TestSearch(unittest.TestCase):
    @parameterized.expand(build_data_mysql())
    def test01_search_236(self,id,message):
        url = "http://open.test.jiehun.com.cn/search/content/app/home/feed/community/list"
        data = {
            "tabId": id,
            "pageSize": 20,
            "scrollId": "",
            "page": 1
        }
        data = json.dumps(data)
        header = {
            "Content-Type":"application/json",
            "device-id":"C3C84F9B-5263-4970-B194-D04ECD8A3808",
            "city-id":"330100"}
        res = requests.post(url,data,headers=header).json()
        self.assertEqual(res["message"],message)
        sleep(1)
if __name__ == "__main__":
    unittest.main()
    # print(build_data())
    # build_data_mysql()