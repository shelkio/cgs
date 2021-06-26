from selenium import webdriver

driver = webdriver.Chrome('D:\DriverConifg\chromedriver')
driver.maximize_window()

'''
输入url操作
'''
def browser(url):
    driver.get(url)


'''
定位元素
'''
def find_element(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        print('\033[32m定位成功，元素为:' + xpath + '\033[0m')
    except:
        print('\033[31m元素不存在，元素为:' + xpath + '\033[0m')


'''
输入操作
'''
def send_keys(xpath, content):
    try:
        driver.find_element_by_xpath(xpath).send_keys(content)
        print('\033[32m输入成功，元素为:' + xpath + '\033[0m')
    except:
        print('\033[31m元素不存在，元素为:' + xpath + '\033[0m')


'''
点击操作
'''
def click(xpath):
    try:
        driver.find_element_by_xpath(xpath).click()
        print('\033[32m点击成功，元素为:' + xpath + '\033[0m')
    except:
        print('\033[31m元素不存在，元素为:' + xpath + '\033[0m')


'''
获取元素的内容
'''
def get_attribute(xpath):
    try:
        content = driver.find_element_by_xpath(xpath).get_attribute('textContent')
        print('\033[32m获取到元素内容，元素为:' + xpath + '\033[0m')
        return content
    except:
        print('\033[31m元素不存在，元素为:' + xpath + '\033[0m')


'''
清除元素的内容
'''
def clear(xpath):
    try:
        content = driver.find_element_by_xpath(xpath).clear()
        print('\033[32m清空元素内容，元素为:' + xpath + '\033[0m')
        return content
    except:
        print('\033[31m元素不存在，元素为:' + xpath + '\033[0m')


if __name__ == '__main__':
    click('111111112222asdasdasd')
