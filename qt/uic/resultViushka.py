# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Універ\Практика\proctica\resultViushka.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("background:#22222e;\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 260, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: white;\n"
"background:#22222e;\n"
"border:1px solid white;\n"
"border-radius:30;")
        self.pushButton.setObjectName("pushButton")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(10, 40, 381, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(150, 150))
        self.tableView.setMaximumSize(QtCore.QSize(381, 201))
        self.tableView.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"color:white;\n"
"border:1px solid white;")
        self.tableView.setMidLineWidth(1)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.verticalHeader().setCascadingSectionResizes(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Розрахунки:"))
        self.pushButton.setText(_translate("Form", "На головну"))
