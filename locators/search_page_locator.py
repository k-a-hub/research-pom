# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class SearchPageLocator:

    def __init__(self):
        pass

    search_box = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
