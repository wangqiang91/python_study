import requests
import json
from time import sleep

def get_phone_code(phone_num):
    url = "https://open-beta.jiehun.com.cn/user/account/post-sent-sms"
    data = {
        "securityCode": "31805b3e0e1f055e9bc4064529d4e6cd",
	    "phone": phone_num
    }
    data = json.dumps(data)
    header = {
        "content-type":"application/json",
    }
    res = requests.post(url,data,headers=header).text
    if "成功" in res:
        print(f"{phone_num}获取验证码成功")

def user_regist(phone_num):
    url = "https://open-beta.jiehun.com.cn/user/account/post-code-login"
    data = {
        "phone": phone_num,
    	"completSwitch": False,
    	"referer": "hunbasha_ios",
    	"code": "123456"
    }
    data = json.dumps(data)
    header = {
        "content-type":"application/json",
    }
    res = requests.post(url,data,headers=header).text
    if "" in res:
        print(f"{phone_num}注册登录成功")
def become_manager(phone_num):
    url = "https://open-beta.zghbh.com/tk/portal/web/user"
    data = {
        "deptId": "100",
        "staffName": "预发"+phone_num[-4:],
        "mobile": phone_num,
        "staffStatus": 0,
        "status": "0",
        "postIds": [],
        "roleIds": [
            "1"
        ],
        "cityIds": "110900,510100,440100,330100,310900,120300,420100"
    }
    data = json.dumps(data)
    header = {
        "content-type":"application/json",
        "authorization":"3a908e56-bb27-48df-bb5c-31549345b7c0"
    }
    res = requests.post(url,data,headers=header).text
    if "success" in res:
        print(f"{phone_num}运营后台人员添加成功")
def run(phone_num):
    get_phone_code(phone_num)
    sleep(1)
    user_regist(phone_num)
    sleep(1)
    become_manager(phone_num)
    sleep(1)

phone_list = ["19999990062","19999990063","19999990064","19999990065","19999990066",
"19999990067","19999990068","19999990069","19999990070"]
for item in phone_list:
    run(item)
