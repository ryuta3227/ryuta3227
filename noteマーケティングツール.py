#コピー防止のためにコードの一部を変更しています

#検索URL
pattern = ("")
#いいね数
like = 50

loginID = ("")
password = ("")


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urllib.parse
import time
import random
from time import sleep

from bs4 import BeautifulSoup
import requests
import re

note = ('https://note.com')


driver = webdriver.Chrome("Chromedriver")

#ヘッドレス化
#from selenium.webdriver import Chrome,ChromeOptions
#options = ChromeOptions()
#options.add_argument('--headless')
#driver = Chrome(options=options)

#noteログインページ
driver.get("https://note.com/login")

sleep(random.randint(1,3))

"""
ID,パスワード,検索URLの入力
"""

driver.find_element_by_name("login").send_keys(loginID)
sleep(random.randint(1,6))
driver.find_element_by_name("password").send_keys(password)
URL = pattern


sleep(random.randint(,2))
# ログインボタンをクリック
driver.find_element_by_class_name("logining_msg").click()
sleep(random.randint(1,3))
#目的のページに遷移
driver.get(URL)
BREAK = 0


#ページ読み込みのために待機
sleep(random.randint(15,20))

#新しいページソースを読み込む
new_page_source = driver.page_source

#req = requests.get(new_page_source).text
soup = BeautifulSoup(new_page_source,'lxml')
sleep(random.randint(1,6))
#URL全取得

href_list = []
all_url = []
#ページの仕様変わる可能性あり！⬇︎セレクタの名前と場所
#キーワード検索
for a in soup.select('.o-textNote__title > a'): #.o-textNote
    href_list.append(a.get('href'))
for u in href_list:
    href_list = note + u
    all_url.append(href_list)
print(len(all_url))

#ハッシュタグ検索
for a in soup.select('.renewal-p-cardItem__eyecatch > a'): #.o-textNote
    href_list.append(a.get('href'))
for u in href_list:
    href_list = note + u
    all_url.append(href_list)
print(len(all_url))

#ntoe検索
sleep(random.randint(1,3))
#driver.get(URL)
BREAK = 0
for item in all_url:
    try:
        driver.get(item)
        sleep(random.randint(2,3))

        driver.find_element_by_class_name("o-like__pc").click()
        sleep(random.randint(1,3))

        BREAK = BREAK + 1
        print(BREAK)
        if BREAK > like:
            print('処理完了しました！')
            break
    except:
        print("pass")
        sleep(random.randint(3,7))
        pass

