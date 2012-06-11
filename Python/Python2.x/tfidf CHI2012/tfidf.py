# -*- coding: utf-8 -*-
'''
python2
tf-idfを計算する

Created on 2012/06/03

@author: y42sora
'''
import csv
import math
import os.path

import nltk

def read_text_file(filepath):
  """
  テキストファイルを読み込んで，中身のリストを返す
  """
  text_list = []
  f = open(filepath)
  for line in f:
    for word in nltk.word_tokenize(line):
      # 単語の邪魔な部分削除
      if word.isalpha() and 1 < len(word):
        text_list.append(word.lower())
  
  return text_list

def freq_all_file(arg, dirname, names):
  '''
  指定したファイルリストから，各ファイルごとにtf-idfが高いものの上位２０単語を取り出す
  出力形式は，
  ファイル名, 単語×２０のcsv形式
  '''
    
  #ある単語がいくつの文書に登場したか
  df = dict([])
  #df計算
  for filepath in names:
    for word in read_text_file(dirname+ "\\" + filepath):
      if word not in df:
        df[word] = 1
      else:
        df[word] += 1
  
  #各単語のidfを求める
  idf = dict([])
  for word, num in df.items():
    idf[word] = math.log((len(names) * 1.0) / num)
          
  #各文書ごとにtf-idfを計算する
  tfidf_csv = csv.writer(open("tfidf.csv", 'ab'), dialect='excel')
  for filepath in names:
    read_word = read_text_file(dirname+ "\\" + filepath)
    fdist = nltk.FreqDist(read_word)
    
    #tfidfを求める
    tfidf = dict([])
    for word, num in fdist.items():
      if idf[word] != 0:
        tfidf[word] = ((num*1.0) / len(read_word)) / idf[word]
    
    #辞書のvalueでソートして一番よく出る上位２０件を多い順に取り出す
    row = [filepath]
    for word, num in sorted(tfidf.items(), key=lambda x:x[1])[-20:][::-1]:
      row.append(word)
    
    #論文ごとにtfidfが高いものの上位２０件
    tfidf_csv.writerow(row)

  
os.path.walk("C:\\test", freq_all_file, None)
  
