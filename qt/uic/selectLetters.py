# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Універ\Практика\proctica\selectLetters.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(263, 350)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(6, 6, 251, 150))
        self.label_2.setMinimumSize(QtCore.QSize(0, 150))
        self.label_2.setStyleSheet("background-color: #007bd1;")
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setPixmap(QtGui.QPixmap("d:\\Універ\\Практика\\proctica\\checklist.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(6, 160, 181, 19))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(6, 183, 251, 30))
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:1px solid #007bd1;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 30, 141, 111))
        self.label_3.setMinimumSize(QtCore.QSize(141, 111))
        self.label_3.setStyleSheet("background-color: #007bd1;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("d:\\Універ\\Практика\\proctica\\maths.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 91, 25))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:white;\n"
"border:2px solid #007bd1;\n"
"background:#007bd1;")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Введіть буквосполучення:"))
        self.pushButton.setText(_translate("Form", "Готово"))
