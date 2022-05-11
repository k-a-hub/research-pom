# -*- coding: utf-8 -*-

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome import service

from page.search_page import SearchPage
from page.result_page import ResultPage

chrome_service = service.Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=chrome_service)

search_page = SearchPage(driver)
search_page.open()
search_page.search('ブラウザ自動化ツール')

result_page = ResultPage(search_page.driver)
print(result_page.get_result_stats())

sleep(3)
result_page.close()
