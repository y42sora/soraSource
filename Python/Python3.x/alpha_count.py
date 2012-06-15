'''
python3
Created on 2012/06/05

@author: y42sora
'''
import os.path
import csv
import codecs

reg_ext = ["c","cpp","py","js","xml","css","html","java","php","tex","perl","cc","rb","f90","ada","po","go","scala"]
file_type_dic = dict([])

#エラー出力
er = open('erros.txt', 'w')

class FileType:
  def __init__(self, ext):
    self.ext = ext
    self.count = 0
    
    self.dic = dict([])
    for w in range(ord(' '), ord('~')+1):
      self.dic[chr(w)] = 0
      
  def open_and_add_dic(self, filename, encoding):
    #対象のファイルを指定したエンコーディングで読み込む
    
    #ファイル読み込みでエラーがあったとき対策
    f = codecs.open(filename, encoding=encoding)
    lines = []
    for line in f:
      lines.append(line)
      
    #無事読み込みできたら処理する
    for line in lines:
      for w in line.lower():
        if w in self.dic:
          self.dic[w] += 1
    self.count += 1
    
  def add_dic(self, filename):
    #対象のファイルを読み込んで登録する
    
    try:
      self.open_and_add_dic(filename,"utf-8")
    except Exception as Excep:
      try:
        self.open_and_add_dic(filename,"cp1252")
      except:
        #ファイル読み込みができなかった場合
        print(Excep, filename)
        er.write(str(Excep) + " " + str(filename) + "\n")
    
  def get_str(self):
    #出力用のリストを取得する
    ans = [self.ext, self.count]
    for w in range(ord(' '), ord('~')+1):
      ans.append(str(self.dic[chr(w)]))
      
    return ans 

def add_file(filepath):
  #対象のファイルを登録する
  
  root, ext = os.path.splitext(filepath)
  ext = ext[1:].lower()
  
  #登録されていない拡張子は無視する
  if ext in reg_ext:
    if ext not in file_type_dic:
      file_type_dic[ext] = FileType(ext)
    file_type_dic[ext].add_dic(filepath)


#計算する
for path, dirs, filenames in os.walk("C:\\test"):
  for filename in filenames:
    add_file(path+"\\"+ filename)

log_csv = csv.writer(open("alpha_count.csv", 'w'), lineterminator="\n")
#何番目が何に対応しているかを出力
meta = ['filetype', 'filecount']
for w in range(ord(' '), ord('~')+1):
  meta.append(str(chr(w)))
log_csv.writerow(meta)

#各ファイルタイプごとのデータを出力
for ext,file_type in file_type_dic.items():
  log_csv.writerow(file_type.get_str())    


"""
# 拡張子の出現回数順に出力する
ext_dic = dict([])
for path, dirs, filenames in os.walk("C:\\test"):
  for filename in filenames:
    ext = os.path.splitext(filename)[1][1:].lower()
    if ext not in ext_dic:
      ext_dic[ext] = 0
    ext_dic[ext] += 1

for k, v in sorted(ext_dic.items(), key=lambda x:x[1]):
  print(k,v)
"""