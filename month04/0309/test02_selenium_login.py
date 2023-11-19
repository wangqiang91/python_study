from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from parameterized import parameterized
test_data = [("15989548965","123456","用户不存在"),("13052256330","1234","错误")]
class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://yg.test.zghbh.com/login")
    @classmethod
    def tearDownClass(cls) -> None:
        sleep(2)
        cls.driver.quit()
    @parameterized.expand(test_data)
    def test_login(self,name,pwd,msg):
        username = self.driver.find_element(By.XPATH,"/html/body/div/section/div/form/div[1]/div/div/input")
        username.clear()
        username.send_keys(name)
        password = self.driver.find_element(By.XPATH,"/html/body/div/section/div/form/div[2]/div/div/input")
        password.clear()
        password.send_keys(pwd)
        self.driver.find_element(By.XPATH,"/html/body/div/section/div/form/div[3]/div/div[1]/input").send_keys("1212")
        sleep(5)
        self.driver.find_element(By.XPATH,"/html/body/div/section/div/form/div[4]/div/button/span/span").click()
        # 获取点击登录后返回的信息
        res = self.driver.find_element(By.XPATH,"/html/body/div[2]").text
        # 断言对比预期数据是否在返回的信息中
        self.assertIn(msg,res)
if __name__ == "__main__":
    unittest.main()