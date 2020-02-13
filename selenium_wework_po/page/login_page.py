# @Time     :2020/1/19 下午3:25
# @Author   :HuJinTao
# @File     :login_page.py

import json

from selenium_wework_po.page.basic_page import BasicPage
from selenium_wework_po.page.index_page import IndexPage


class LoginPage(BasicPage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome'

    def save_cookies(self, filename):
        '''保存cookie'''
        cookies = self._driver.get_cookies()
        jsonCookies = json.dumps(cookies)
        with open(filename, 'w') as f:
            f.write(jsonCookies)

    def get_cookies(self, filename):
        '''读取已保存的cookies'''
        with open(filename, 'r') as f:
            list_cookies = json.loads(f.read())
        for i in list_cookies:
            self._driver.add_cookie(i)

    def goto_index(self):
        filename = 'wework_cookies'

        #sleep(20)

        # 手动扫描下登录的二维码，此时登录成功后将保存cookies，执行一次就可以了
        #self.save_cookies(filename)

        # 读取已保存的cookies
        self.get_cookies(filename)

        # 最后刷新下页面
        # self._driver.get(self._base_url)
        self._driver.refresh()

        return IndexPage(self._driver)
