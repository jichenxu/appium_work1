# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/12 16:00
@Auth ： chenxu
@File ：information_page.py
"""
from test_appium.page.address_page import Address
from test_appium.page.base_page import BasePage


class Information(BasePage):
    def goto_address_list(self):
        self.parse_action("../page/infromation.yaml","goto_address")
        return Address(self.driver)