import time
from img import baiduorcapi
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://bjjj.zhongchebaolian.com/cgsadm/#/changeindicatormanage/indicatormanage')
time.sleep(3)
driver.find_element_by_id('username').send_keys('17600352198')
driver.find_element_by_id('password').send_keys('a12345678')
# driver.find_element_by_id('account-img-code').send_keys(code[0]['words'])
# time.sleep(5)
# driver.find_element_by_id('login-btn').click()
# time.sleep(1)
i = -1
while driver.title == '登录':
    i = i+1
    try:
        time.sleep(2)
        code_element = driver.find_element_by_id('imgCode')
        code_element.screenshot('../img/easy_img/code.png')
        code = baiduorcapi.bdocrapi('../img/easy_img/code.png')
        # 判断验证码是否为空
        if not code:
            print('验证码为空')
            time.sleep(2)
            driver.find_element_by_id('account-img-code').send_keys(code[0]['words'])
            driver.find_element_by_id('login-btn').click()
        driver.find_element_by_id('account-img-code').send_keys(code[0]['words'])
        driver.find_element_by_id('login-btn').click()
    except :
        print('验证码识别次数:'+str(i))
        time.sleep(5)
        print('登录成功')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[8]/li/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[8]/li/ul/div/a/li').click()
        time.sleep(2)
        for i in range(520, 534):
            if i < 10:
                i = '00' + str(i)
            elif 10 <= i and i < 100:
                i = '0' + str(i)
            else:
                i = str(i)
            with open('1.txt', 'a') as f:
                f.write(i + "\n")
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/div[2]/input').send_keys(
                'FQ20210621000' + i)
            print('搜索' + i)
            time.sleep(2)
            driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/div[5]/span/button').click()
            time.sleep(3)
            zz = driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/section/div/div[4]/div[3]/table/tbody/tr/td[6]/div').get_attribute('textContent')
            code = str.find(str(zz), '京')
            if code == 0:
                driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/div[2]/input').clear()
                time.sleep(2)
                print(driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div[2]/section/div/div[4]/div[3]/table/tbody/tr/td[2]/div').get_attribute(
                    'textContent') + '已修改过')
            else:
                driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/div[2]/input').clear()
                time.sleep(2)
                driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div[2]/section/div/div[4]/div[4]/div[2]/table/tbody/tr[1]/td[18]/div/button/i').click()
                time.sleep(2)
                driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[3]/div/div/input').clear()
                print(zz)
                driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[3]/div/div/input').send_keys('京' + zz)
                print('修改' + driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[1]/div/div/input').get_attribute(
                    'value'))
                time.sleep(2)
                driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[3]/div/button[2]/span').click()
