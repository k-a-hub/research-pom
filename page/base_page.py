# -*- coding: utf-8 -*-

class BasePage:

    def __init__(self, driver=None, url=None):
        self.driver = driver
        self.url = url
    
    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()
