# -*- coding: utf-8 -*-
'''
asinが書かれたcsvファイルを読み、値段を取得する

Created on 2012/01/08

@author: y42sora
python 2.x
'''
import csv

import bottlenose
from BeautifulSoup import BeautifulStoneSoup

import api_key

open_filename = "amazon.csv"
save_filename = "price.csv"
amazon = bottlenose.Amazon(api_key.amazon_key, api_key.amazon_secret, Region='JP',AssociateTag=api_key.amazon_aa)

def get_title_and_price(itemid):
    # アマゾンからタイトルと値段を取ってくる
    res = amazon.ItemLookup(ItemId=itemid,ResponseGroup='ItemAttributes')
    soup = BeautifulStoneSoup(res)
    
    ans = []
    try:
        ans.append(soup.find('title').text.encode('sjis'))
        ans.append(soup.find('formattedprice').text[1:].replace(',','').encode('sjis'))
        ans.append(itemid)
    except UnicodeEncodeError:
        return []
    except AttributeError:
        return []
    return ans

save_csv = csv.writer(open(save_filename, 'w'))

with open(open_filename, 'r') as file:
    for line in file:
        title_price = get_title_and_price(line.splitlines()[0])
        if title_price:
            save_csv.writerow(title_price)

