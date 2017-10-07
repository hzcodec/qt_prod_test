#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        lbl1 = QtGui.QLabel('This is a very long text hula', self)
        lbl1.move(15, 10)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')    
        #self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    frame = Example()
    frame.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
