# @Time     :2020/2/10 下午12:51
# @Author   :HuJinTao
# @File     :test_managetools.py
from selenium_wework_po.page.login_page import LoginPage

class TestManageTools():
    def setup_class(self):
        self.login = LoginPage()

    def teardown_class(self):
        # self.login.close_browser()
        pass

    def test_add_picture(self):
        img_path = '/Users/hujintao/Desktop/wuhan.jpg'
        add_picture_success = self.login.goto_index().goto_managetools().goto_material().add_picture(img_path)
        assert 'wuhan' in add_picture_success.get_add_picture_success_message()