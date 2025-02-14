"""
@File    ：testcases/conftest.py
@Author  ：zr
@Date    ：2024-09-24
@Desc    ：web测试用例的前置
"""

import pytest
import psutil
import allure
from selenium import webdriver
from utils.timer import form_time
from utils.logger import log
from common.read_cfg import web_cfg
from config.config import cm

web_driver = None


@allure.title("浏览器驱动")
@pytest.fixture(scope='function', autouse=True)
def drivers(request):
    global web_driver
    web_driver = webdriver.Chrome(executable_path=cm.web_driver)
    web_driver.get(web_cfg.web_url)

    @allure.step("退出浏览器驱动")
    def fn():
        web_driver.close()
        web_driver.quit()

    @pytest.fixture(scope='function', autouse=True)
    def close_quit(self):
        process_name = web_cfg.web_driver_process
        # 查找所有的Chrome驱动进程
        process_list = [process for process in psutil.process_iter() if process.name() == process_name]
        if len(process_list) > 0:
            # 如果有多个Chrome驱动程序正在运行，则杀死所有的Chrome驱动程序
            for process in process_list:
                process.kill()
            log.info('存在Chrome驱动程序，并且已杀死所有Chrome驱动程序')
        else:
            log.info('没有Chrome驱动程序正在运行')

    @pytest.fixture(scope='function', autouse=True)
    def reconnect(self):
        process_name = web_cfg.web_driver_process
        # 查找所有的Chrome驱动进程
        process_list = [process for process in psutil.process_iter() if process.name() == process_name]
        if len(process_list) > 0:
            # 如果有多个Chrome驱动程序正在运行，则杀死所有的Chrome驱动程序
            if process_list[0] != process_list[1]:
                fn()
        else:
            log.info('没有Chrome驱动发生重启')

    request.addfinalizer(fn)
    with allure.step("返回浏览器驱动"):
        return web_driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 后置，获取测试结果
    outcome = yield
    reps = outcome.get_result()

    if reps.when == 'call' and reps.failed:
        # 在测试失败时进行截图, 添加到allure报告中
        img = web_driver.get_screenshot_as_png()
        # 为截图文件命名
        name = '_'.join([reps.nodeid.replace('testcases/', '').replace('::', '_'), form_time('%Y%m%d %H%M%S')])
        allure.attach(img, name=name, attachment_type=allure.attachment_type.PNG)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_call(item):
    # 记录正在运行的用例
    called = item.nodeid.replace('testcases/', '').replace('::', '_')
    log.info('case：%s', called)
    yield
