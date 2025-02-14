"""
@File    ：el_home.py
@Author  ：zr
@Date    ：2025-02-05
@Desc    ：home界面的元素信息
"""

from selenium.webdriver.common.by import By

byid = By.ID
byname = By.NAME
bycname = By.CLASS_NAME
bytname = By.TAG_NAME
bylink = By.LINK_TEXT
bycss = By.CSS_SELECTOR
byxpath = By.XPATH


# home界面元素配置信息
banner_ele = (byxpath, '//*[@id="app"]/div/div[1]/div/div/div[1]/img')
solutions_ele = (byxpath, '//*[@id="app"]/div/div[2]/div[2]/div/div[1]')
solution_text=(byxpath,'//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]')
solution_request=(byxpath,'//*[@id="app"]/div/div[3]/button/span')
solution_contents=(bycname,'el-form-item__content')
