import sys
import datetime 
import os
import codecs
import time

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Background:
	def __init__(self, window):
		self.window = window

		#エディタのテキストエリア
		self.text_area = window.text_area

		#タイマー処理の設定
		self.setTimer()

		#現在時刻の設定。起動時に現在時刻を読み取る
		#これが保存ファイルになる
		self.now_date = datetime.datetime.today().strftime('%Y-%m-%d')
		self.window.setWindowTitle(self.now_date)

		#保存ディレクトリの設定　後で設定ファイルから読み込むようにする
		self.save_dir = "/Users/y42sora/Files/Dropbox/Data/Emacs"

		#保存フォルダ(今月)
		self.monthly_folder = self.now_date[:-3]

		#変更があったかどうか
		self.modify_flag = False
		self.modify_timer = 0

		#オートセーブまでのカウント　この回数だけdo_counterが呼ばれたらセーブする
		self.autosave_count = 5

		#ファイルの最新更新時刻
		self.save_file_time = time.ctime(0)

		#カーソル位置
		self.cursor = QTextCursor(self.text_area.textCursor())

	def setTimer(self):
		#一定時間ごとに繰り返す処理
		self.timer = QTimer()
		self.timer.setInterval(1000)
		self.timer.timeout.connect(self.do_counter)
		self.timer.start()

	def do_counter(self):
		if self.check_autosave():
			self.modify_flag = False
			self.autosave()
			self.window.setWindowTitle(self.now_date)

	def test(self):
		sys.stdout.write("push.\n")

	def insert_now_time(self):
		self.text_area.appendPlainText(datetime.datetime.today().strftime('%H:%M') + "\n")

	def check_autosave(self):
		#オートセーブまでの時間が経過したかどうか
		if self.modify_flag:
			self.window.setWindowTitle(self.now_date + " *")
			if self.autosave_count < self.modify_timer :
				return True
			else:
				self.modify_timer += 1
		return False

	def text_area_changed(self):
		#テキストエリアが変更されたときに呼び出される
		self.modify_flag = True
		self.modify_timer = 0



	def get_file_path(self):
		return self.save_dir + "/" + self.monthly_folder

	def get_full_file_path(self):
			return self.get_file_path() + "/" + self.now_date + ".txt"


	def autosave(self):
		#一定時間に起動して保存する

		#この辺にコリジョン解決を書く予定
		if os.path.exists(self.get_full_file_path()):
			mtime = os.path.getmtime(self.get_full_file_path())
		else:
			mtime = 0

		if self.save_file_time != mtime:
			"""なんか変更があったみたいだから解決しよう"""

		#全部終わったら保存
		self.write_file(self.text_area.toPlainText())


	def write_file(self, seve_text):
		#引数のテキストでファイルを保存する
		print("保存")

		if not os.path.isdir(self.get_file_path()):
			os.makedirs(self.get_file_path())

		f = codecs.open(self.get_full_file_path(), "w", encoding="utf-8")
		f.write(seve_text)

		self.save_file_time = os.path.getmtime(self.get_full_file_path())


