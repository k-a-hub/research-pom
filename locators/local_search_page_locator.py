# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class LocalSearchPageLocator:

    def __init__(self):
        pass

    search_box = (By.XPATH, '/html/body/div/form/div[1]/input')
    search_btn = (By.XPATH, '/html/body/div/form/div[2]/input[1]')
    login_btn = (By.XPATH, '/html/body/div/form/div[2]/input[2]')