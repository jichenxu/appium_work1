# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/12 15:56
@Auth ： chenxu
@File ：app.py
"""
from appium import webdriver

from test_appium.page.base_page import BasePage
from test_appium.page.information_page import Information


class App(BasePage):

    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        # 不清空缓存启动app
        caps["noReset"] = "true"
        # 设置等待页面空闲状态的时间为0s
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 显式等待10s
        self.driver.implicitly_wait(10)
        return self
    def goto_main(self):
        return Information(self.driver)