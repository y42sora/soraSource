# -*- coding: utf-8 -*-

import urllib
import urllib2

from BeautifulSoup import BeautifulSoup


appid = "自分のを入れるべし"  # 登録したアプリケーションID
pageurl = "http://jlp.yahooapis.jp/MAService/V1/parse"

# Yahoo!形態素解析の結果をリストで返す
def yahoo_morphological(sentence, appid=appid, results="ma", filter="1|2|3|4|5|6|7|8|9|10|11|12|13"):
    sentence = sentence.encode("utf-8")
    params = urllib.urlencode({'appid':appid, 'results':results, 'filter':filter, 'sentence':sentence})
    c = urllib2.urlopen(pageurl, params)  # POSTで投稿
    soup = BeautifulSoup(c.read())
    return [[w.surface.string, w.reading.string, w.pos.string] for w in soup.ma_result.word_list]



import MeCab
m = MeCab.Tagger('')
def mecab_morphological(st):
    parsed_list = []
    st = st.encode('utf-8')
    node = m.parseToNode(st)
    node = node.next
    while node:
        parsed_list.append([node.surface.decode('utf-8')] + node.feature.decode('utf-8').split(","))
        node = node.next
    return parsed_list[:-1]



st = u"吉野家に行ったんですよ．吉野家．"
for word in mecab_morphological(st):
    print( ",".join([w for w in word]) )
print("")
for word in yahoo_morphological(st):
    print( ",".join([w for w in word]) )
