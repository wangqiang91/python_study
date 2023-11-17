import unittest
from HTMLTestRunner import HTMLTestRunner
from test01_search import TestSearch

suit = unittest.TestSuite()
suit.addTest(unittest.makeSuite(TestSearch))
with open(r"month04\0309\report.html","wb") as f:
    runner = HTMLTestRunner(f,title="测试报告")
    runner.run(suit)
