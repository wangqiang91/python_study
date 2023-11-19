"""
    selenium操作鼠标
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.maximize_window()
node = driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]')
mouce = ActionChains(driver)
mouce.move_to_element(node).perform()
driver.find_element(By.LINK_TEXT,"高级搜索").click()