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
core_products = (byxpath, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[1]')
core_product_text=(byxpath,'//*[@id="app"]/div/div[2]/span')
solution_text=(byxpath,'//*[@id="app"]/div/div[3]/div/span')
solution_fBanner=(byxpath,'//*[@id="app"]/div/div[3]/section/div[1]/ol/li[5]/img')
solution_sBanner=(byxpath,'//*[@id="app"]/div/div[3]/section/div[1]/ol/li[6]/img')
cooperation_text=(byxpath,'//*[@id="app"]/div/div[4]/div[1]/span')
bussiness_cooperation_apply=(byxpath,'//*[@id="app"]/div/div[4]/div[2]/div[1]/button')
solution_design_apply=(byxpath,'//*[@id="app"]/div/div[4]/div[2]/div[2]/button')
news=(byxpath,'//*[@id="app"]/div/div[5]/div[1]/span')
news_detail=(byxpath,'//*[@id="app"]/div/div[5]/div[2]/div/div[1]')
news_title=(byxpath,'//*[@id="app"]/div/div[5]/div[2]/div/div[2]')
news_subtitle=(byxpath,'//*[@id="app"]/div/div[5]/div[2]/div/div[3]')