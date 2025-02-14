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
video_titles=(byxpath,'//*[@id="app"]/div/div[4]/div[2]/div')
more_videos=(byxpath,'//*[@id="app"]/div/div[3]/div[2]')
video_products=(byxpath,'//*[@id="el-id-902-50"]/label[3]/span')

