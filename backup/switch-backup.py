import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication
from Information import *

class Screen1(QDialog):
    def __init__(self):
        super(Screen1, self).__init__()
        uic.loadUi("WI_information.ui", self)
        self.pushButton_info.clicked.connect(self.gotoscreen1)
        self.pushButton_PE.clicked.connect(self.gotoscreen2)
    def gotoscreen1(self):
        widget.setCurrentIndex(0)
    def gotoscreen2(self):
        widget.setCurrentIndex(1)


class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        uic.loadUi("screen2.ui", self)
        self.pushButton_1.clicked.connect(self.gotoscreen1)
        self.pushButton_2.clicked.connect(self.gotoscreen2)
    def gotoscreen1(self):
        widget.setCurrentIndex(0)
    def gotoscreen2(self):
        widget.setCurrentIndex(1)


#main
app=QApplication(sys.argv)
screen1 = Screen1()
screen2 = Screen2()
widget=QtWidgets.QStackedWidget()
widget.addWidget(screen1)
widget.addWidget(screen2)
widget.setFixedWidth(755)
widget.setFixedHeight(770)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")

