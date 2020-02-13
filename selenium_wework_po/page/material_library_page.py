# @Time     :2020/2/12 上午11:38
# @Author   :HuJinTao
# @File     :material_library_page.py
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_po.page.basic_page import BasicPage

class MaterialLibraryPage(BasicPage):
    '''素材库页面'''

    def element_wait(self, timeout, element):
        WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable(element))

    def add_picture(self,uploadImagePath):
        '''添加图片'''
        element_picture = (By.LINK_TEXT, '图片')
        element_add_picture = (By.LINK_TEXT, '添加图片')
        element_uploadImage = (By.CSS_SELECTOR, '[name="uploadImageFile"]')
        element_done_button = (By.LINK_TEXT, '完成')

        # 操作步骤
        self.find(element_picture).click()

        self.element_wait(10, element_add_picture)
        self.find(element_add_picture).click()

        self.find(element_uploadImage).send_keys(uploadImagePath)
        sleep(2)
        self.find(element_done_button).click()

        return self

    def get_add_picture_success_message(self):
        check_element = (By.CSS_SELECTOR, '.js_pic_name_show')
        element_text = self.find(check_element).text
        print('新增的图片名称是 ', element_text)
        return element_text