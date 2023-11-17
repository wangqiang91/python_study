import unittest
from test02_login import TestLogin
from test01_add import TestAdd
from HTMLTestRunner import HTMLTestRunner
# 1、初始化测试套件
suite = unittest.TestSuite()
# 2、添加测试用例(makeSuite添加整个类)
suite.addTest(TestLogin("test01_login"))
suite.addTest(unittest.makeSuite(TestAdd))
# 3、创建运行器对象（文本形式的测试报告）
# runner = unittest.TextTestRunner()
# 4、执行测试用例
# runner.run(suite)
# 生成html格式测试报告
with open(r"month04\0308_unittest\report.html","wb") as f:
    runner = HTMLTestRunner(f,title = "测试报告")
    runner.run(suite)