# -*- coding: utf-8 -*-
# @Time   : 2020-06-14 21:25
# @Author : Saber
# @File   : lagou_web.py


from selenium import webdriver


class Test_saber():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # 最大化浏览器窗口
        self.driver.implicitly_wait(3)  # 隐世等待

    def teardown(self):
        self.driver.quit()  # 资源的回收，自动关闭

    def test_hcu(self):
        self.driver.get("http://www.testerhome.com")  # 打开被测浏览器
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_class_name('team-name').click()
        self.driver.find_element_by_css_selector('//*[@title="Jenkins 项目配置 allure 报告和 Dingding 消息"]').click()

    # browser = webdriver.Chrome()
    # browser.get('https://baidu.com')
