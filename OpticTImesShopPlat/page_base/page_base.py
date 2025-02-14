"""
@File    ：page_base.py
@Author  ：zr
@Date    ：2024-09-24
@Desc    ：Base类：存放所有Page页面公共操作方法
"""
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utils.logger import log
from utils.timer import sleep
from selenium.webdriver.common.action_chains import ActionChains


class Base:
    def __init__(self, driver):
        self.driver = driver

    def base_find(self, loc, timeout=30, poll=0.5):
        """
        查找元素
        timeout：超时的时长，一般30S，超时未找到报错
        poll：检测间隔时长，默认0.5s，如果有一闪而逝的提示信息框，修改为0.1s
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def base_input(self, loc, text):
        """输入文本"""
        el = self.base_find(loc)
        el.clear()
        if text is not None:
            el.send_keys(text)
        log.info(f"{el}输入文本:{text}")

    def base_click(self, loc):
        """点击"""
        self.base_find(loc).click()
        sleep()
        log.info(f'点击按钮：{loc}')

    def base_get_text(self, loc):
        """获取当前元素文本"""
        _text = self.base_find(loc).text
        log.info(f"获取文本：{_text}")
        return _text

    def base_get_title(self):
        """获取当前页title"""
        title = self.driver.title
        log.info(f"当前页面：{title}")
        return title

    def base_alert_confirm(self):
        """自动确认弹框 以便继续进行后续的测试操作"""
        self.driver.switchTo().alert().accept()

    def base_is_dis(self, loc):
        """查看元素是否可见"""
        state = self.base_find(loc).is_displayed()
        log.info(f"获取元素可见状态：{state}")
        return state

    def base_keep_press(self, loc, time):
        """保持长按"""
        ActionChains(self.driver).click_and_hold(self.base_find(loc)).perform()
        log.info(f"长按：{loc}")
        sleep(time)
        ActionChains(self.driver).release(self.base_find(loc)).perform()
        log.info(f"释放：{loc}")

    def base_select(self, loc, text):
        """
        下拉框选择
        :param loc: select标签元素，父类, 不是option
        :param text: 通过显示文本选择
        """
        Select(self.base_find(loc)).select_by_visible_text(text)
        log.info(f"选择下拉框{loc}的{text}")

    def base_tick_checkbox(self, loc, num):
        """勾选框"""
        checkbox_list = self.base_find(loc)
        action = ActionChains(self.driver)
        for i in range(0, num):
            action.move_to_element(checkbox_list[i])
            action.click(checkbox_list[i]).perform()
            sleep()

    def base_invisible_element(self, loc, num, stop):
        """对动态变化元素执行动作链"""
        msg = self.base_find(loc)
        for i in range(0, num):
            action = ActionChains(self.driver)
            action.move_to_element(msg[i])
            action.click(msg[i])
            action.perform()
            sleep(stop)

    def base_refresh(self):
        """刷新页面F5"""
        self.driver.refresh()

    def base_quit(self):
        """退出浏览器"""
        self.driver.quit()
