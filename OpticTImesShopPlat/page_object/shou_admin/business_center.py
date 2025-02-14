"""
@File    ：page_login.py
@Author  ：zr
@Date    ：2024-09-24
@Desc    ：商务中心封装
"""

import allure

from page_base.page_base import Base


class PageBusiness(Base):
    """商务中心页面"""

    def page_show_data_one(self):
        """展示列表第一条数据"""
        self.base_find(default_list)

    def page_search_input(self, data):
        """搜索内容输入"""
        self.base_input(search_desc, data)

    def page_search_click(self):
        """点击搜索"""
        self.base_click(search_btn)

    def page_reset_click(self):
        """点击重置"""
        self.base_click(reset_btn)

    def page_show(self):
        """点击展示列表首条数据"""
        with allure.step(f"展示显示的第一条数据: "):
            self.page_show_data_one()

    def page_search(self, data):
        with allure.step(f"搜索内容并点击"):
            self.page_search_input(data)
        with allure.step(f"点击搜索"):
            self.page_search_click()
        with allure.step(f"展示显示的第一条数据: "):
            self.page_show_data_one()

    def page_reset(self):
        with allure.step(f"点击重置"):
            self.page_reset()
        with allure.step(f"展示显示的第一条数据: "):
            self.page_show_data_one()