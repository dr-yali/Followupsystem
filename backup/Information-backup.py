import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI_Information import Ui_Information
import mysql.connector

class MainWindow(QMainWindow, Ui_Information):

    #####定义按钮#####
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_new.clicked.connect(self.informartionnew)
        self.pushButton_save.clicked.connect(self.informartionSave)
        self.pushButton_delete.clicked.connect(self.informartiondelete)
    #~~~~~定义按钮~~~~~~~~#

    #####定义按钮功能#####

    def informartionSave(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123123",
            database="SCR"
        )
        masql = db.cursor()
        ID = self.lineEdit_ID.text()
        Status = self.comboBox_Status.currentText()
        Recorddate = self.Recorddate.text()
        Name = self.lineEdit_Name.text()
        Sex = self.comboBox_Sex.currentText()
        Age = self.lineEdit_Age.text()
        Tel = self.lineEdit_Tel.text()
        Af = '1'
        Af_LT = str(self.checkBox_Af_LT.checkState())
        Af_RT = str(self.checkBox_Af_RT.checkState())
        Other_sym = ''
        LOM = str(self.checkBox_LOM.checkState())
        Instability = str(self.checkBox_Instability.checkState())
        Neckpain = str(self.checkBox_Neckpain.checkState())
        ACjointpain = str(self.checkBox_ACjointpain.checkState())
        Duration = self.comboBox_Duration.currentText()
        Aggravation = self.comboBox_Aggravation.currentText()
        Truama = ''
        Reason = self.comboBox_Reason.currentText()
        Action  = self.comboBox_Action.currentText()
        Occupation = self.comboBox_Occupation.currentText()
        Sport = self.comboBox_Sport.currentText()
        Excerise =''
        aVAS = ''
        ProR = ''
        Dominant = ''

        if self.radioButton_Profession.isChecked():
            ProR = '0'
        elif self.radioButton_Recreational.isChecked():
            ProR = '1'
        if self.radioButton_VAS0.isChecked():
            aVAS = '0'
        elif self.radioButton_VAS1.isChecked():
            aVAS = '1'
        elif self.radioButton_VAS2.isChecked():
            aVAS = '2'
        elif self.radioButton_VAS3.isChecked():
            aVAS = '3'
        elif self.radioButton_VAS4.isChecked():
            aVAS = '4'
        elif self.radioButton_VAS5.isChecked():
            aVAS = '5'
        elif self.radioButton_VAS6.isChecked():
            aVAS = '6'
        elif self.radioButton_VAS7.isChecked():
            aVAS = '7'
        elif self.radioButton_VAS8.isChecked():
            aVAS = '8'
        elif self.radioButton_VAS9.isChecked():
            aVAS = '9'
        elif self.radioButton_VAS10.isChecked():
            aVAS = '10'

        if self.radioButton_Domin_LT.isChecked():
            Dominant = '0'
        elif self.radioButton_Domin_LT.isChecked(): Dominant ='1'

        sql = "INSERT INTO information_1" \
              " (`ID`, `Status`, `记录日期`, `姓名`, `性别`, `年龄`, `电话`, `患侧`, `LT患侧`, `RT患侧`, `其他症状`, `LOM`, `Instability`, `Neck pain`, `AC joint pain`, `VAS`, `患病时间`, `加重时间`, `外伤史`, `受伤原因`, `受伤动作`, `职业`, `有无运动`, `运动`, `专业or业余`, `优势手`) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (ID, Status, Recorddate, Name, Sex, Age, Tel, Af, Af_LT, Af_RT, Other_sym, LOM, Instability, Neckpain,
                ACjointpain, aVAS, Duration, Aggravation, Truama, Reason, Action, Occupation, Sport, Excerise, ProR,
                Dominant)


        sqla = "INSERT INTO information_1(`ID`, `Status`, `记录日期`, `姓名`, `性别`, `年龄`, `电话`, `患侧`, `LT患侧`, `RT患侧`, `其他症状`, `LOM`, `Instability`, `Neck pain`, `AC joint pain`, `pain`, `患病时间`, `加重时间`, `外伤史`, `受伤原因`, `受伤动作`, `职业`, `有无运动`, `运动`, `运动年数`, `专业or业余`, `优势手`) " \
              "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        vala = (ID, Status, Recorddate, Name, Sex, Age, Tel, Af, Af_LT, Af_RT, Other_sym, LOM, Instability, Neckpain,
                ACjointpain, aVAS, Duration, Aggravation, Truama, Reason, Action, Occupation, Sport, Excerise, ProR,
                Dominant)

        masql.execute(sql,val)
        db.commit()
        print(masql.rowcount, "条记录插入成功。")
        db.close()

    def informartionnew(self):
        print( "New file" )
    def informartiondelete(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123123",
            database="SCR"
        )
        masql = db.cursor()
        sql_d = "DELETE FROM information_1 WHERE id ='10031'"
        masql.execute(sql_d)
        db.commit()
        print(masql.rowcount, "条记录删除成功。")
        db.close()
    # ~~~~~定义按钮功能~~~~~~~~#
