# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/12 16:04
@Auth ： chenxu
@File ：address_page.py
"""
from test_appium.page.add_member_page import AddMember
from test_appium.page.base_page import BasePage


class Address(BasePage):
   def goto_add_member(self):
       self.swip_click("添加成员")
       return AddMember(self.driver)