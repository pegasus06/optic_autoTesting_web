"""
@File    ：el_login.py
@Author  ：zr
@Date    ：2024-09-24
@Desc    ：登录界面的元素信息
"""

from selenium.webdriver.common.by import By

byid = By.ID
byname = By.NAME
bycname = By.CLASS_NAME
bytname = By.TAG_NAME
bylink = By.LINK_TEXT
bycss = By.CSS_SELECTOR
byxpath = By.XPATH

# 界面元素配置信息
search_desc = (bycss, '.el-input__inner[0]')
search_email = (bycss, '.input__inner[1]')
search_btn = (bycss, '.el-button[0]')
reset_btn = (bycss, '.el-button[1]')
default_list=(bycss,'.cell el-tooltip')

