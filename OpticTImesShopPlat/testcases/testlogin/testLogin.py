"""
@File    test_login.py
@Author  zr
@Date    2024-09-24
"""

import allure
import pytest
from common.read_yaml import login_para
from utils.logger import log
from common.common import Common
from page_object.shop_prev.page_login import PageLogin

@allure.feature("登录成功,登录失败")
class TestLogin(Common):
    """测试登录 """

    @allure.story("测试登录")
    @allure.title("登录成功{login_case}")
    @allure.description("登录成功")
    @allure.severity("minor")
    @pytest.mark.parametrize("login_case", login_para)
    @pytest.mark.logintest
    def test_login(self, drivers, login_case):
        username = login_case['username']
        password = login_case['password']
        expect_text = login_case['expect']
        log.info(f"username:{username}")
        log.info(f"password: {password}")
        log.info(f"expect text: {expect_text}")
        PageLogin(drivers).page_login(username, password)
        with allure.step("登录成功"):
            assert expect_text == drivers.title
