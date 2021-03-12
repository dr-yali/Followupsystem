import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI_Information import Ui_Information
import mysql.connector

class MainWindow(QMainWindow,Ui_Information):

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
        Af_LT = self.checkBox_Af_LT
        Af_RT = self.checkBox_Af_RT
        Other_sym = ''
        LOM = self.checkBox_LOM
        Instability = self.checkBox_Instability
        Neckpain = self.checkBox_Neckpain
        ACjointpain = self.checkBox_ACjointpain
        Duration = self.comboBox_Duration.currentText()
        Aggravation = self.comboBox_Aggravation.currentText()
        Truama = ''
        Reason = self.comboBox_Reason.currentText()
        Action  = self.comboBox_Action.currentText()
        Occupation = self.comboBox_Occupation.currentText()
        Sport = self.comboBox_Sport.currentText()
        Excerise =''

        if self.radioButton_Profession.isChecked():
            ProR = '0'
        elif self.radioButton_Recreational.isChecked():
            ProR = '1'
        if self.radioButton_VAS0.isChecked():
            VAS = '0'
        elif self.radioButton_VAS1.isChecked():
            VAS = '1'
        elif self.radioButton_VAS2.isChecked():
            VAS = '2'
        elif self.radioButton_VAS3.isChecked():
            VAS = '3'
        elif self.radioButton_VAS4.isChecked():
            VAS = '4'
        elif self.radioButton_VAS5.isChecked():
            VAS = '5'
        elif self.radioButton_VAS6.isChecked():
            VAS = '6'
        elif self.radioButton_VAS7.isChecked():
            VAS = '7'
        elif self.radioButton_VAS8.isChecked():
            VAS = '8'
        elif self.radioButton_VAS9.isChecked():
            VAS = '9'
        elif self.radioButton_VAS10.isChecked():
            VAS = '10'

        if self.radioButton_Domin_LT.isChecked():
            Domin = '0'
        elif self.radioButton_Domin_LT.isChecked(): Domin ='1'

sql = "INSERT INTO information_1" \
              " (`ID`, `Status`, `记录日期`, `姓名`, `性别`, `年龄`, `电话`, `患侧`, `LT患侧`, `RT患侧`, `其他症状`, `LOM`, `Instability`, `Neck pain`, `AC joint pain`, `VAS`, `患病时间`, `加重时间`, `外伤史`, `受伤原因`, `受伤动作`, `职业`, `有无运动`, `运动`,`专业or业余`, `优势手`) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val1 =  (ID, Status, Recorddate, Name, Sex, Age, Tel, Af, Af_LT, Af_RT, Other_sym, LOM, Instability, Neckpain, ACjointpain, VAS, Duration, Aggravation, Truama, Reason, Action, Occupation, Sport, Excerise, ProR, Domin)
        val = (ID, Status, 记录日期, 姓名, 性别, '53', '13905872212', '', 'RT', '', 'None', '', '', '', '', '', '180', '0', '有\n√', '拉伤',
'具体不详', '无', '', '无', '', '', '右')

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
        sql_d = "DELETE FROM information_1 WHERE id =10031'"
        masql.execute(sql_d)
        db.commit()
        print(masql.rowcount, "条记录删除成功。")
        db.close()
    # ~~~~~定义按钮功能~~~~~~~~#
