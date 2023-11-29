import unittest
from test01_login import Test_Login
from test02_content_center import Content_Manage
from HTMLTestRunner import HTMLTestRunner
suit = unittest.TestSuite()
# suit.addTest(unittest.makeSuite(Test_Login))
# suit.addTest(Content_Manage('test_content_list'))
case_path=r'practice\selenium_yugong'

get_case=unittest.defaultTestLoader.discover(case_path,'test*.py')

# runner = unittest.TextTestRunner()
# runner.run(suit)
with open (r"practice\selenium_yugong\report.html","wb") as f:
    runner = HTMLTestRunner(f,title="测试报告")
    runner.run(get_case)