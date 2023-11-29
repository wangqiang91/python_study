from time import sleep
from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from parameterized import parameterized
login_fail_list = [("12345678901","123456","用户不存在"),("13052256330","12345678","密码错误")]
class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get("http://yg.test.zghbh.com/")
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
    @parameterized.expand(login_fail_list)
    def test_login_fail(self,usern,pwd,msg):
        username = self.driver.find_element('xpath','//*[@placeholder="账号"]')
        username.clear()
        username.send_keys(usern)
        password = self.driver.find_element('xpath','//*[@placeholder="密码"]')
        password.clear()
        password.send_keys(pwd)
        verification = self.driver.find_element('xpath','//*[@placeholder="验证码"]')
        verification.send_keys("1")
        self.driver.find_element('xpath','//*[@type="button"]').click()
        message = self.driver.find_element('xpath','/html/body/div[2]/div/h2').text
        print(message)
        self.assertIn(msg,message)
        sleep(5)
    def test_login_success(self):
        username = self.driver.find_element('xpath','//*[@placeholder="账号"]')
        username.clear()
        username.send_keys("19999990062")
        password = self.driver.find_element('xpath','//*[@placeholder="密码"]')
        password.clear()
        password.send_keys("123456")
        verification = self.driver.find_element('xpath','//*[@placeholder="验证码"]')
        verification.send_keys("1")
        sleep(1)
        self.driver.find_element('xpath','//*[@type="button"]').click()
        data= ('xpath','/html/body/div/section/section[1]/div/div/div[1]/div/ul/div[1]/li/div/span')
        nrzx = WebDriverWait(self.driver,10,poll_frequency=0.5).until(lambda x:x.find_element(*data)).text
        self.assertEqual("内容中心",nrzx)

        
if __name__ == "__main__":
    unittest.main()