# -*- coding: utf-8 -*-

'''
Created on 2011/09/15

@author: y42sora
'''

class RgbConnection(object):
	'''
	RGB通信をするクラス
	一ビットづつpushDataに入れていく
	Falseが戻ってきた場合はデータの読み落としがある。
	Trueが帰ってきた場合は読めている
	8bit事に書き込みをしていく
	
	'''

	def __init__(self):
		self.flag = False
		self.data = None
		self.decode_data = None

	def start_connection(self):
		"""
		rgb通信を開始する
		このときデータが受信中だったら中断し、Falseを返して通信を初めからやり直す
		
		Returns:
		boole :　中断されずに通信できたかどうか
		"""

		print "start_connection"
		
		self.rgb = -1
		self.count  = 0
		if self.data != None:
			self.data = ""
			return False
		self.data = ""
		
		return True

	def stop_connection(self):
		"""
		rgb通信を終了する
		          このときデータが受信できていなかった場合、Falseを返す
		         受信できた場合はself.decode_dataに保存され、get_dacode_dataで読み出す
		
		Returns:
		    bool : データが受信できたかどうか
		"""
		
		if self.data == None: return False
		if len(self.data) != 8:	return False;
		
		self.decode_data = chr(int(self.data, 2))
		self.data = None
		return True

	def get_decode_data(self):
		"""
		通信結果をデコードしたものを返す
		常に最後に読んだものを返す
		
		Returns:
		読み込んだ文字のasciiコード
		読み込んだ事がない場合はNoneを返す
		"""
		return self.decode_data

	def push_data(self, rgb):
		""" 二進数が渡されるので、self.dataに書き込む
		
		Returns:
		bool : 通信終了かどうか
		"""
		
		if rgb != 2:
			self.rgb = rgb
			return False
		if self.rgb == -1:
                        """
			self.count = self.count + 1
			if 100 < self.count :
				self.start_connection()
			"""
			return False
		
		self.data = self.data+str(self.rgb)
		self.rgb = -1
		if 8 <= len(self.data) :
			self.stop_connection()
			return True
		return False

	def toConnectionData(self, binaryData):
		connectionData = []
		for binary in binaryData:
			connectionData.append(2)
			connectionData.append(binary)
		return connectionData
		
	def toBinary2(self, decimal):
		"""
		数値をバイナリ(文字列)に変換する
		ord('a')で文字をバイナリに変換できる
		"""
		if decimal == 0: return '0'
		bin_str = ""
		while decimal > 0:
			bin_str += str(decimal % 2)
			decimal >>= 1
		for i in range(len(bin_str) , 8):
			bin_str += "0"
			
		return bin_str[::-1]
