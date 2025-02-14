"""
@File    ：common.py
@Author  : zr
@Date    : 2024/9/23
@Desc    ：用例执行前后置,pytest框架
"""
from utils.logger import log


class Common:
    @staticmethod
    def setup_class():
        log.info('-------module start')

    @staticmethod
    def teardown_class():
        log.info('-------module end')

    @staticmethod
    def teardown_method():
        log.info('-------case end')
