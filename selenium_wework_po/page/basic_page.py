# @Time     :2020/1/19 下午3:22
# @Author   :HuJinTao
# @File     :basic_page.py

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasicPage():
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = webdriver.Firefox()
            self._driver.implicitly_wait(3)
            self._driver.get(self._base_url)
        else:
            self._driver = driver

    def close_browser(self):
        self._driver.quit()

    def find(self, locator):
        return self._driver.find_element(*locator)