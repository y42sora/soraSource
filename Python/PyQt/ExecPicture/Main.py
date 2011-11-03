import sys
from PyQt4.QtGui import *
import os


import Steganography

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        
        self.setWindowTitle("D&D")
        self.resize(360, 240)
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore() 
    
    def dropEvent(self, event):
        files = [unicode(u.toLocalFile()) for u in event.mimeData().urls()]
        for f in files:
            print f
            file("output.py", "w").write(Steganography.uncover(f))
            os.system("python output.py")
            
    
app = QApplication(sys.argv)
w = MainWidget()
w.show()
exit(app.exec_())