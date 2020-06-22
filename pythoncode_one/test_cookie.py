# -*- coding: utf-8 -*-
# @Time   : 2020-06-22 21:11
# @Author : Saber
# @File   : test_cookie.py

import json
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_Cookie():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')

    def test_Getcookie(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        sleep(10)
        Cookie = self.driver.get_cookies()
        with open("cookie.json", "w") as f:
            json.dump(Cookie, f)

    def test_cookie_Login(self):
        cookies = json.load(open('cookie.json'))
        for cookie in cookies:  # 通过for循环遍历cookie信息,将cookie信息以键值对的形式添加到浏览器中
            self.driver.add_cookie(cookie)
        # sleep(20)
        # self.driver.refresh()
        while True:
            self.driver.refresh()
            lef = WebDriverWait(self.driver, 10). \
                until(expected_conditions.element_to_be_clickable((By.ID, "menu_index")))
            if lef is not None:
                break

    def teardown(self):
        self.driver.quit()
