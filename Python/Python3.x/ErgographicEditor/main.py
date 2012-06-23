from PyQt4.QtCore import *
from PyQt4.QtGui  import *

import background


class ApplicationWindow(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self)
		
		self.setWindowTitle("てきすとえでぃたー")

		self.text_area = TextArea(self)
		self.setCentralWidget(self.text_area)

		self.bg = background.Background(self)
		self.text_area.set_background(self.bg)


	def keyPressEvent(self, ev):
		if ev.key()==Qt.Key_Q:
			if (ev.modifiers() and Qt.ControlModifier):
 				self.bg.insert_now_time()


class TextArea(QPlainTextEdit):
	def __init__(self, parent=None):
		QPlainTextEdit.__init__(self)
		self.count = 0

	def set_background(self, bg):
		self.bg = bg
	
	def inputMethodEvent(self, ev):
		self.bg.text_area_changed()
		QPlainTextEdit.inputMethodEvent(self, ev)

	def keyReleaseEvent(self, ev):
		self.bg.text_area_changed()

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)

	win = ApplicationWindow()
	win.show()
	sys.exit( app.exec_() )

