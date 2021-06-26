# _*_ coding: utf-8 _*_
from framework.browser_engine import BrowserEngine
from pageobjects.login_process import LoginProcess
import unittest
class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
    # @classmethod
    # def tearDownClass(cls):
    #     """
    #     测试固件的setUp()的代码，主要是测试的前提准备工作
    #     :return:
    #     """
    #     cls.driver.quit()
    def test_login(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法
        :return:
        """
        login = LoginProcess(self.driver)
        code = login.getcode()
        login.unm_pwd_login(u'17600352198','a12345678',code)

if __name__ == '__main__':
    unittest.main()