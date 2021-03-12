import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import mysql.connector
from Information import MainWindow
# from Frontpage_code_b import NewcaseDialog1


class CMD_INFO(QDialog):          #弹对话框，默认显示Information信息
    def __init__(self):
        super(CMD_INFO, self).__init__()
        loadUi("./Charts/WI_information.ui", self)
    def newcase1(self):

        # widget.setCurrentIndex(0)
        _translate = QtCore.QCoreApplication.translate
        self.comboBox_Reason.setItemText(0, _translate("Form", ""))
        self.comboBox_Duration.setItemText(0, _translate("Form", ""))
        self.radioButton_Recreational.setChecked(2)
        self.radioButton_Profession.setChecked(2)
        # self.comboBox_Action.setItemText(0, _translate("Form", ""))
        # self.comboBox_Sport.setItemText(0, _translate("Form", ""))
        # self.checkBox_Diabetes.setText(_translate("Form", ""))
        # self.checkBox_Thyroid.setText(_translate("Form", ""))
        # self.checkBox_Tuberculosis.setText(_translate("Form", ""))
        # self.checkBox_Ant.setText(_translate("Form", ""))
        # self.checkBox_Posts.setText(_translate("Form", ""))
        # self.checkBox_MDI.setText(_translate("Form", ""))
        # self.checkBox_Lock.setText(_translate("Form", ""))
        # self.checkBox_Medication.setText(_translate("Form", ""))
        # self.checkBox_Physiotherapy.setText(_translate("Form", ""))
        # self.checkBox_Arthocentesis.setText(_translate("Form", ""))
        # self.checkBox_ShoulderSurgery.setText(_translate("Form", ""))
        # # self.Recorddate.setDate()
        # self.checkBox_Af_LT.setText(_translate("Form", ""))
        # self.checkBox_Af_RT.setText(_translate("Form", ""))
        # self.comboBox_4.setItemText(0, _translate("Form", ""))
        # self.comboBox_Status.setItemText(0, _translate("Form", ""))
        # self.radioButton_VAS0.setText( _translate("Form", ""))
        # self.radioButton_VAS1.setText( _translate("Form", ""))
        # self.radioButton_VAS2.setText( _translate("Form", ""))
        # self.radioButton_VAS3.setText( _translate("Form", ""))
        # self.radioButton_VAS4.setText()
        # self.radioButton_VAS5.setText()
        # self.radioButton_VAS6.setText()
        # self.radioButton_VAS7.setText()
        # self.radioButton_VAS8.setText()
        # self.radioButton_VAS9.setText()
        # self.radioButton_VAS10.setText()
        # self.checkBox_LOM.setText(_translate("Form", ""))
        # self.checkBox_Instability.setText(_translate("Form", ""))
        # self.checkBox_Neckpain.setText(_translate("Form", ""))
        # self.checkBox_ACjointpain.setText(_translate("Form", ""))
        # self.comboBox_Sex.setItemText(0, _translate("Form", ""))
        # self.radioButton_Domin_LT.setText()
        # self.comboBox_Aggravation.setItemText(0, _translate("Form", ""))
        # self.radioButton_Domin_RT.setText()
        # self.checkBox_Humerus.setText(_translate("Form", ""))
        # self.checkBox_ACCCInjury.setText(_translate("Form", ""))
        # self.checkBox_Clavivle.setText(_translate("Form", ""))
        # self.checkBox_Hypertension.setText(_translate("Form", ""))
        # self.checkBox_Breast.setText(_translate("Form", ""))
        # self.checkBox_Asthma.setText(_translate("Form", ""))
        # self.comboBox_Occupation.setItemText(0, _translate("Form", ""))
        # self.comboBox_5.setItemText(0)
        print("子界面新建病历")
    def insert(self):
        t = MainWindow
        k = t.informartionInsert(self)
    def delete(self):
        t = MainWindow
        k = t.informartionDelete(self)
    def search(self):
        t = MainWindow
        k = t.informartionSearch(self)
        self.lineEdit_ID.setText(str(k[0]))
        self.comboBox_Status.setCurrentText(str(k[1]))
        self.Recorddate.setDate(k[2])
        self.lineEdit_Name.setText(str(k[3]))
        self.comboBox_Sex.setCurrentText(str(k[2]))
        self.lineEdit_Age.setText(str(k[5]))
        self.lineEdit_Tel.setText(str(k[6]))
        self.checkBox_Af_LT.setCheckState(int(k[8]))
        self.checkBox_Af_RT.setCheckState(int(k[9]))
        self.checkBox_LOM.setCheckState(int(k[11]))
        self.checkBox_Instability.setCheckState(int(k[12]))
        self.checkBox_Neckpain.setCheckState(int(k[13]))
        self.checkBox_ACjointpain.setCheckState(int(k[14]))
        self.comboBox_Duration.setCurrentText(str(k[16]))
        self.comboBox_Aggravation.setCurrentText(str(k[17]))
        self.comboBox_Reason.setCurrentText(str(k[19]))
        self.comboBox_Action.setCurrentText(str(k[20]))
        self.comboBox_Occupation.setCurrentText(str(k[21]))
        self.comboBox_Sport.setCurrentText(str(k[23]))
        # Dominal Hand
        if int(k[26]) == 0:
            self.radioButton_Domin_LT.setChecked(1)
        else:
            self.radioButton_Domin_RT.setChecked(1)
        # ProfR
        if int(k[25]) == 0:
            self.radioButton_Profession.setChecked(1)
        else:
            self.radioButton_Recreational.setChecked(1)
        # VAS
        if int(k[15]) == 0:
            self.radioButton_VAS0.setChecked(1)
        elif int(k[15]) == 1:
            self.radioButton_VAS1.setChecked(1)
        elif int(k[15]) == 2:
            self.radioButton_VAS2.setChecked(1)
        elif int(k[15]) == 3:
            self.radioButton_VAS3.setChecked(1)
        elif int(k[15]) == 4:
            self.radioButton_VAS4.setChecked(1)
        elif int(k[15]) == 5:
            self.radioButton_VAS5.setChecked(1)
        elif int(k[15]) == 6:
            self.radioButton_VAS6.setChecked(1)
        elif int(k[15]) == 7:
            self.radioButton_VAS7.setChecked(1)
        elif int(k[15]) == 8:
            self.radioButton_VAS8.setChecked(1)
        elif int(k[15]) == 9:
            self.radioButton_VAS9.setChecked(1)
        elif int(k[15]) == 10:
            self.radioButton_VAS10.setChecked(1)
# # main
# app = QApplication(sys.argv)
# frontpage = CMD_INFO()
# widget = QtWidgets.QStackedWidget()
# widget.addWidget(frontpage)
# widget.setFixedHeight(850)
# widget.setFixedWidth(920)
# widget.show()
# try:
#     sys.exit(app.exec_())
# except:
#     print("Exiting")