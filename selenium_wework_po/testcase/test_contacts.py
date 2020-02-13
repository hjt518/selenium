# @Time     :2020/1/19 下午5:59
# @Author   :HuJinTao
# @File     :test_contacts.py

import pytest
from selenium_wework_po.page.login_page import LoginPage


class TestAddressBook():
    def setup_class(self):
        self.login = LoginPage()

    def teardown_class(self):
        # self.login.close_browser()
        pass

    test_data = [
        ('2020鼠年大吉', 'selenium_01', '63901200'),
        ('2020鼠年大吉', 'selenium_02', '63901201')
    ]

    @pytest.mark.parametrize('username,userid,userphone', test_data)
    def test_add_member_sucess(self, username, userid, userphone):
        add_numbers_page = self.login.goto_index().goto_address_book().add_member(username, userid, userphone)
        assert '保存成功' in '|'.join(add_numbers_page.get_addmember_success_message())

    test_error_data = [
        ('2020鼠年大吉', 'selenium_03', '12345678901')
    ]

    @pytest.mark.parametrize('username,userid,userphone', test_error_data)
    def test_add_member_fail(self, username, userid, userphone):
        add_number_error_page = self.login.goto_index().goto_address_book().add_member(username, userid,
                                                                                       userphone)
        assert '请填写正确的手机号码' in '|'.join(add_number_error_page.get_addmember_error_message())

    def test_delete_member(self):
        self.login.goto_index().goto_address_book().delete_member()

    def test_update_member_success(self):
        username = 'update张三疯'
        userphone = '63901203'
        mumber_details_page = self.login.goto_index().goto_address_book().update_member(username, userphone)
        assert username in mumber_details_page.get_update_success_message()

    def test_update_member_fail(self):
        username = 'updatefailed'
        userphone = '199000000000011111'
        mumber_details_page = self.login.goto_index().goto_address_book().update_member(username, userphone)
        assert '请填写正确的手机号码' in '|'.join(mumber_details_page.get_update_fail_message())
