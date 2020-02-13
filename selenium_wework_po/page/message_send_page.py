# @Time     :2020/2/12 上午11:56
# @Author   :HuJinTao
# @File     :message_send_page.py
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_po.page.basic_page import BasicPage


class MessageSendPage(BasicPage):

    def element_wait(self, timeout, element):
        WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable(element))


    def send_message(self, app='', scope='',content=''):
        element_selectapp_link = (By.LINK_TEXT, '选择需要发消息的应用')
        element_app = (By.CSS_SELECTOR, '[data-name="%s"]'%(app))
        element_submit_button = (By.LINK_TEXT, '确定')
        element_selectscope_link = (By.LINK_TEXT, '选择发送范围')

        self.find(element_selectapp_link).click()
        self.find(element_app).click()
        self.find(element_submit_button).click()

        self.find(element_selectscope_link).click()
