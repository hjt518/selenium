# @Time     :2020/1/19 下午3:45
# @Author   :HuJinTao
# @File     :index_page.py
import pytest
from selenium.webdriver.common.by import By
from selenium_wework_po.page.managetools_page import ManageTools
from selenium_wework_po.page.basic_page import BasicPage
from selenium_wework_po.page.contacts_page import ContactsPage
from selenium_wework_po.page.message_send_page import MessageSendPage


class IndexPage(BasicPage):
    '''首页-登录后的默认进入的页面'''
    def goto_address_book(self):
        # 点击"通讯录"
        self._driver.find_element(By.CSS_SELECTOR, '[id="menu_contacts"]').click()
        return ContactsPage(self._driver)

    def goto_managetools(self):
        '''点击管理工具菜单'''
        self._driver.find_element(By.ID,'menu_manageTools').click()
        return ManageTools(self._driver)

    def import_user(self,uploadpath):
        '''导入成员'''

        element_import_addresslist = (By.CSS_SELECTOR, '.js_service_list .ww_indexImg_Import')
        element_upload = (By.ID, 'js_upload_file_input')
        element_submit = (By.CSS_SELECTOR, '.import_settingSubmit')

        self.find(element_import_addresslist).click()
        self.find(element_upload).send_keys(uploadpath)
        self.find(element_submit).click()

        return self

    def get_import_user_message(self):
        return self._driver.find_element(By.CSS_SELECTOR, '.import_succStage_resultShow').text

    def goto_message_send(self):
        element_message_send = (By.CSS_SELECTOR, '.js_service_list a.js_groupMessage')
        self.find(element_message_send).click()
        return MessageSendPage(self._driver)
