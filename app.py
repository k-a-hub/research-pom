# -*- coding: utf-8 -*-

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Google Chromeのドライバーセットし、Google検索画面を開く
driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.google.com/')

# 検索テキストボックスに検索キーワードを入れてEnterキーを押下
search_box = driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_box.send_keys('ブラウザ自動化ツール' + Keys.ENTER)

# 検索結果の件数と実行時間を取得
result_stats = driver.find_element_by_xpath('//*[@id="result-stats"]').text
print(result_stats)

sleep(10)
driver.quit()
