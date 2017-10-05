import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

#class ProdTestMonitor(QtGui.QWidget):
class ProdTestMonitor(QtGui.QMainWindow):

    def __init__(self):
        super(ProdTestMonitor, self).__init__()

        self.setGeometry(2030, 30, 500, 200)
        self.setWindowTitle('ActSafe Production Test')

        extractAction = QtGui.QAction('&Get here', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Leave the application')
        extractAction.triggered.connect(self.close_application)
        self.statusBar()

        self.initUI()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

    def initUI(self):

        lbl = QtGui.QLabel(self)
        lbl.move(200, 10)
        lbl.setText('Jennie')

        # create quit button
        quitBtn = QtGui.QPushButton('Quit', self)
        quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        quitBtn.move(5, 5)
        quitBtn.resize(50,40)


    def close_application(self):
        print('Hello')
        choice = QtGui.QMessageBox.question(self, 'Tired? Want to go home?', 'Do you want to quit?',
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
