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

# 登录界面元素配置信息
login_username = (byxpath, '//div[@id=\'app\']/div/div/div[2]/form/div[1]/div/div/div/input')
login_pwd = (byxpath, '//div[2]/div/div/div/input')
login_btn = (bycss, '.el-button:nth-child(3)')
register_btn = (byxpath, '//*[@id="app"]/div/div/div[2]/button[2]/span')
forget_pass = (byxpath, '//*[@id="app"]/div/div/div[2]/div/span')
login_err_info = (bycss, '//*[@id="message_11"]/p')

