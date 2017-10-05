import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

#class ProdTestMonitor(QtGui.QWidget):
class ProdTestMonitor(QtGui.QMainWindow):

    def __init__(self):
        super(ProdTestMonitor, self).__init__()

        self.setGeometry(2030, 30, 500, 200)
        self.setWindowTitle('ActSafe Production Test')

        extractAction = QtGui.QAction('&Quit', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.triggered.connect(self.close_application)
        self.statusBar()

        self.initUI()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

    def initUI(self):

        # bold fonts
        myFont = QtGui.QFont('Times')
        myFont.setBold(True)

        comPortLbl = QtGui.QLabel(self)
        comPortLbl.move(200, 10)
        comPortLbl.setText('COM port:')
        comPortLbl.setFont(myFont)

        comPortTxt = QtGui.QLabel(self)
        comPortTxt.move(280, 10)
        comPortTxt.setText('ttyACM0')

        # create quit button
        quitBtn = QtGui.QPushButton('Quit', self)
        quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        quitBtn.move(5, 5)
        quitBtn.resize(50,40)


    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Tired?', 'Do you want to quit?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            print('GTH')
            sys.exit()
        else:
            pass


def main():
    app = QtGui.QApplication(sys.argv)
    frame = ProdTestMonitor()
    frame.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
