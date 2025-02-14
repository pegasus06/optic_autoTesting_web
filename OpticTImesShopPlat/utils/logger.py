"""
@File    : logger.py
@Author  : zr
@Date    : 2024/9/23
@Desc    ：日志管理模块
"""

import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from config.config import cm


class Log:
    def __init__(self, seg):

        self.seg = seg

        # 创建logger
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            # 定义日志文件大小为10M
            max_bytes = 10 * 1024 * 1024
            # 定义保留的文件数量为50个
            backup_count = 50

            # 创建日志文件处理器，备份文件命名规则默认为添加后缀数字，数字越大时间越早
            if self.seg == "time":
                fh = TimedRotatingFileHandler(cm.log_file, when='D', backupCount=backup_count, encoding='utf-8')
                """
                :param：when
                        'S'：每秒切分日志文件
                        'M'：每分钟切分日志文件
                        'H'：每小时切分日志文件
                        'D'：每天切分日志文件（默认值）
                        'W0' ~ 'W6'：每星期切分日志文件（0表示星期一，1表示星期二，以此类推）
                        'midnight'：每天午夜切分日志文件 与'D'相同
                :param：interval  默认1，1D就是一天
                """
                fh.setLevel(logging.INFO)
            else:
                fh = RotatingFileHandler(cm.log_file, maxBytes=max_bytes, backupCount=backup_count, encoding='utf-8')
                fh.setLevel(logging.INFO)

            # 创建一个handle输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 定义输出的格式
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 添加到handle
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    @property
    def fmt(self):
        return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'

# 使用时间分割log文件，可以修改when参数，建议在性能测试脚本中使用
# log = Log('time').logger
# 使用大小分割log文件
log = Log('size').logger
