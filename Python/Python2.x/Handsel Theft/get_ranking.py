# -*- coding: utf-8 -*-
'''
Created on 2012/01/08
Amazonランキングから100件のasinを求める

@author: y42sora
python 2.x
'''

import urllib2
import csv
from HTMLParser import HTMLParser

class TestParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.asin = []

    def handle_starttag(self,tag,attrs):
        if tag == 'div':
            for i in attrs:
                if i[0] == 'class' and i[1] == 'zg_item zg_sparseListItem':
                    for x in attrs:
                        if x[0] == 'asin':
                            self.asin.append(x[1])

# 調べるランキングURL
ranking = [
           "http://www.amazon.co.jp/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg=",
           "http://www.amazon.co.jp/gp/bestsellers/books/466298/ref=zg_bs_pg_1?ie=UTF8&pg="
           ]
pages = [1,2,3,4,5]

# 保存するファイル
save_csv = csv.writer(open('amazon.csv', 'w'))

openner = urllib2.build_opener()
parser = TestParser()

# アクセス
for url in ranking[1:]:
    for pg in pages:
        read = openner.open(url+str(pg)).read()
        parser.feed(read)

# csvに保存
for x in parser.asin:
    save_csv.writerow([x.encode('sjis')])