import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import mysql.connector
from Info import CMD_INFO
# from PE import CMD_PE
# from DI import CMD_DI
# from RE import CMD_RE
# from OP import CMD_OP
# from SC import CMD_SC
class NewcaseDialog(QDialog):          #弹对话框，默认显示Information信息
    def __init__(self):
        super(NewcaseDialog, self).__init__()
        loadUi("./Charts/WI_information.ui", self)
        Info=CMD_INFO
        self.pushButton_new.clicked.connect(Info.newcase1)
        self.pushButton_save.clicked.connect(Info.insert)
        self.pushButton_delete.clicked.connect(Info.delete)
        self.pushButton_Search.clicked.connect(Info.search)
        # PE= CMD_PE
        # self.pushButton_PE_New.clicked.connect(PE.PE_New)
        # self.pushButton_PE_Edit.clicked.connect(PE.PE_Edit)
        # self.pushButton_PE_Del.clicked.connect(PE.PE_Del)
        # DI = CMD_DI
        # self.pushButton_DI_New.clicked.connect(DI.DI_New)
        # self.pushButton_DI_Edit.clicked.connect(DI.DI_Edit)
        # self.pushButton_DI_Del.clicked.connect(DI.DI_Del)
        # RE = CMD_RE
        # self.pushButton_RE_New.clicked.connect(RE.RE_New)
        # self.pushButton_RE_Edit.clicked.connect(RE.RE_Edit)
        # self.pushButton_RE_Del.clicked.connect(RE.RE_Del)
        # OP = CMD_OP
        # self.pushButton_OP_Anch.clicked.connect(self.OP_Anch)
        # self.pushButton_OP_BLSL.clicked.connect(self.OP_BLSL)
        # self.pushButton_OP_RCGT.clicked.connect(self.OP_RCGT)
        # self.pushButton_OP_LaBa.clicked.connect(self.OP_LaBa)
        # self.pushButton_OP_ACOt.clicked.connect(self.OP_ACOt)
        # SC = CMD_SC
        # self.pushButton_SC_ASES.clicked.connect(SC.SC_ASES)
        # self.pushButton_SC_SST.clicked.connect(SC.SC_SST)
        # self.pushButton_SC_Quic.clicked.connect(SC.SC_Quic)
        # self.pushButton_SC_WOSI.clicked.connect(SC.SC_WOSI)
        # self.pushButton_SC_Cons.clicked.connect(SC.SC_Cons)
        # self.pushButton_SC_UCLA.clicked.connect(SC.SC_UCLA)
        # self.pushButton_SC_Rowe.clicked.connect(SC.SC_Rowe)
        # self.pushButton_SC_PostPain.clicked.connect(SC.SC_PostPain)
        # self.pushButton_SC_Edit.clicked.connect(SC.SC_Edit)
        # self.pushButton_SC_Del.clicked.connect(SC.SC_Del)

class Frontpage(QDialog):


    def __init__(self):
        super(Frontpage, self).__init__()
        loadUi("Frontpage.ui",self)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 60)
        self.tableWidget.setColumnWidth(2, 40)
        self.tableWidget.setColumnWidth(3, 110)
        self.tableWidget.setColumnWidth(5, 110)
        self.loaddata()
        self.pushButton_Newcase.clicked.connect(self.Newcase)

    def loaddata(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123123",
            database="SCR"
        )
        masql = db.cursor()
        tablerow=0
        self.tableWidget.setRowCount(40)
        sql_s = "select * from information_1 limit 10"
        masql.execute(sql_s)
        results = masql.fetchall()
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))#ID
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[3]))#姓名
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[5]))#Age
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[1]))#Status
            tablerow+=1

    def Newcase(self):
        dlg = NewcaseDialog()
        dlg.exec_()
# main
app = QApplication(sys.argv)
frontpage = Frontpage()
widget = QtWidgets.QStackedWidget()
widget.addWidget(frontpage)
widget.setFixedHeight(850)
widget.setFixedWidth(920)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")