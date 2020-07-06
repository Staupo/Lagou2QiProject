# -*- coding: utf-8 -*-
# @Time   : 2020-07-05 15:44
# @Author : Saber
# @File   : test_addcontact.py

from time import sleep
import yaml
from appium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

with open('./datas/add_datas.yml', encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    print(datas)
    Add = datas['add']
    Del = datas['del']


class TestAddContact:

    def setup_class(self):
        desire_cap = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "noReset": "True",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "autoGrantPermissions": "True",
            "unicodeKeyBoard": "True",  # 输入中文的设置
            "resetKeyBoard": "True"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_cap)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize('username, gender, phonenumber', Add)
    def test_AddContact(self, username, gender, phonenumber):
        # 用一个显示等待，visibility_of_element_located方法判断一个元素是否出现，防止元素没有出现就去定位元素
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@resource-id="com.tencent.wework:id/dyx" and @text="通讯录"]')))
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/dyx" and @text="通讯录"]').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true)\
            .instance(0)).scrollIntoView(new UiSelector().\
            text("添加成员").instance(0));').click()  # 这里直接用安卓adk自带的定位工具进行滚动查找，防止联系人太多普通定位检索不到元素
        self.driver.find_element_by_xpath('//*[@text="手动输入添加"]')
        sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys(
            f'{username}')
        self.driver.find_element_by_xpath('//*[@text="性别"]/..//*[@text="男"]').click()
        if gender == '女':
            self.driver.find_element_by_xpath('//*[@text="男"]').click()
        else:
            self.driver.find_element_by_xpath('//*[@text="女"]').click()
        self.driver.find_element_by_xpath('//*[@text="手机号"]').send_keys(f'{phonenumber}')
        self.driver.find_element_by_xpath('//*[@text="保存"]').click()
        add_Contacts = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@class="android.widget.Toast"]')))
        # 利用显示等待判断Toast是否出现
        assert "添加成功" == add_Contacts  # 断言一下是否添加成功

        self.driver.find_element_by_id('com.tencent.wework:id/h9e').click()  # 这里进行一个返回操作，使页面回到通讯录页面

    @pytest.mark.parametrize('username', Del)
    def test_delete_contact(self, username):
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/dyx" and @text="通讯录"]').click()
        # 滚动查找被删除的联系人
        self.driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true)\
            .instance(0)).scrollIntoView(new UiSelector().\
            text("{username}").instance(0));').click()
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/h9p"]').click()  # 点击右上角
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/b2c" and @text="编辑成员"]').click()
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/e3f" and @text="删除成员"]').click()
        self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        # 验证是否删除成功，这里利用显示等待判断元素是否已经不存在
        WebDriverWait(self.driver, 10).until_not(lambda x: x.find_element_by_xpath(f'//*[@text="{username}"]'))
