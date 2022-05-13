# -*- coding: utf-8 -*-

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome import service

from page.local_search_page import LocalSearchPage
from page.result_page import ResultPage
from page.signin_page import SigninPage

chrome_service = service.Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=chrome_service)

search_page = LocalSearchPage(driver)
search_page.open()
search_page.search('ブラウザ自動化ツール')

result_page = ResultPage(search_page.driver)
print(result_page.get_result_stats())

sleep(2)
result_page.close()

# ----------------------------------------------

chrome_service = service.Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=chrome_service)

search_page = LocalSearchPage(driver)
search_page.open()
search_page.login()

sigin_page = SigninPage(search_page.driver)
sigin_page.display()

sleep(2)
sigin_page.close()