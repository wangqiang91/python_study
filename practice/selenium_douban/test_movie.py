from time import sleep
from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
class Test_Movie(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get("https://movie.douban.com/")
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.close()
    def test01_select(self):
        ele = ('xpath','//*[@id="inp-query"]')
        WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_element(*ele)).send_keys("龙的传人")
        self.driver.find_element('xpath','//*[@id="db-nav-movie"]/div[1]/div/div[2]/form/fieldset/div[2]/input').click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,10000);")
        sleep(1)
        data = self.driver.find_element('xpath','//*[@id="root"]/div/div[2]/div[1]/div[1]/div[6]/div/div/div[1]/a').text
        print(data)
        self.assertIn("龙的传人",data)
        self.driver.back()
    def test02_buy_ticket(self):
        self.driver.find_element('xpath','/html/body/div[3]/div[1]/div/div[2]/div[1]/div[1]/h2/span[1]/a').click()
        ele1 = ('xpath','//*[@id="33456512"]/ul/li[4]/a')
        WebDriverWait(self.driver,10,poll_frequency=0.5).until(lambda x:x.find_element(*ele1)).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        sleep(2)
        self.driver.find_element('xpath','//*[@id="content"]/div/div[1]/div[1]/button[1]').click()
        sleep(2)
        ele2 = self.driver.find_element('xpath','//*[@id="app"]/div[1]/ul/li[4]/ul')
        self.driver.execute_script("arguments[0].scrollIntoView();",ele2)
        ele3 = self.driver.find_element('xpath','//*[@id="app"]/div[2]/h2/div/span')
        ActionChains(self.driver).move_to_element(ele3).perform()
        sleep(1)
        self.driver.find_element('xpath','//*[@id="app"]/div[2]/h2/div/ul/li[2]/a').click()
        sleep(2)
        self.driver.close()
if __name__ == "__main__":
    unittest.main()