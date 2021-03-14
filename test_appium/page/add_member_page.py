# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/12 16:06
@Auth ： chenxu
@File ：add_member_page.py
"""
from test_appium.page.add_page import AddAndSave
from test_appium.page.base_page import BasePage


class AddMember(BasePage):
    def goto_add(self):
        self.parse_action("../page/add_member.yaml","goto_add")
        return AddAndSave(self.driver)