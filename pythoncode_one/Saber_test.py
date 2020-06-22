# -*- coding: utf-8 -*-
# @Time   : 2020-06-17 22:54
# @Author : Saber
# @File   : Saber_test.py

# 复用浏览器方式登录企业微信（调试）
# cmd chrome --remote-debugging-port=9222 启动浏览器
# 访问 http://localhost:9222/

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Testgeterror:
    def test_login(self):
        option = Options()
        option.debugger_address = 'localhost:9222'  # 通过option参数指定调试地址
        driver = webdriver.Chrome(options=option)
        driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        # 不会新跳出浏览器窗口，会在当前浏览器窗口执行
