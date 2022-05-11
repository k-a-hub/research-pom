# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class SigninPageLocator:

    def __init__(self):
        pass

    email_box = (By.XPATH, '//*[@id="identifierId"]')
    forgot_email_btn = (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/button')
    create_account_link = (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button/span')
    next_link = (By.XPATH, '//*[@id="identifierNext"]/div/button/span')
