# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Універ\Практика\proctica\resultViushka2Label.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(280, 350)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(0, 140))
        self.label_2.setStyleSheet("background-color:#007bd1;\n"
"")
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setPixmap(QtGui.QPixmap("d:\\Універ\\Практика\\proctica\\checklist.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color:black;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.input_one = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.input_one.setFont(font)
        self.input_one.setStyleSheet("border:1px solid #007bd1;\n"
"color:black;\n"
"")
        self.input_one.setObjectName("input_one")
        self.gridLayout.addWidget(self.input_one, 2, 0, 1, 1)
        self.input_two = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.input_two.setFont(font)
        self.input_two.setStyleSheet("border:1px solid #007bd1;\n"
"color:black;\n"
"")
        self.input_two.setObjectName("input_two")
        self.gridLayout.addWidget(self.input_two, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: white;\n"
"background:#007bd1;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 20, 141, 111))
        self.label_4.setStyleSheet("background-color: #007bd1;\n"
"")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("d:\\Універ\\Практика\\proctica\\maths.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2.raise_()
        self.label.raise_()
        self.input_one.raise_()
        self.input_two.raise_()
        self.label_4.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Розрахунки:"))
        self.input_one.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.input_two.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("Form", "На головну"))
