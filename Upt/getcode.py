import time

from selenium import webdriver
driver = webdriver.Chrome('D:\DriverConifg\chromedriver')
driver.maximize_window()
driver.get('https://bjjj.zhongchebaolian.com/cgsadm/#/changeindicatormanage/indicatormanage')
time.sleep(2)
code_element = driver.find_element_by_id('imgCode') # 定位到验证码元素

print(code_element.screenshot('./out_img.png'))