# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/12 18:18
@Auth ： chenxu
@File ：test_add.py
"""
from test_appium.page.app import App


class TestAdd:

    def test_add_members(self):
        App().start().goto_main().goto_address_list().goto_add_member().goto_add().add_and_save("周星星","523423232@qq.com")