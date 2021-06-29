# _*_ coding: utf-8 _*_
from framework.base_page import BasePage
from img import baiduorcapi


class LoginProcess(BasePage):
    # 用户名输入框
    unm = r"id=>username"
    # 密码输入框
    pwd = r"id=>password"
    # 验证码输入框
    code = r"id=>account-img-code"
    # 验证码图片
    codeimg = r"id=>imgCode"
    # 登录按钮
    loginbutton = 'id=>login-btn'

    def getcode(self):
        # 定位到验证码元素
        code_element = self.find_element(self.codeimg)
        code_element.screenshot('../img/easy_img/code.png')
        code = baiduorcapi.bdocrapi('../img/easy_img/code.png')
        for i in range(100):
            if not code:
                self.sleep(5)
                self.click(self.codeimg)
                # 定位到验证码元素
                code_element = self.find_element(self.codeimg)
                code_element.screenshot('../img/easy_img/code.png')
                code = baiduorcapi.bdocrapi('../img/easy_img/code.png')
            return code[0]['words']
    def unm_pwd_login(self,unm,pwd,code):
        self.type(self.unm,unm)
        self.type(self.pwd,pwd)
        i = -1
        while self.get_page_title() == '登录':
            i = i+1
            try:
                self.sleep(5)
                self.type(self.code, self.getcode())
                self.click(self.loginbutton)
            except :
                print('验证码识别次数:'+str(i))
                print('登录成功')






