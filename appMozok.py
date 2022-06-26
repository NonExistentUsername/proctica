import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from qt.uic.mainViushka import Ui_Practica
from qt.uic.resultViushka import Ui_Form

#main Window init
app = QtWidgets.QApplication(sys.argv)
Practica = QtWidgets.QMainWindow()
ui = Ui_Practica()
ui.setupUi(Practica)
Practica.show()

#result Window init
global ResultForm
ResultForm = QtWidgets.QWidget()
resUi = Ui_Form()
resUi.setupUi(ResultForm)


def showResultWindow():
    Practica.close()
    ResultForm.show()

def backToMain():
    ResultForm.close()
    Practica.show()

ui.pushButton.clicked.connect(showResultWindow)
resUi.pushButton.clicked.connect(backToMain)

sys.exit(app.exec_())

