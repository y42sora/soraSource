# -*- coding: utf-8 -*-
'''
Created on 2012/01/09

@author: y42sora
python 2.x
'''

import sys
import PyQt4.QtGui as QtGui
import add_amazon
import webbrowser


class ButtonBoxWidget(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.setup_ui()
        
    def setup_ui(self):
        self.one = QtGui.QPushButton('1', parent=self)
        self.two = QtGui.QPushButton('2', parent=self)
        self.three = QtGui.QPushButton('3', parent=self)
        self.four = QtGui.QPushButton('4', parent=self)
        self.five = QtGui.QPushButton('5', parent=self)
        self.six = QtGui.QPushButton('6', parent=self)
        self.seven = QtGui.QPushButton('7', parent=self)
        self.eight = QtGui.QPushButton('8', parent=self)
        self.nine = QtGui.QPushButton('9', parent=self)
        self.zero = QtGui.QPushButton('0', parent=self)
        self.enter = QtGui.QPushButton('OK', parent=self)
        self.reset = QtGui.QPushButton('reset', parent=self)
        
        layout = QtGui.QGridLayout()
        layout.addWidget(self.one, 0,0)
        layout.addWidget(self.two, 0,1)
        layout.addWidget(self.three, 0,2)
        layout.addWidget(self.four, 1,0)
        layout.addWidget(self.five, 1,1)
        layout.addWidget(self.six, 1,2)
        layout.addWidget(self.seven, 2,0)
        layout.addWidget(self.eight, 2,1)
        layout.addWidget(self.nine, 2,2)
        layout.addWidget(self.reset, 3,0)
        layout.addWidget(self.zero, 3,1)
        layout.addWidget(self.enter, 3,2)
        
        self.setLayout(layout)

class DisplayWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.setup_ui()
        self.ama = add_amazon.AmazonGet()
        
    def setup_ui(self):
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        
        self.lcd_number = QtGui.QLCDNumber(parent=self)
        self.lcd_number.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        
        self.lcd_number.setFrameStyle(QtGui.QFrame.NoFrame)
        self.lcd_number.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_number.setDigitCount(7)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.lcd_number)
        self.setLayout(layout)
        
        self.num = 0
        
    def enter(self):
        url = self.ama.get_amazon_url(self.num)
        try:
            if webbrowser.open(url) == False:
                raise webbrowser.Error
        except webbrowser.Error:
            print >> sys.stderr, "open failed"
            sys.exit(1)
        
    def update_num(self):
        self.lcd_number.display("%d" % self.num)
        self.lcd_number.update()
        
    def reset(self):
        self.num = 0
        self.update_num()
        
    def add_num(self, num):
        self.num = self.num*10 + num
        self.update_num()
    
    def add_one(self):
        self.add_num(1)
    def add_two(self):
        self.add_num(2)
    def add_three(self):
        self.add_num(3)
    def add_four(self):
        self.add_num(4)
    def add_five(self):
        self.add_num(5)
    def add_six(self):
        self.add_num(6)
    def add_seven(self):
        self.add_num(7)
    def add_eight(self):
        self.add_num(8)
    def add_nine(self):
        self.add_num(9)
    def add_zero(self):
        self.add_num(0)

        
def set_signal(bt, disp):
    # ボタン毎に違う値を出す方法が解らなかったので
    bt.one.clicked.connect(disp.add_one)
    bt.two.clicked.connect(disp.add_two)
    bt.three.clicked.connect(disp.add_three)
    bt.four.clicked.connect(disp.add_four)
    bt.five.clicked.connect(disp.add_five)
    bt.six.clicked.connect(disp.add_six)
    bt.seven.clicked.connect(disp.add_seven)
    bt.eight.clicked.connect(disp.add_eight)
    bt.nine.clicked.connect(disp.add_nine)
    bt.zero.clicked.connect(disp.add_zero)
    bt.enter.clicked.connect(disp.enter)
    bt.reset.clicked.connect(disp.reset)
            
    
def main():
    app = QtGui.QApplication(sys.argv)
    
    panel = QtGui.QWidget()
    
    display_widget = DisplayWidget(parent=panel)
    button_box_widget = ButtonBoxWidget(parent=panel)
    set_signal(button_box_widget, display_widget)
    
    panel_layout = QtGui.QVBoxLayout()
    panel_layout.addWidget(display_widget)
    panel_layout.addWidget(button_box_widget)
    
    panel.setLayout(panel_layout)
    panel.setFixedSize(200,300)
    
    main_window = QtGui.QMainWindow()
    main_window.setWindowTitle(u"お年玉ドロボウ")
    main_window.setCentralWidget(panel)
    main_window.show()
    app.exec_()
    
if __name__ == '__main__':
    main()