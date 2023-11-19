from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
class YuGong:
    def __init__(self):
        self.driver = webdriver.Firefox()        
        # self.driver.get('http://yg.test.zghbh.com/login')
        self.driver.get("https://book.douban.com/top250")
        self.driver.maximize_window()

    def input_username(self):
        user_name = self.driver.find_element(By.XPATH,"/html/body/div/section/div/form/div[1]/div/div/input")
        user_name.clear()
        user_name.send_keys("13052256330")
    def input_password(self):
        password = self.driver.find_element(By.XPATH,"/html/body/div/section/div/form/div[2]/div/div/input")
        password.clear()
        password.send_keys("1234567")
    def get_books(self):
        tab_list = self.driver.find_elements(By.XPATH,'//*[@id="content"]/div/div[1]/div/table')
        for item in tab_list:
            print(item.text)
            print("*" * 50)
        # self.driver.quit()
    def get_all_books(self):
        while True:
            self.get_books()
            try:
                self.driver.find_element(By.PARTIAL_LINK_TEXT,"后页").click()
                sleep(2)
            except Exception as e:
                break
    def main(self):
        self.input_username()
        self.input_password()
        sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    YuGong().get_all_books()

