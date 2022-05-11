# -*- coding: utf-8 -*-

import os

from selenium.webdriver.common.keys import Keys
from locators.local_search_page_locator import LocalSearchPageLocator

from page.base_page import BasePage

class LocalSearchPage(BasePage):

    def __init__(self, driver):
        url = f'file:///{os.getcwd()}/index.html'
        super().__init__(driver, url)

    def search(self, keyword):
        locator = LocalSearchPageLocator.search_box
        search_box = self.driver.find_element(*locator)
        search_box.send_keys(keyword)
        locator = LocalSearchPageLocator.search_btn
        search_btn = self.driver.find_element(*locator)
        search_btn.click()
    
    def login(self):
        locator = LocalSearchPageLocator.login_btn
        login_btn = self.driver.find_element(*locator)
        login_btn.click()
