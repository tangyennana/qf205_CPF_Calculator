# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cpfcalui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
import numpy as np
import pandas as pd
from contribution_each_account import calculate_each_account
from getyearlybal import person
from escalating import escalatingPlan
from StandardPlan import standardPlan
from basic_plan2 import basic_plan
from GraphQT import GraphApp,PlotCanvas
import time

class Ui_cpfcalui(object):
    def setupUi(self, cpfcalui):
        cpfcalui.setObjectName("cpfcalui")
        cpfcalui.resize(1500, 979)
        self.label = QtWidgets.QLabel(cpfcalui)
        self.label.setGeometry(QtCore.QRect(30, 10, 301, 81))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(cpfcalui)
        self.tabWidget.setGeometry(QtCore.QRect(30, 70, 451, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 231, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(250, 10, 171, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 231, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 40, 61, 22))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 40, 61, 22))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_21.setGeometry(QtCore.QRect(330, 40, 61, 22))
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 70, 71, 22))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.label_5.setObjectName("label_5")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(120, 120, 301, 121))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 299, 119))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 300, 121))
        self.listWidget.setObjectName("listWidget")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(280, 250, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(120, 253, 31, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(153, 250, 31, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(190, 253, 51, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(240, 250, 31, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 250, 61, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(10, 290, 161, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(170, 290, 61, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 330, 181, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_8.setGeometry(QtCore.QRect(190, 330, 91, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_9.setGeometry(QtCore.QRect(290, 330, 61, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_10.setGeometry(QtCore.QRect(360, 330, 61, 22))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(10, 370, 211, 16))
        self.label_10.setObjectName("label_10")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(230, 370, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(10, 400, 131, 16))
        self.label_11.setObjectName("label_11")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(230, 400, 73, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 440, 211, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(120, 253, 31, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(360, 330, 61, 22))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(10, 290, 161, 16))
        self.label_15.setObjectName("label_15")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(230, 370, 73, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 231, 16))
        self.label_16.setObjectName("label_16")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(153, 250, 31, 22))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(10, 370, 211, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(10, 400, 131, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(190, 253, 51, 16))
        self.label_20.setObjectName("label_20")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(100, 70, 71, 22))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(190, 40, 101, 22))
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_4.setGeometry(QtCore.QRect(230, 400, 73, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(240, 250, 31, 22))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(250, 10, 171, 22))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(10, 40, 231, 16))
        self.label_21.setObjectName("label_21")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(120, 120, 300, 121))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 250, 61, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(290, 330, 61, 22))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(10, 330, 181, 16))
        self.label_22.setObjectName("label_22")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_18.setGeometry(QtCore.QRect(170, 290, 61, 22))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 250, 61, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(190, 330, 91, 22))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(320, 40, 101, 22))
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_12 = QtWidgets.QLabel(cpfcalui)
        self.label_12.setGeometry(QtCore.QRect(20, 610, 461, 251))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("photo_2018-10-01_20-06-39.jpg"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.line = QtWidgets.QFrame(cpfcalui)
        self.line.setGeometry(QtCore.QRect(480, 0, 20, 981))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.label_23 = QtWidgets.QLabel(cpfcalui)
        self.label_23.setGeometry(QtCore.QRect(520, 30, 1400, 111))
        self.label_24 = QtWidgets.QLabel(cpfcalui)
        self.label_24.setGeometry(QtCore.QRect(520, 610, 411, 251))
        self.label_24.setText("")
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_23.setObjectName("label_23")
        self.widget = QtWidgets.QWidget(cpfcalui)
        self.widget.setGeometry(QtCore.QRect(530, 170, 391, 161))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(cpfcalui)
        self.widget_2.setGeometry(QtCore.QRect(530, 350, 391, 161))
        self.widget_2.setObjectName("widget_2")
        
        # adding graph widget
        self.graph = PlotCanvas(cpfcalui, width=5, height=5)
        self.graph.setGeometry(QtCore.QRect(520, 100, 730, 500))
        self.graph.setObjectName("graph")
        # TODO: add self.graph.addData() method to add new data 


        self.retranslateUi(cpfcalui)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(cpfcalui)
    

    def retranslateUi(self, cpfcalui):
        _translate = QtCore.QCoreApplication.translate
        cpfcalui.setWindowTitle(_translate("cpfcalui", "Dialog"))
        self.label.setText(_translate("cpfcalui", "CPF CALCULATOR"))
        self.label_2.setText(_translate("cpfcalui", "Target Excess Amount For Withdrawal :"))
        self.lineEdit.setText(_translate("cpfcalui", "$"))
        self.label_3.setText(_translate("cpfcalui", "Current amount in accounts :"))
        self.lineEdit_2.setText(_translate("cpfcalui", "OA"))
        self.lineEdit_3.setText(_translate("cpfcalui", "SA"))
        self.label_4.setText(_translate("cpfcalui", "Current Age :"))
        self.label_5.setText(_translate("cpfcalui", "Salary at age :"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(True)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("cpfcalui", "Add"))
        self.label_6.setText(_translate("cpfcalui", "Age :"))
        self.label_7.setText(_translate("cpfcalui", "Salary :"))
        self.pushButton_2.setText(_translate("cpfcalui", "Del"))
        self.lineEdit_21.setText(_translate("cpfcalui", "Medi"))
        self.label_8.setText(_translate("cpfcalui", "Top up amount per year :"))
        self.lineEdit_7.setText(_translate("cpfcalui", "$"))
        self.label_9.setText(_translate("cpfcalui", "HDB loan payment (Monthly) : "))
        self.lineEdit_8.setText(_translate("cpfcalui", "No. of months"))
        self.lineEdit_9.setText(_translate("cpfcalui", "Age"))
        self.lineEdit_10.setText(_translate("cpfcalui", "$"))
        self.label_10.setText(_translate("cpfcalui", "Retirement account savings @ 55 :"))
        self.comboBox.setItemText(0, _translate("cpfcalui", "BRS"))
        self.comboBox.setItemText(1, _translate("cpfcalui", "FRS"))
        self.comboBox.setItemText(2, _translate("cpfcalui", "ERS"))
        self.label_11.setText(_translate("cpfcalui", "Monthly payout plan :"))
        self.comboBox_2.setItemText(0, _translate("cpfcalui", "SP"))
        self.comboBox_2.setItemText(1, _translate("cpfcalui", "BP"))
        self.comboBox_2.setItemText(2, _translate("cpfcalui", "EP"))
        self.pushButton_3.setText(_translate("cpfcalui", "Calculate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("cpfcalui", "You"))
        self.label_13.setText(_translate("cpfcalui", "Current Age :"))
        self.label_14.setText(_translate("cpfcalui", "Age :"))
        self.lineEdit_11.setText(_translate("cpfcalui", "$"))
        self.label_15.setText(_translate("cpfcalui", "Top up amount per year :"))
        self.comboBox_3.setItemText(0, _translate("cpfcalui", "BRS"))
        self.comboBox_3.setItemText(1, _translate("cpfcalui", "FRS"))
        self.comboBox_3.setItemText(2, _translate("cpfcalui", "ERS"))
        self.label_16.setText(_translate("cpfcalui", "Target Excess Amount For Withdrawal :"))
        self.label_17.setText(_translate("cpfcalui", "Retirement account savings @ 55 :"))
        self.label_18.setText(_translate("cpfcalui", "Monthly payout plan :"))
        self.label_19.setText(_translate("cpfcalui", "Salary at age :"))
        self.label_20.setText(_translate("cpfcalui", "Salary :"))
        self.lineEdit_14.setText(_translate("cpfcalui", "OA"))
        self.comboBox_4.setItemText(0, _translate("cpfcalui", "SP"))
        self.comboBox_4.setItemText(1, _translate("cpfcalui", "BP"))
        self.comboBox_4.setItemText(2, _translate("cpfcalui", "EP"))
        self.lineEdit_16.setText(_translate("cpfcalui", "$"))
        self.label_21.setText(_translate("cpfcalui", "Current amount in accounts :"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.setText(_translate("cpfcalui", "Del"))
        self.lineEdit_17.setText(_translate("cpfcalui", "Age"))
        self.label_22.setText(_translate("cpfcalui", "HDB loan payment (Monthly) : "))
        self.lineEdit_18.setText(_translate("cpfcalui", "$"))
        self.pushButton_5.setText(_translate("cpfcalui", "Add"))
        self.lineEdit_19.setText(_translate("cpfcalui", "No. of months"))
        self.lineEdit_20.setText(_translate("cpfcalui", "SA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("cpfcalui", "Spouse"))
        self.pushButton_2.clicked.connect(self.delete_item_listWidget)
        self.pushButton.clicked.connect(self.add_item_listWidget)
        self.pushButton_3.clicked.connect(self.cal_cpf)
        self.pushButton_4.clicked.connect(self.delete_item_listWidget2)
        self.pushButton_5.clicked.connect(self.add_item_listWidget2)
        self.label_23.setText(_translate("cpfcalui", "End Message"))
        


    def delete_item_listWidget(self):
        self.listWidget.takeItem(self.listWidget.currentRow())
        
    def add_item_listWidget(self):
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item.setText('Age:' + self.lineEdit_5.text() + ' Salary: $' + self.lineEdit_6.text())
        self.listWidget.update()
        self.listWidget.repaint()
        
    def delete_item_listWidget2(self):
        self.listWidget_2.takeItem(self.listWidget_2.currentRow())
        
    def add_item_listWidget2(self):
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item.setText('Age:' + self.lineEdit_12.text() + ' Salary: $' + self.lineEdit_15.text())
        self.listWidget_2.update()
        self.listWidget_2.repaint()
    
    def cal_cpf(self):
        #DataType Checker
        Error = ""
        try:
            i = int(self.lineEdit.text())
        except ValueError:
            Error += self.label_2.text() + " is not an integer value ! " + "\n"  
        try:
            i = int(self.lineEdit_2.text())
        except ValueError:
            Error += self.label_3.text() + " is not an integer value ! " + "\n"  
        try:
            i = int(self.lineEdit_3.text())
        except ValueError:
            Error += self.label_3.text() + " is not an integer value ! " + "\n"  
        try:
            i = int(self.lineEdit_4.text())
        except ValueError:
            Error += self.label_4.text() + " is not an integer value ! " + "\n"  
        #Convert own list to dataframe 
        try:
            age = []
            salary = []
            for i in range(self.listWidget.count()):
                word=str(self.listWidget.item(i).text())
                first=word.find(":")
                second=word.find("S")
                age.append(int(word[first+1:second]))
                salary.append(int(word[second+9:len(word)]))
            d = {'Age': age, 'Salary': salary}
            ownList = pd.DataFrame(data=d)
            print(ownList)
        except ValueError:
            Error += "Own Salary and age list contains a non integer pair ! " + "\n"
            
     
        try:
            i = int(self.lineEdit_7.text())
        except ValueError:
            Error += self.label_8.text() + " is not an integer value ! " + "\n"  
        try:
            i = int(self.lineEdit_8.text())
        except ValueError:
            Error += self.label_9.text() + " number of months is not an integer value ! " + "\n"  
        try:
            i = int(self.lineEdit_9.text())
        except ValueError:
            Error += self.label_9.text() + " age is not an integer value ! " + "\n"  
        try:
            i = int(self.lineEdit_10.text())
        except ValueError:
            Error += self.label_9.text() + " Amount is not an integer value ! " + "\n"  
        
        
        
            
        #DataType Checker End 
        
        #if no error start calculating CPF
        
        if len(Error) == 0 : 
            contribution = calculate_each_account(ownList)
            a = person(int(self.lineEdit_4.text()),int(self.lineEdit_2.text()),int(self.lineEdit_3.text()),int(self.lineEdit_21.text()),contribution)
            print(a.get_yearly_bal())
            
            if str(self.comboBox_2.currentText()) == "SP":
                monthlyPayment = standardPlan(55,a.yearly_bal.iloc[-1]['OA'],a.yearly_bal.iloc[-1]['SA'],str(self.comboBox.currentText()))
                if monthlyPayment == "Not Enough Money" :
                    self.label_23.setText("You Have Not Enough Money For Retirement!")
            if str(self.comboBox_2.currentText()) == "BP":
                monthlyPayment = basic_plan(55,a.yearly_bal.iloc[-1]['OA'],a.yearly_bal.iloc[-1]['SA'],str(self.comboBox.currentText()))
                if monthlyPayment == "Not Enough Money" :
                    self.label_23.setText("You Have Not Enough Money For Retirement!")
            if str(self.comboBox_2.currentText()) == "EP":
                monthlyPayment = escalatingPlan(55,str(self.comboBox.currentText()),a.yearly_bal.iloc[-1]['OA'],a.yearly_bal.iloc[-1]['SA'])
                if monthlyPayment == "Not Enough Money" :
                    self.label_23.setText("You Have Not Enough Money For Retirement!")
                
                
            
            
            # load the graph after calculation
            df = a.yearly_bal
            for index, row in df.iterrows():
                self.graph.addData((int(row['Age']), row['OA'], row['SA'], row['Medi']))
                #time.sleep(1)
            self.graph.generate_plot()
            
            self.label_23.setText("You Have Enough Money For Retirement!")
            QtMultimedia.QSound.play("a1jm9-bwm4f.wav")
            self.label_24.setPixmap(QtGui.QPixmap("xzRPizGbLMMDQw7HBVotrFnKLULeZl6P.jpg"))
        #if error stop and display error messages.
        else :
            self.label_23.setText(Error)

        
       



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cpfcalui = QtWidgets.QDialog()
    ui = Ui_cpfcalui()
    ui.setupUi(cpfcalui)
    cpfcalui.show()
    cpfcalui.setWindowTitle("CPF Calculator")
    cpfcalui.setWindowIcon(QtGui.QIcon("O_m2BLlJ_400x400.png"))
    sys.exit(app.exec_())
