# @Time     :2020/1/19 下午6:51
# @Author   :HuJinTao
# @File     :contacts_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium_wework_po.page.basic_page import BasicPage


class ContactsPage(BasicPage):
    '''通讯录页'''

    def element_wait(self, timeout, element):
        WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable(element))

    def add_member(self, username, userid, userphone):
        '''添加成员'''

        # 元素信息
        element_add_member = (By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member')
        element_username = (By.NAME, 'username')
        element_acctid = (By.NAME, 'acctid')
        element_sex = (By.CSS_SELECTOR, '.ww_radio[value="2"]')
        element_zipcode = (By.CSS_SELECTOR, '.ww_telInput_zipCode_input')
        element_area_code = (By.CSS_SELECTOR, 'li[data-value="853"]')
        element_memberphone = (By.CSS_SELECTOR, '[id="memberAdd_phone"]')
        element_save_button = (By.CSS_SELECTOR, '.js_btn_save')

        # 点击"添加成员"
        self.element_wait(10, element_add_member)
        self.find(element_add_member).click()
        # 输入 姓名、id
        self.find(element_username).send_keys(username)
        self.find(element_acctid).send_keys(userid)
        # 性别
        self.find(element_sex).click()
        # 手机号所属区域
        self.find(element_zipcode).click()
        self.find(element_area_code).click()
        # 输入手机号
        self.find(element_memberphone).send_keys(userphone)
        # 点击保存按钮
        self.find(element_save_button).click()

        return self

    def get_addmember_error_message(self):
        result = []
        for element in self._driver.find_elements(By.CSS_SELECTOR, '.ww_tip_Warning'):
            result.append(element.text)
        print('打印报错信息'.center(50, '-'))
        print(result)
        return result

    def get_addmember_success_message(self):
        result = []
        for element in self._driver.find_elements(By.CSS_SELECTOR, '.ww_tip.success'):
            result.append(element.text)
        print('打印保存成功信息'.center(50, '-'))
        print(result)
        return result

    def delete_member(self):
        '''删除用户'''
        # 元素定位
        element_check_box = (
            By.CSS_SELECTOR, '.js_has_member table.member_colRight_memberTable tr:nth-child(2) td:nth-child(1)')
        element_delete_button = (By.CSS_SELECTOR, '.js_has_member .ww_operationBar .js_delete')
        element_submit_button = (By.CSS_SELECTOR, '.ww_dialog_foot [d_ck="submit"]')

        # 操作步骤
        self.find(element_check_box).click()
        self.find(element_delete_button).click()
        self.find(element_submit_button).click()

        return self

    def update_member(self, username, userphone):
        '''修改用户'''
        # 元素定位
        element_row = (
            By.CSS_SELECTOR, '.js_has_member table.member_colRight_memberTable tr:nth-child(2) td:nth-child(2)')
        element_update_button = (By.CSS_SELECTOR, 'div.member_colRight_view div.member_colRight_operationBar a.js_edit')
        element_username = (By.NAME, 'username')
        element_phone = (By.NAME, 'mobile')
        element_submit_button = (By.CSS_SELECTOR, 'form.js_member_editor_form div:nth-child(1) a.js_save')

        # 操作步骤
        self.find(element_row).click()
        self.find(element_update_button).click()

        self.element_wait(10, element_username)

        self.find(element_username).clear()
        self.find(element_phone).clear()
        self.find(element_username).send_keys(username)
        self.find(element_phone).send_keys(userphone)
        self.find(element_submit_button).click()

        return self

    def get_update_success_message(self):
        '''获取修改人员成功的信息'''
        element = (
            By.CSS_SELECTOR,
            '.member_display_formWrap .member_display_cover_detail div.member_display_cover_detail_name')
        text = self.find(element).text
        print('修改后人员名称是：', text)
        return text

    def get_update_fail_message(self):
        '''获取修改人员失败的信息'''
        element = (By.CSS_SELECTOR, '.ww_tip_Warning')
        result = []
        for i in self._driver.find_elements(*element):
            result.append(i.text)
        print('修改人员失败，报错信息是：',result)
        return result
