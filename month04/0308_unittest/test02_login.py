'''
    测试登录模块
'''
import json
import requests
import unittest
from time import sleep
from parameterized import parameterized
data_list = [
    ("123456","13052256330",0),
    ("123456weqe","13052256330",10004),
    ("123456","13052256336",10003)]
class TestLogin(unittest.TestCase):
    @parameterized.expand(data_list)
    def test01_login(self,pwd,name,code):
        """登录成功"""
        url = "http://open.test.jiehun.com.cn/user/account/get-login"
        data = {
            "password": pwd,
            "username": name
        }
        data = json.dumps(data)
        header = {
            "Content-Type":"application/json"
        }
        html = requests.post(url,data,headers=header).json()
        self.assertEqual(html["code"],code)
        sleep(1)
    # def test02_login(self):
    #     """密码错误"""
    #     url = "http://open.test.jiehun.com.cn/user/account/get-login"
    #     data = {
    #         "password": "123456weqe",
    #         "username": "13052256330"
    #     }
    #     data = json.dumps(data)
    #     header = {
    #         "Content-Type":"application/json"
    #     }
    #     html = requests.post(url,data,headers=header).json()
    #     self.assertEqual(html["code"],10004)
    #     sleep(1)
    # def test03_login(self):
        """用户名错误"""
        url = "http://open.test.jiehun.com.cn/user/account/get-login"
        data = {
            "password": "123456",
            "username": "13052256336"
        }
        data = json.dumps(data)
        header = {
            "Content-Type":"application/json"
        }
        html = requests.post(url,data,headers=header).json()
        self.assertEqual(html["code"],1003)
        sleep(1)
if  __name__ == "__main__":
    unittest.main()