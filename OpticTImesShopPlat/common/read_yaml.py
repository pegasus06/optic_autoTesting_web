"""
@File    ：read_yaml.py
@Author  ：zr
@Date    ：2024-09-24
@Desc    ：读取yaml格式的测试数据，返回的是字典列表
"""

import yaml

from config.config import cm


class ReadYaml:

    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def read_yaml(self, key):
        with open(self.yaml_file, 'r', encoding='utf-8') as f:
            datas = yaml.load(f, Loader=yaml.FullLoader)  # 避免报警告，需要加入Loader=yaml.FullLoader
            value = datas[key]
            return value

yaml_para = ReadYaml(cm.test_web_yaml_file)
login_para = yaml_para.read_yaml('login')
"""
返回字典列表 
[{'case1': '登录成功1', 'username': 70001, 'password': '7001@mcx', 'expect': '失败'}, 
{'case2': '登录成功2', 'username': 70002, 'password': None, 'expect': '密码'}, 
{'case3': '登录成功3', 'username': 70003, 'password': 70003, 'expect': '密码', 'desc': '登录失败(用户不存在）'}]
"""
