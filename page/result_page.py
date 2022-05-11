# -*- coding: utf-8 -*-

from locators.result_page_locator import ResultPageLocator
from page.base_page import BasePage


class ResultPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver=driver)
    
    def get_result_stats(self):
        locator = ResultPageLocator.result_status
        result_stats = self.driver.find_element(*locator).text
        return result_stats
