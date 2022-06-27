import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QHeaderView
from PyQt5.QtGui import QIcon
from qt.uic.mainViushka import Ui_Practica
from qt.uic import resultViushka
from qt.uic import resultViushka2
from computing_managers import *

#main Window init
app = QtWidgets.QApplication(sys.argv)
Practica = QtWidgets.QMainWindow()
ui = Ui_Practica()
Practica.setWindowIcon(QIcon("grade.png"))

ui.setupUi(Practica)
Practica.show()

#result Window init
global ResultForm
ResultOneDimensionTableForm = QtWidgets.QWidget()
ResultOneDimensionTableUI = resultViushka.Ui_Form()
ResultOneDimensionTableUI.setupUi(ResultOneDimensionTableForm)

SimpleVariableResultForm = QtWidgets.QWidget()
SimpleVariableResultUI = resultViushka2.Ui_Form()
SimpleVariableResultUI.setupUi(SimpleVariableResultForm)


#change title 
Practica.setWindowTitle("УжНУ Практика")
ResultOneDimensionTableForm.setWindowTitle("УжНУ Практика, результат обчислювань")
SimpleVariableResultForm.setWindowTitle("УжНУ Практика, результат обчислювань")

appcontroller = None

class OneDimensionTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.__data = data

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if role == QtCore.Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(section)
            else:
                return str(self.__data[section][0])
        return None

    def columnCount(self, parent=None):
        return 1

    def rowCount(self, parent=None):
        return len(self.__data)

    def data(self, index: QModelIndex, role: int):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            if isinstance(self.__data[row][col + 1], float):
                return "{:.3f}".format(self.__data[row][col + 1])
            return str(self.__data[row][col + 1])

def OneDimensionResultView(data):
    model = OneDimensionTableModel(data)
    ResultOneDimensionTableUI.tableView.horizontalHeader().setResizeMode(QHeaderView.Stretch)

    ResultOneDimensionTableUI.tableView.setModel(model)
    ResultOneDimensionTableForm.show()

def SimpleVariableResultView(data):
    print(data)
    SimpleVariableResultUI.label.setText(data[0] + " = " + str(data[1]))
    SimpleVariableResultForm.show()

operation_id_to_ui_opener = [
    lambda result: OneDimensionResultView(result),
    lambda result: OneDimensionResultView(result),
    lambda result: OneDimensionResultView(result),
    lambda result: OneDimensionResultView(result),
    lambda result: SimpleVariableResultView(result),
    lambda result: SimpleVariableResultView(result),
    lambda result: SimpleVariableResultView(result),
    lambda result: SimpleVariableResultView(result[0]),
    lambda result: SimpleVariableResultView(result),
    lambda result: SimpleVariableResultView(result),
    lambda result: SimpleVariableResultView(result),
    lambda result: SimpleVariableResultView(result),
]


def showResultWindow():
    if appcontroller:
        try:
            result = appcontroller(ui.lang_combo.currentIndex(), ui.first_item_combo.currentIndex(), ui.second_item_combo.currentIndex(), ui.operation_combo.currentIndex())

            Practica.close()
            operation_id_to_ui_opener[ui.operation_combo.currentIndex()](result)
        except:
            QMessageBox.critical(Practica, "Помилка", "Не можливо виконати операцію!")

def backToMain(form):
    form.close()
    Practica.show()

def chooseFile():
    global appcontroller        
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(Practica ,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
    appcontroller = AppController(fileName)

ui.calculate.clicked.connect(showResultWindow)
ui.action.triggered.connect(chooseFile)
ResultOneDimensionTableUI.pushButton.clicked.connect(lambda: backToMain(ResultOneDimensionTableForm))
SimpleVariableResultUI.pushButton.clicked.connect(lambda: backToMain(SimpleVariableResultForm))

sys.exit(app.exec_())

