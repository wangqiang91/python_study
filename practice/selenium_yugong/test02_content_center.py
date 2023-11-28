from time import sleep
from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait

class Content_Manage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get('http://yg.test.zghbh.com/login')
        username = cls.driver.find_element('xpath','//*[@placeholder="账号"]')
        username.clear()
        username.send_keys("13052256330")
        password = cls.driver.find_element('xpath','//*[@placeholder="密码"]')
        password.clear()
        password.send_keys("123456")
        verification = cls.driver.find_element('xpath','//*[@placeholder="验证码"]')
        verification.send_keys("1")
        cls.driver.find_element('xpath','//*[@type="button"]').click()
        data = ('xpath','//*[@id="cns-main-app"]/section[1]/div/div/div[1]/div/ul/div[1]/li/div')
        WebDriverWait(cls.driver,5,poll_frequency=0.5).until(lambda x:x.find_element(*data)).click()
        cls.driver.find_element('xpath','//*[@id="cns-main-app"]/section[1]/div/div/div[1]/div/ul/div[1]/li/ul/div[8]/li/div').click()
    def test_content_list(self):
        pass
    
if __name__ == "__main__":
    unittest.main()