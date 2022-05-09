# @Time     :2020/2/10 下午6:33
# @Author   :HuJinTao
# @File     :test_index.py

from selenium_wework_po.page.login_page import LoginPage

class TestIndex():
    '''测试首页'''
    def setup_class(self):
        self.login = LoginPage()

    def teardown_class(self):
        #self.login.close_browser()
        pass

    def test_import_user(self):
        uploadpath = '/Users/hujintao/Desktop/通讯录批量导入模板.xlsx'
        upload_page =self.login.goto_index().import_user(uploadpath)
        assert '新增导入' in upload_page.get_import_user_message()

    def test_send_message(self):
        self.login.goto_index().goto_message_send().send_message(app='武汉')
        print('123')
