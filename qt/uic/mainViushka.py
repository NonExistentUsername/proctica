# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Універ\Практика\proctica\mainViushka.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Practica(object):
    def setupUi(self, Practica):
        Practica.setObjectName("Practica")
        Practica.setEnabled(True)
        Practica.resize(405, 512)
        font = QtGui.QFont()
        font.setPointSize(15)
        Practica.setFont(font)
        Practica.setAutoFillBackground(False)
        Practica.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Practica)
        self.centralwidget.setStyleSheet("selection-background-color: #007bd1;\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.operation_combo = QtWidgets.QComboBox(self.centralwidget)
        self.operation_combo.setGeometry(QtCore.QRect(10, 360, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.operation_combo.setFont(font)
        self.operation_combo.setStyleSheet("border:1px solid #007bd1;\n"
"color:black;")
        self.operation_combo.setObjectName("operation_combo")
        self.operation_combo.addItem("")
        self.operation_combo.addItem("")
        self.operation_combo.addItem("")
        self.operation_combo.addItem("")
        self.operation_combo.addItem("")
        self.operation_combo.addItem("")
        self.operation_combo.addItem("")
        self.operation_combo.addItem("")
        self.operation_combo.addItem("")
        self.operation_combo.addItem("")
        self.operation_combo.addItem("")
        self.operation_combo.addItem("")
        self.operation_combo.addItem("")
        self.first_item_combo = QtWidgets.QComboBox(self.centralwidget)
        self.first_item_combo.setGeometry(QtCore.QRect(10, 280, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.first_item_combo.setFont(font)
        self.first_item_combo.setStyleSheet("border:1px solid #007bd1;\n"
"color:black;\n"
"")
        self.first_item_combo.setObjectName("first_item_combo")
        self.first_item_combo.addItem("")
        self.first_item_combo.addItem("")
        self.first_item_combo.addItem("")
        self.first_item_combo.addItem("")
        self.first_item_combo.addItem("")
        self.first_item_combo.addItem("")
        self.first_item_combo.addItem("")
        self.lang_combo = QtWidgets.QComboBox(self.centralwidget)
        self.lang_combo.setGeometry(QtCore.QRect(10, 204, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lang_combo.setFont(font)
        self.lang_combo.setAutoFillBackground(False)
        self.lang_combo.setStyleSheet("border:1px solid #007bd1;\n"
"color:black;\n"
"\n"
"")
        self.lang_combo.setFrame(True)
        self.lang_combo.setObjectName("lang_combo")
        self.lang_combo.addItem("")
        self.lang_combo.addItem("")
        self.lang_combo.addItem("")
        self.lang_combo.addItem("")
        self.lang_combo.addItem("")
        self.lang_combo.addItem("")
        self.lang_combo.addItem("")
        self.lang_combo.addItem("")
        self.lang_combo.addItem("")
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setGeometry(QtCore.QRect(210, 440, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.calculate.setFont(font)
        self.calculate.setStyleSheet("color:white;\n"
"border:2px solid #007bd1;\n"
"background:#007bd1;\n"
"")
        self.calculate.setObjectName("calculate")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 180, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color:black;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 261, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:black;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 340, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:black;")
        self.label_3.setObjectName("label_3")
        self.second_item_combo = QtWidgets.QComboBox(self.centralwidget)
        self.second_item_combo.setGeometry(QtCore.QRect(210, 281, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.second_item_combo.setFont(font)
        self.second_item_combo.setStyleSheet("border:1px solid #007bd1;\n"
"color:black;\n"
"")
        self.second_item_combo.setObjectName("second_item_combo")
        self.second_item_combo.addItem("")
        self.second_item_combo.addItem("")
        self.second_item_combo.addItem("")
        self.second_item_combo.addItem("")
        self.second_item_combo.addItem("")
        self.second_item_combo.addItem("")
        self.second_item_combo.addItem("")
        self.second_item_combo.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 261, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:black;")
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 411, 161))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: #007bd1\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(140, 20, 121, 121))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("premium-icon-business-impact-4365114.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.calculate_2 = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_2.setGeometry(QtCore.QRect(10, 440, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.calculate_2.setFont(font)
        self.calculate_2.setStyleSheet("color:white;\n"
"border:2px solid #007bd1;\n"
"background:#007bd1;\n"
"")
        self.calculate_2.setObjectName("calculate_2")
        Practica.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Practica)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menubar.setFont(font)
        self.menubar.setMouseTracking(True)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setEnabled(True)
        self.menu.setMouseTracking(True)
        self.menu.setTabletTracking(False)
        self.menu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menu.setAutoFillBackground(False)
        self.menu.setStyleSheet("")
        self.menu.setTearOffEnabled(False)
        self.menu.setToolTipsVisible(False)
        self.menu.setObjectName("menu")
        Practica.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(Practica)
        self.action.setIconVisibleInMenu(False)
        self.action.setShortcutVisibleInContextMenu(False)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(Practica)
        QtCore.QMetaObject.connectSlotsByName(Practica)

    def retranslateUi(self, Practica):
        _translate = QtCore.QCoreApplication.translate
        Practica.setWindowTitle(_translate("Practica", "MainWindow"))
        self.operation_combo.setItemText(0, _translate("Practica", "Статистичний розподіл частот"))
        self.operation_combo.setItemText(1, _translate("Practica", "Стат. розподіл відносних частот"))
        self.operation_combo.setItemText(2, _translate("Practica", "Стат. розподіл накопичувальних частот"))
        self.operation_combo.setItemText(3, _translate("Practica", "Стат. розподіл відносних нак. частот"))
        self.operation_combo.setItemText(4, _translate("Practica", "Вибіркове середнє значення"))
        self.operation_combo.setItemText(5, _translate("Practica", "Дисперсія"))
        self.operation_combo.setItemText(6, _translate("Practica", "Середнє квадратичне відхилення"))
        self.operation_combo.setItemText(7, _translate("Practica", "Мода"))
        self.operation_combo.setItemText(8, _translate("Practica", "Медіана"))
        self.operation_combo.setItemText(9, _translate("Practica", "Коефіціент кореляції"))
        self.operation_combo.setItemText(10, _translate("Practica", "Розмах варіації"))
        self.operation_combo.setItemText(11, _translate("Practica", "Коефіціент варіації"))
        self.operation_combo.setItemText(12, _translate("Practica", "Вибіркове середнє в 2й степені"))
        self.first_item_combo.setItemText(0, _translate("Practica", "За алфавітом"))
        self.first_item_combo.setItemText(1, _translate("Practica", "За голосними"))
        self.first_item_combo.setItemText(2, _translate("Practica", "За приголосними"))
        self.first_item_combo.setItemText(3, _translate("Practica", "Окремі літери"))
        self.first_item_combo.setItemText(4, _translate("Practica", "Довжина слів"))
        self.first_item_combo.setItemText(5, _translate("Practica", "Довжина речень"))
        self.first_item_combo.setItemText(6, _translate("Practica", "Буквосполучення"))
        self.lang_combo.setItemText(0, _translate("Practica", "Українська"))
        self.lang_combo.setItemText(1, _translate("Practica", "Англійська"))
        self.lang_combo.setItemText(2, _translate("Practica", "російська"))
        self.lang_combo.setItemText(3, _translate("Practica", "Угорська"))
        self.lang_combo.setItemText(4, _translate("Practica", "Словацька"))
        self.lang_combo.setItemText(5, _translate("Practica", "Чеська"))
        self.lang_combo.setItemText(6, _translate("Practica", "Німецька"))
        self.lang_combo.setItemText(7, _translate("Practica", "Румунська"))
        self.lang_combo.setItemText(8, _translate("Practica", "Польська"))
        self.calculate.setText(_translate("Practica", "РОЗРАХУВАТИ"))
        self.label.setText(_translate("Practica", "Мова:"))
        self.label_2.setText(_translate("Practica", "Перша ознака:"))
        self.label_3.setText(_translate("Practica", "Операція:"))
        self.second_item_combo.setItemText(0, _translate("Practica", "Нічого"))
        self.second_item_combo.setItemText(1, _translate("Practica", "За алфавітом"))
        self.second_item_combo.setItemText(2, _translate("Practica", "За голосними"))
        self.second_item_combo.setItemText(3, _translate("Practica", "За приголосними"))
        self.second_item_combo.setItemText(4, _translate("Practica", "Окремі літери"))
        self.second_item_combo.setItemText(5, _translate("Practica", "Довжина слів"))
        self.second_item_combo.setItemText(6, _translate("Practica", "Довжина речень"))
        self.second_item_combo.setItemText(7, _translate("Practica", "Буквосполучення"))
        self.label_4.setText(_translate("Practica", "Друга ознака:"))
        self.calculate_2.setText(_translate("Practica", "Розрахувати всі х-ки"))
        self.menu.setTitle(_translate("Practica", "Файл"))
        self.action.setText(_translate("Practica", "Відкрити файл "))
