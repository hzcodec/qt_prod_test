#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class ProdTestMonitor(QtGui.QWidget):
    
    def __init__(self):
        super(ProdTestMonitor, self).__init__()

        self.setGeometry(2030, 30, 500, 300)
        self.setWindowTitle('Production Test')

        extractAction = QtGui.QAction('&Quit', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.triggered.connect(self.close_application)
        self.statusBar()

        self.initUI()
        
    def initUI(self):
        
        comPortLbl = QtGui.QLabel('This is a very long text hula bandula shit', self)
        comPortLbl.move(15, 10)

        quitBtn = QtGui.QPushButton('Quit', self)
        quitBtn.clicked.connect(self.close_application)
        quitBtn.move(5, 55)
        quitBtn.resize(50,40)
        
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Tired?', 'Do you want to quit?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

def main():
    
    app = QtGui.QApplication(sys.argv)
    frame = ProdTestMonitor()
    frame.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
