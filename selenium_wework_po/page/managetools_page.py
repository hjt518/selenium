# @Time     :2020/2/9 下午4:07
# @Author   :HuJinTao
# @File     :managetools_page.py
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_po.page.basic_page import BasicPage
from selenium_wework_po.page.material_library_page import MaterialLibraryPage


class ManageTools(BasicPage):
    '''管理工具页面'''
    def goto_material(self):
        '''素材库页面-添加图片'''
        # 元素信息
        element_material_library = (By.CSS_SELECTOR, '.manageTools_cnt li.manageTools_cnt_item:nth-child(5)')
        self.find(element_material_library).click()

        return MaterialLibraryPage(self._driver)

