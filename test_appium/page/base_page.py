# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/12 15:33
@Auth ： chenxu
@File ：base_page.py
"""
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    param_list = {}
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    def find_click(self,locator):
        self.find(locator).click()

    def find(self,locator):
        return self.driver.find_element_by_xpath(locator)
        # 滚动查找元素

    def swip_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()
    def parse_action(self,path,fun_name):
        with open(path,encoding='utf-8') as f:
            function = yaml.safe_load(f)
            steps = function[fun_name]
            for step in steps:
                if step['action'] == 'click':
                    self.find_click(step['locator'])
                elif step['action'] == 'find':
                    self.find(step['action'])
                elif step['action'] == 'send':
                    content: str = step["value"]
                    for param in self.param_list:
                        content = content.replace("{%s}"%param,self.param_list[param])
                    self.find(step['locator']).send_keys(content)

