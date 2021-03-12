import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI_Information import Ui_Information
import mysql.connector
from datetime import date

class MainWindow(QMainWindow, Ui_Information):

    #####定义按钮#####
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_new.clicked.connect(self.informartionNew)
        self.pushButton_save.clicked.connect(self.informartionSave)
        self.pushButton_delete.clicked.connect(self.informartionDelete)
        self.pushButton_Search.clicked.connect(self.informartionSearch)
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
        Action = self.comboBox_Action.currentText()
        Occupation = self.comboBox_Occupation.currentText()
        Sport = self.comboBox_Sport.currentText()
        Excerise = ''
        aVAS = ''
        ProR = ''
        Dominant = ''
        Treatment = ''
        Medication = str(self.checkBox_Medication.checkState())
        Physiotherapy = str(self.checkBox_Physiotherapy.checkState())
        Arthocentesis = str(self.checkBox_Arthocentesis.checkState())
        ShoulderSurgery = str(self.checkBox_ShoulderSurgery.checkState())
        Instabilitya = ''
        Ant = str(self.checkBox_Ant.checkState())
        Posts = str(self.checkBox_Posts.checkState())
        MDI = str(self.checkBox_MDI.checkState())
        Lock = str(self.checkBox_Lock.checkState())
        DLtime = self.lineEdit_DLtime.text()
        DLReason = self.lineEdit_DLReason.text()
        Fracture = ''
        Humerus = str(self.checkBox_Humerus.checkState())
        ACCCInjury = str(self.checkBox_ACCCInjury.checkState())
        Clavivle = str(self.checkBox_Clavivle.checkState())
        Thyroid = str(self.checkBox_Thyroid.checkState())
        Tuberculosis = str(self.checkBox_Tuberculosis.checkState())
        Hypertension = str(self.checkBox_Hypertension.checkState())
        Diabetes = str(self.checkBox_Diabetes.checkState())
        Breast = str(self.checkBox_Breast.checkState())
        Asthma = str(self.checkBox_Asthma.checkState())
        Remarks = self.lineEdit_Remarks.text()

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
        elif self.radioButton_Domin_RT.isChecked():
            Dominant = '1'



        sql1 = "INSERT INTO information_1" \
              " (`ID`, `Status`, `记录日期`, `姓名`, `性别`, `年龄`, `电话`, `患侧`, `LT患侧`, `RT患侧`, `其他症状`, `LOM`, `Instability`, `Neck pain`, `AC joint pain`, `VAS`, `患病时间`, `加重时间`, `外伤史`, `受伤原因`, `受伤动作`, `职业`, `有无运动`, `运动`, `专业or业余`, `优势手`) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val1 = (ID, Status, Recorddate, Name, Sex, Age, Tel, Af, Af_LT, Af_RT, Other_sym, LOM, Instability, Neckpain, ACjointpain, aVAS, Duration, Aggravation, Truama, Reason, Action, Occupation, Sport, Excerise, ProR, Dominant)
        sql2 = "INSERT INTO information_2" \
               "(`ID`, `治疗史`, `药物治疗`, `物理治疗`, `关节注射`, `肩部手术`, `Instability`, `Ant`, `Post`, `MDI`, `LOCK`, `D/L Times`,  `Last D/L reason`, `Fracture`, `Humerus`, `Clavicle`, `ACCC injury`, `Hypertension`, `Diabetes`, `Thyroid disease`, `Breast operation`, `Tuberculosis`, `Asthma`, `Remarks`)" \
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val2 = (ID, Treatment, Medication, Physiotherapy, Arthocentesis, ShoulderSurgery, Instabilitya, Ant, Posts, MDI, Lock, DLtime, DLReason, Fracture, Humerus, Clavivle, ACCCInjury, Hypertension, Diabetes, Thyroid, Breast, Tuberculosis, Asthma, Remarks)

        masql.execute(sql1, val1)
        masql.execute(sql2, val2)
        db.commit()
        print(masql.rowcount, "条记录插入成功。")
        db.close()

    def informartionNew(self):
        print("New file")
    def informartionDelete(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123123",
            database="SCR"
        )
        masql = db.cursor()
        sql_d1 = "DELETE FROM information_1 WHERE id ='10031'"
        sql_d2 = "DELETE FROM information_2 WHERE id ='10031'"
        masql.execute(sql_d1)
        masql.execute(sql_d2)
        db.commit()
        print(masql.rowcount, "条记录删除成功。")
        db.close()

    def informartionSearch(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123123",
            database="SCR"
        )
        masql = db.cursor()

        #imforms = (ID, Status, Recorddate, Name, Sex, Age, Tel, Af, Af_LT, Af_RT, Other_sym, LOM, Instability, Neckpain, ACjointpain, aVAS, Duration, Aggravation, Truama, Reason, Action, Occupation, Sport, Excerise, ProR, Dominant)
        sql_s1 = "select * from information_1 WHERE id ='10015'"
        sql_s2 = "select * from information_2 WHERE id ='10015'"
        masql.execute(sql_s1)
        result = masql.fetchall()
        print(masql.rowcount, "条记录查询到。")
        for x in result:
            print(x)
        masql.execute(sql_s2)
        result = masql.fetchall()
        for y in result:
            print(y)
        self.lineEdit_ID.setText(str(x[0]))
        self.comboBox_Status.setCurrentText(str(x[1]))
        self.Recorddate.setDate(x[2])
        self.lineEdit_Name.setText(str(x[3]))
        self.comboBox_Sex.setCurrentText(str(x[2]))
        self.lineEdit_Age.setText(str(x[5]))
        self.lineEdit_Tel.setText(str(x[6]))
        self.checkBox_Af_LT.setCheckState(int(x[8]))
        self.checkBox_Af_RT.setCheckState(int(x[9]))
        self.checkBox_LOM.setCheckState(int(x[11]))
        self.checkBox_Instability.setCheckState(int(x[12]))
        self.checkBox_Neckpain.setCheckState(int(x[13]))
        self.checkBox_ACjointpain.setCheckState(int(x[14]))
        #self.comboBox_Duration.setCurrentText(str(x[16]))
        #self.comboBox_Aggravation.setCurrentText(str(x[17]))
        #self.comboBox_Reason.setCurrentText(str(x[19]))
        #self.comboBox_Action.setCurrentText(str(x[20]))
        self.comboBox_Occupation.setCurrentText(str(x[21]))
        #self.comboBox_Sport.setCurrentText(str(x[23]))
        #Dominal Hand
        if int(x[26])==0:
            self.radioButton_Domin_LT.setChecked(1)
        else:
            self.radioButton_Domin_RT.setChecked(1)
        #ProfR
        if int(x[25])==0:
            self.radioButton_Profession.setChecked(1)
        else:
            self.radioButton_Recreational.setChecked(1)
        #VAS
        if int(x[15])==0:
            self.radioButton_VAS0.setChecked(1)
        elif int(x[15])==1:
            self.radioButton_VAS1.setChecked(1)
        elif int(x[15])==2:
            self.radioButton_VAS2.setChecked(1)
        elif int(x[15])==3:
            self.radioButton_VAS3.setChecked(1)
        elif int(x[15])==4:
            self.radioButton_VAS4.setChecked(1)
        elif int(x[15])==5:
            self.radioButton_VAS5.setChecked(1)
        elif int(x[15])==6:
            self.radioButton_VAS6.setChecked(1)
        elif int(x[15])==7:
            self.radioButton_VAS7.setChecked(1)
        elif int(x[15])==8:
            self.radioButton_VAS8.setChecked(1)
        elif int(x[15])==9:
            self.radioButton_VAS9.setChecked(1)
        elif int(x[15])==10:
            self.radioButton_VAS10.setChecked(1)
        db.close()
    # ~~~~~定义按钮功能~~~~~~~~#
