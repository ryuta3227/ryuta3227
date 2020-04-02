from bs4 import BeautifulSoup
from pathlib import Path
import requests
import re
import time

i = 1
j = 1


#ブランドごとに変える
base_url = 'https://store.musinsa.com/app/brand/goods_list/massnoun'
store = 'https://store.musinsa.com'

req = requests.get(base_url).text
soup = BeautifulSoup(req,'lxml')
time.sleep(1)

#画像用フォルダ作成,自分のシステムに書き換える
output_folder = Path('/Users/ryuutarou/Desktop/MASSNOUN/')
output_folder.mkdir(exist_ok = True)

#URL全取得
a_href_list = []
for a in soup.select('a'):
    a_href_list.append(a.get('href'))
#必要なurlだけ残す
a_href_list_find = [s for s in a_href_list if '/app/product/detail/'in s]
#print(a_href_list_find)
all_url = []
for u in a_href_list_find:
     a_href_list_find = store + u
     all_url.append(a_href_list_find)
del all_url [1::2] #リストの奇数番目を削除　偶数番目なら　del all_url [0::2]
print(all_url)
print(len(all_url))

product_img = []
product_code = []
prduct_url = []
info = []
#リストのurlを取得して、それぞれ格納

BREAK = 1

for each_page in all_url:

    req = requests.get(each_page).text
    soup = BeautifulSoup(req,'lxml')

    prduct_url.append(each_page)
    info.append(each_page)
    #ブランド名
    #brand = []
    brand_and_product_code = soup.select_one('.product_article_contents')
    info.append(brand_and_product_code.text)

    #価格
    #price = []
    product_price = soup.select_one('.product_article > #normal_price')
    info.append(product_price.text)

    #商品情報
    #info = []
    for product_info in soup.select('.detail_product_info > p'):
        info.append(product_info.text)
    info = [s for s in info if not'\xa0'in s]

        #画像
    for img in soup.select('.detail_product_info > img'):
        product_img =(f"{img.attrs['src']}")#写真　　
        if not product_img.startswith('ht'):
            product_img = (f"http:{img.attrs['src']}")
        product_code = (f"{img.attrs['alt']}")#写真のファイル名
        product_code = product_code+'{}'.format(i)
        product_code = product_code+'.jpg'
        print(product_img)
        save_path = output_folder.joinpath(product_code)
        image = requests.get(product_img)
        open(save_path,'wb').write(image.content)
        time.sleep(3)
        i = i + 1
    for img in soup.select('.detail_product_info > p img'):
        product_img = (f"{img.attrs['src']}")#写真　
        if not product_img.startswith('ht'):
            product_img = (f"http:{img.attrs['src']}")
        product_code = (f"{img.attrs['alt']}")#写真のファイル名
        product_code = product_code+'{}'.format(j)
        product_code = product_code+'.jpg'
        print(product_code)
        save_path = output_folder.joinpath(product_code)
        image = requests.get(product_img)
        open(save_path,'wb').write(image.content)
        time.sleep(3)
        j = j + 1


    BREAK = BREAK + 1
    #print(BREAK)
    if BREAK > 3:
        print('-------------BREAK--------------')
        break

    print(info)
    time.sleep(3)


#出力確認用
print(prduct_url)
print(product_img)
print(product_code)
print(prduct_url)
print(price)
print(info)
