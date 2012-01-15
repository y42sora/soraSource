# -*- coding: utf-8 -*-
'''
Amazonのカートへ入れる処理を行う

Created on 2012/01/09

@author: y42sora
python 2.x
'''
import csv

from BeautifulSoup import BeautifulSoup

from amazon import Amazon
import api_key

class AmazonGet():
    # Amazon　のカートへ商品を入れる
    def __init__(self):
        self.amazon = Amazon(api_key.amazon_key, api_key.amazon_secret)
        self.price_file = "pricebg.csv"

    def create_cart(self,asin):
        # カートを作る。
        # 以降は返り値のcartidとhmacが必要
        # 購入はpurchaseurlにアクセス
        res = self.amazon.cartCreate(str(asin), 1)
        soup = BeautifulSoup(res)
        ans = []
        try:
            ans.append(soup.find('cartid').text.encode('sjis'))
            ans.append(soup.find('hmac').text.encode('sjis'))
            ans.append(soup.find('urlencodedhmac').text.encode('sjis'))
            ans.append(soup.find('purchaseurl').text)
        except UnicodeEncodeError:
            return []
        except AttributeError:
            return []
        return ans
    
    def cart_add(self,asin, cartid, hmac):
        # 指定された商品を一個カートに入れる
        res = self.amazon.cartAdd(asin,1,cartid, hmac)
        
    def cart_get(self, cartid, hmac):
        # カートの情報を手に入れる
        # デバッグ用
        res = self.amazon.cartGet(cartid, hmac)
        soup = BeautifulSoup(res)
        print soup.prettify()
    
        ans = []
        try:
            ans.append(soup.find('subtotal').text.encode('sjis'))
        except UnicodeEncodeError:
            return []
        except AttributeError:
            return []
        return ans

    def solv_nap(self,nap_size, item_list):
        """
        ナップサック問題を解く
        価値は全て１、商品の大きさを実際の価格にしている
        これにより、指定された値段内で商品を詰められる
        """
        gold = [-1] * (nap_size+1)
        
        gold[0] = 0
        for item in item_list:
            for i in range(nap_size+1):
                if gold[i] != -1:
                    if i+item.size < nap_size:
                        if gold[i+item.size] < gold[i] + item.price:
                            gold[i+item.size] = gold[i]+item.price
        
        # 最も最大金額に近いものを取り出す
        for i in range(nap_size, 0, -1):
            if gold[i] != -1:
                x = i
                break
            
        # 何を買ったかを調べる
        ans = []
        item_list.reverse()
        for item in item_list:
            if 0 <= x - item.size:
                if gold[x] != gold[x-item.size]: 
                    ans.append((str(item.size),str(item.asin)))
                    x -= item.size
        return ans
    
    def get_amazon_url(self,money):
        # 指定された金額でぴったりになるように商品を買う
        # 買う為のurlを返す
        reader = csv.reader(open(self.price_file, 'r'))
    
        # 必要な情報は値段とasinなのでそれを取り出す
        prices = set([])
        item_list = []
        for row in reader:
            if int(row[1]) not in prices:
                item_list.append(Item(1,int(row[1]),0,row[0], row[2]))
                prices.add(int(row[1]))
        
        items = self.solv_nap(money, item_list)
        
        if items != None:
            id = self.create_cart(items[0][1])
        for item in items[1:]:
            self.cart_add(item[1], id[0], id[1])
            
        return id[3]

class Item:
    # DPのためのアイテムを管理するクラス
    def __init__(self, price, size, count, name, asin):
        self.price = price
        self.size = size
        self.count = count
        self.name = name
        self.asin = asin