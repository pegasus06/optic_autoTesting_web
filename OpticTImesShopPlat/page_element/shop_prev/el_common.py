"""
@File    ：el_menu.py
@Author  ：zr
@Date    ：2025-02-05
@Desc    ：menu界面的元素信息
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
banner_logo = (byxpath, '//*[@id="app"]/div/div[1]/div[1]/div')
menu_home=(byxpath,'//*[@id="app"]/div/div[1]/ul/li[1]')
menu_product=(byxpath,'//*[@id="app"]/div/div[1]/ul/li[2]')
menu_solution=(byxpath,'//*[@id="app"]/div/div[1]/ul/li[3]')
menu_support=(byxpath,'//*[@id="app"]/div/div[1]/ul/li[4]')
menu_about=(byxpath,'//*[@id="app"]/div/div[1]/ul/li[5]')
search_btn=(byxpath,'//*[@id="app"]/div/div[1]/div[2]/div[1]')
cart_btn=(byxpath,'.topTip_right_car')
home_info=(bycname,'.el-dropdown user')
