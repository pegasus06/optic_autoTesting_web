"""
@File    : timer.py
@Author  : zr
@Date    : 2024/9/23
@Desc    ：时间字符串管理
"""
import time
import datetime
from functools import wraps


def timestamp():
    """时间戳"""
    return time.time()


def form_time(fmt="%Y%m"):
    """
    datetime格式化时间
    :param fmt “%Y%m%d %H%M%S
    """
    return datetime.datetime.now().strftime(fmt)


def sleep(seconds=1.0):
    """睡眠时间"""
    time.sleep(seconds)


def running_time(func):
    """函数运行时间"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timestamp()
        res = func(*args, **kwargs)
        print("校验元素done！用时%.3f秒！" % (timestamp() - start))
        print(res)
        return res

    return wrapper

if __name__ == '__main__':
    timestamp()