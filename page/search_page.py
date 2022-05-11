# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys

from locators.search_page_locator import SearchPageLocator
from page.base_page import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        url = 'https://www.google.com/'
        super().__init__(driver, url)

    def search(self, keyword):
        locator = SearchPageLocator.search_box
        search_box = self.driver.find_element(*locator)
        search_box.send_keys(keyword + Keys.ENTER)
