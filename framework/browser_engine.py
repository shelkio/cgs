# _*_ coding: utf-8 _*_
import configparser
import os
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):
    dri = os.path.dirname(os.getcwd())
    # dri = os.path.dirname(os.path.abspath('.'))
    # chrome_driver_path = dir + '/tools/chromedriver.exe'
    # ie_driver_path = dir + '/tools/IEDriverServer.exe'


    def  __init__(self,driver):
        self.driver = driver


    def open_browser(self,driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.getcwd()) + '/Config/config.ini'
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer","URL")
        logger.info("The test server url is: %s" % url)


        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome()
            logger.info("Starting Chrome browser")
        elif browser == "IE":
            driver = webdriver.Ie()
            logger.info("Starting IE browser")

        driver.get(url)
        logger.info("Open url: %s " % url)
        driver.maximize_window()
        logger.info("Maximize the current window. " )
        #driver.implicitly_wait(10)
        #logger.info("Set implicitly wait 10 seconds. " )
        return driver

    def quit_browser(self):
        logger.info("Now,Close and quit the browser.")
        self.driver.quit()