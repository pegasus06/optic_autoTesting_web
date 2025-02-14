"""
@File    ：runtest.py
@Author  ：zr
@Date    ：2024-09-24
@Desc    ：测试用例执行的入口
"""

import os
import pytest

from allure_des.allure_des import set_report_env_on_results, \
    set_report_executer_on_results, \
    set_report_categories_on_results
from config.config import cm
from utils.timer import sleep


def run():
    pytest.main(['-s','--allure-stories=登录成功,登录失败', '--alluredir=%s' % cm.dir_report_json,'-m=webtest'])
    # 在json目录下创建categories.json文件
    set_report_categories_on_results()
    # 在json目录下创建environment.properties文件
    set_report_env_on_results()
    # 在json目录下创建executor.json文件
    set_report_executer_on_results()
    sleep(3)
    os.system("allure generate %s -o %s --clean" % (cm.dir_report_json, cm.dir_report_html))


if __name__ == '__main__':
    run()
