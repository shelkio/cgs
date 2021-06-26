# _*_ coding: utf-8 _*_
import unittest
from libs.HTMLTestRunner import HTMLTestRunner
import os
import time




#设置报告文件保存路径
repoot_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
#获取当前系统时间
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
#设置报告文件名称格式
HtmlFile = repoot_path + now + "HTMLtemplate.html"
fp = open(HtmlFile,"wb")
#构建suite2
suite = unittest.TestLoader().discover("testsuits")


if __name__ == '__main__':
    #初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner(stream=fp,title=u"测试项目报告",description=u"用例测试情况")
    #开始执行测试套件
    runner.run(suite)





