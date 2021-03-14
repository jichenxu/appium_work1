# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/12 16:06
@Auth ： chenxu
@File ：add_page.py
"""
from test_appium.page.base_page import BasePage


class AddAndSave(BasePage):

    def add_and_save(self,name,email):
        self.param_list['name_value'] = name
        self.param_list['email_value'] = email
        self.parse_action("../page/add.yaml","add")

