"""
@File    ：page_home.py
@Author  ：zr
@Date    ：2024-12-11
@Desc    ：Home界面封装
"""

import allure

from utils.timer import sleep
from page_base.page_base import Base
from page_element.shop_prev import el_home, el_login


class PageHome(Base):
    """Home页面"""

    def page_click_banner(self, ele):
        """点击进入轮播图"""
        self.base_click(el_home.bannerEle)
        sleep()

    def page_input_passwd(self, password):
        """输入密码"""
        self.base_input(el_login.login_pwd, password)
        sleep()

    def page_input_verify_code(self, verify_code):
        """输入验证码"""
        pass

    def page_click_login_btn(self):
        """点击登录按钮"""
        self.base_click(el_login.login_btn)
        sleep()

    def page_get_error_info(self):
        """获取异常提示信息"""
        return self.base_get_text(el_login.login_err_info)

    def page_login(self, username, password):
        sleep(2)
        with allure.step(f"输入用户名: {username}"):
            self.page_input_username(username)
        with allure.step(f"输入密码: {password}"):
            self.page_input_passwd(password)
        sleep(3)
        with allure.step("点击登录按钮"):
            self.page_click_login_btn()
