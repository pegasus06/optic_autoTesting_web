"""
@File    ：read_cfg.py
@Author  : zr
@Date    : 2024/9/23
@Desc    ：封装读取ini配置文件
"""

import configparser
from config.config import cm


# 根据实际定义
HOST = 'host'
DRIVER = 'driver'

class ReadConfig:
    """ini配置文件"""

    def __init__(self, ini_file):
        self.file = ini_file
        self.config = configparser.RawConfigParser()  # 当有%的符号时使用Raw读取 不对配置文件中的值进行解析
        self.config.read(self.file, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(cm.ini_file, 'w') as f:
            self.config.write(f)

    @property
    def web_url(self):
        return self._get(HOST, 'HOST')

    @property
    def web_driver_process(self):
        return self._get(DRIVER, 'DRIVER_PROCESS')

web_cfg = ReadConfig(cm.web_ini_file)
