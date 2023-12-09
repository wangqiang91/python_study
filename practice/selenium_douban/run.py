import unittest
from testmovie import Test_Movie
from HTMLTestRunner import HTMLTestRunner

suit = unittest.TestSuite()
suit.addTest(unittest.makeSuite(Test_Movie))

with open('xxx/port.html','wb') as f:
    runner = HTMLTestRunner(f,title="测试报告")
    runner.run(suit)