# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class ResultPageLocator:

    def __init__(self):
        pass

    result_status = (By.XPATH, '//*[@id="result-stats"]')
