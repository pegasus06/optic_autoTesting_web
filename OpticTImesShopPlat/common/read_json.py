"""
@File    ：read_json.py
@Author  ：zr
@Date    ：2024-09-24
@Desc    ：读取json格式的测试数据
"""

import json

from config.config import cm


class ReadJson:

    def __init__(self, json_file):
        self.json_file = json_file

    def read_json(self, key):
        """ 返回元祖列表 """
        arr = []
        with open(self.json_file, "r", encoding="utf-8") as f:
            datas = json.load(f,)
            value = datas.get(key)
            for data in value:
                arr.append(tuple(data.values())[1:])
            return arr


json_para = ReadJson(cm.test_json_file)
# 读取json文件中的对应模块，每个模块一个实例
login_para = json_para.read_json('login')
group_call_para = json_para.read_json('group_call')

# 得到元祖列表格式如下：
# [('700001', '700001', '登录成功'), ('700002', '', '登录失败，密码不能为空'), ('700003', '700003', '登录成功')]
