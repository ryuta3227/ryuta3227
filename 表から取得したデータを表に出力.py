from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.keys import Keys

import pandas as pd
import openpyxl

#ヘッドレスでChromeを起動

options = ChromeOptions()
options.add_argument('--headless')

browser = Chrome(options=options)

names = []
prices = []
brand = []
buyer = []


#商品一覧１０ページ分 buyma２ページ目 https://www.buyma.com/r/-C3105_2/

for i in range(1,3):
    url = 'https://www.buyma.com/r/_GUCCI-%E3%82%B0%E3%83%83%E3%83%81/-C1002R120/{}{}'.format('_',i)
    browser.implicitly_wait(1)
    browser.get(url)


#product_bodyを探し終わったら次のproduct_bodyの中身を探し始めるfor文
#browser.find_element_by_class_nameで指定したクラス名の要素を取得し、リストとしてproduct_bodysに格納

products = browser.find_elements_by_class_name('product')

for product in products:

    product_name = product.find_element_by_class_name('product_name').text
    names.append(product_name)

    Price_Txt = product.find_element_by_class_name('Price_Txt').text
    prices.append(Price_Txt)

    product_Brand = product.find_element_by_class_name('product_Brand').text
    brand.append(product_Brand)

    product_Buyer = product.find_element_by_class_name('product_Buyer').text
    buyer.append(product_Buyer)

#csv出力

df = pd.DataFrame()

df['product_name'] = names
df['Price_Txt'] = prices
df['product_Brand'] = brand
df['product_Buyer'] = buyer

df.head()

df.to_csv('shop_csv', index = False)

#Excelファイルに出力する

df = df.to_excel("product_list.xlsx",index = False)
