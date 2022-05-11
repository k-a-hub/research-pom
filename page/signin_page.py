# -*- coding: utf-8 -*-


from locators.signin_page_locator import SigninPageLocator
from page.base_page import BasePage


class SigninPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
    
    def display(self):
        locator = SigninPageLocator.email_box
        email_box = self.driver.find_element(*locator)
        locator = SigninPageLocator.forgot_email_btn
        forgot_email_btn = self.driver.find_element(*locator)
        locator = SigninPageLocator.create_account_link
        create_account_link = self.driver.find_element(*locator)
        locator = SigninPageLocator.next_link
        next_link = self.driver.find_element(*locator)

        if email_box.is_displayed() and forgot_email_btn.is_displayed() and create_account_link.is_displayed() and next_link.is_displayed():
            print('全要素表示')
        else:
            print('非表示要素あり')

