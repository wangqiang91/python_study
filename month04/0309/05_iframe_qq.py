from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


# 加速度函数
def get_tracks(distance):
    v = 0
    t = 0.3
    tracks = []
    current = 0
    mid = distance * 4/5
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        s = v0 * t + 0.5 * a * (t ** 2)
        current += s
        tracks.append(round(s))
        v = v0 + a * t

    tracks += [1,3,5,-2,3,-5,-1,3,-3,2]

    # tracks:[第1个0.3s的位移,第2个0.3s的位移,..]
    return tracks



driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url="https://mail.qq.com/")

# 切换iframe
driver.switch_to.frame("login_frame")

# QQ号、密码、登录
driver.find_element(By.XPATH, '//*[@id="u"]').send_keys("30935365")
driver.find_element(By.XPATH, '//*[@id="p"]').send_keys("suibianxiede")
driver.find_element(By.XPATH, '//*[@id="login_button"]').click()

# 出现滑块验证码,新的iframe子页面
time.sleep(2)
driver.switch_to.frame("tcaptcha_iframe")

# 鼠标按住并保持
node = driver.find_element(By.XPATH, '//*[@id="tcaptcha_drag_button"]')
ActionChains(driver).click_and_hold(node).perform()

# 水平向右拖拽一定像素
# 前160个像素快速滑动
ActionChains(driver).move_to_element_with_offset(node, xoffset=160, yoffset=0).perform()

# 快到缺口位置时放慢速度
tracks = get_tracks(40)
for track in tracks:
    ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()

# 释放鼠标
time.sleep(0.5)
ActionChains(driver).release().perform()













