# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\2020-2021第二学期\人工智能导论\RecognitionSystem\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 458)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 20, 54, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(730, 20, 54, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(740, 350, 54, 12))
        self.label_4.setObjectName("label_4")
        self.pList = QtWidgets.QListView(self.centralwidget)
        self.pList.setGeometry(QtCore.QRect(40, 50, 211, 351))
        self.pList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pList.setObjectName("pList")
        self.inputList = QtWidgets.QListView(self.centralwidget)
        self.inputList.setGeometry(QtCore.QRect(320, 50, 181, 351))
        self.inputList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.inputList.setObjectName("inputList")
        self.addToInputButton = QtWidgets.QPushButton(self.centralwidget)
        self.addToInputButton.setGeometry(QtCore.QRect(270, 150, 31, 23))
        self.addToInputButton.setObjectName("addToInputButton")
        self.deleteFromInputButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteFromInputButton.setGeometry(QtCore.QRect(270, 190, 31, 23))
        self.deleteFromInputButton.setObjectName("deleteFromInputButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(520, 180, 91, 81))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 150, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(630, 50, 256, 281))
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setObjectName("listView")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(630, 370, 251, 31))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 923, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "专家系统"))
        self.label.setText(_translate("MainWindow", "规则库"))
        self.label_2.setText(_translate("MainWindow", "输入事实"))
        self.label_3.setText(_translate("MainWindow", "推理过程"))
        self.label_4.setText(_translate("MainWindow", "推理结果"))
        self.addToInputButton.setText(_translate("MainWindow", ">>"))
        self.deleteFromInputButton.setText(_translate("MainWindow", "<<"))
        self.radioButton.setText(_translate("MainWindow", "前向推理"))
        self.radioButton_2.setText(_translate("MainWindow", "反向推理"))
        self.pushButton.setText(_translate("MainWindow", "推理"))

