import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QHeaderView
from PyQt5.QtGui import QIcon
from qt.uic.mainViushka import Ui_Practica
from qt.uic import resultViushka, resultViushka2, resultViushka2table, resultViushka2Label
import traceback
from computing_managers import *
app = QtWidgets.QApplication(sys.argv)
Practica = QtWidgets.QMainWindow()
ui = Ui_Practica()
Practica.setWindowIcon(QIcon("grade.png"))

ui.setupUi(Practica)
Practica.show()

global ResultForm
ResultOneDimensionTableForm = QtWidgets.QWidget()
ResultOneDimensionTableUI = resultViushka.Ui_Form()
ResultOneDimensionTableUI.setupUi(ResultOneDimensionTableForm)

SimpleVariableResultForm = QtWidgets.QWidget()
SimpleVariableResultUI = resultViushka2.Ui_Form()
SimpleVariableResultUI.setupUi(SimpleVariableResultForm)

ResultTwoDimensionTableForm = QtWidgets.QWidget()
ResultTwoDimensionTableUI = resultViushka2table.Ui_Form()
ResultTwoDimensionTableUI.setupUi(ResultTwoDimensionTableForm)

TwoVariablesResultForm = QtWidgets.QWidget()
TwoVariablesResultUI = resultViushka2Label.Ui_Form()
TwoVariablesResultUI.setupUi(TwoVariablesResultForm)

Practica.setWindowTitle("УжНУ Практика")
ResultOneDimensionTableForm.setWindowTitle("УжНУ Практика, результат обчислювань")
ResultTwoDimensionTableForm.setWindowTitle("УжНУ Практика, результат обчислювань")
SimpleVariableResultForm.setWindowTitle("УжНУ Практика, результат обчислювань")

appcontroller = None

class OneDimensionTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.__data = data

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if role == QtCore.Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.__data[section][0])
            else:
                return str(section)
        return None

    def columnCount(self, parent=None):
        return len(self.__data)

    def rowCount(self, parent=None):
        return 1

    def data(self, index: QModelIndex, role: int):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            if isinstance(self.__data[col][row + 1], float):
                return "{:.3f}".format(self.__data[col][row + 1])
            return str(self.__data[col][row + 1])

class TwoDimensionTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, rows, columns, parent=None):
        super().__init__(parent)
        self.__data = data
        self.__rows = rows
        self.__columns = columns

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if role == QtCore.Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.__columns[section])
            else:
                return str(self.__rows[section])
        return None

    def columnCount(self, parent=None):
        return len(self.__columns)

    def rowCount(self, parent=None):
        return len(self.__rows)

    def data(self, index: QModelIndex, role: int):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            num = self.__data[row][col]
            if isinstance(num, float):
                return "{:.3f}".format(num)
            return str(num)

def OneDimensionResultView(data):
    model = OneDimensionTableModel(data)
    ResultOneDimensionTableUI.tableView.setModel(model)
    ResultOneDimensionTableForm.show()

def TwoDimensionResultView(data):
    rows = []
    columns = []
    new_data = []

    for k, v in data:
        rows.append(k)
    for k, v in data[0][1]:
        columns.append(k)

    for k, v in data:
        tmp = []
        for k2, v2 in v:
            tmp.append(v2)
        new_data.append(tmp)

    model = TwoDimensionTableModel(new_data, rows, columns)
    ResultOneDimensionTableUI.tableView.setModel(model)
    ResultOneDimensionTableForm.show()

def OneDimensionResultTwoViews(data):
    data1, data2 = data
    model1 = OneDimensionTableModel(data1)
    model2 = OneDimensionTableModel(data2)
    ResultTwoDimensionTableUI.tableView.setModel(model1)
    ResultTwoDimensionTableUI.tableView_2.setModel(model2)
    ResultTwoDimensionTableForm.show()

def SimpleVariableResultView(data):
    SimpleVariableResultUI.label.setText(data[0] + " = " + str(data[1]))
    SimpleVariableResultForm.show()

def TwoVariableResultView(data):
    TwoVariablesResultUI.input_one.setText(data[0][0] + " = " + str(data[0][1]))
    TwoVariablesResultUI.input_two.setText(data[1][0] + " = " + str(data[1][1]))
    TwoVariablesResultForm.show()

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

operation_it_to_2d_ui_opener = [
    lambda result: TwoDimensionResultView(result),
    lambda result: OneDimensionResultTwoViews(result),
    lambda result: OneDimensionResultTwoViews(result),
    lambda result: OneDimensionResultTwoViews(result),
    lambda result: TwoVariableResultView(result),
    lambda result: TwoVariableResultView(result),
    lambda result: TwoVariableResultView(result),
    lambda result: TwoVariableResultView(result),
    lambda result: TwoVariableResultView(result),
    lambda result: TwoVariableResultView(result),
    lambda result: TwoVariableResultView(result),
    lambda result: TwoVariableResultView(result),
]

def showResultWindow():
    if appcontroller:
        try:
            result = appcontroller(ui.lang_combo.currentIndex(), ui.first_item_combo.currentIndex(), ui.second_item_combo.currentIndex(), ui.operation_combo.currentIndex())

            if ui.second_item_combo.currentIndex() == 0:
                operation_id_to_ui_opener[ui.operation_combo.currentIndex()](result)
            else:
                operation_it_to_2d_ui_opener[ui.operation_combo.currentIndex()](result)
            Practica.close()
        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical(Practica, "Помилка", "Не можливо виконати операцію!")

def backToMain(form):
    form.close()
    Practica.show()

def chooseFile():
    global appcontroller
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(Practica ,"QFileDialog.getOpenFileName()", "","All Files (*);;", options=options)
    appcontroller = AppController(fileName)

ui.calculate.clicked.connect(showResultWindow)
ui.action.triggered.connect(chooseFile)
ResultOneDimensionTableUI.pushButton.clicked.connect(lambda: backToMain(ResultOneDimensionTableForm))
SimpleVariableResultUI.pushButton.clicked.connect(lambda: backToMain(SimpleVariableResultForm))
ResultTwoDimensionTableUI.pushButton.clicked.connect(lambda: backToMain(ResultTwoDimensionTableForm))
TwoVariablesResultUI.pushButton.clicked.connect(lambda: backToMain(TwoVariablesResultForm))

sys.exit(app.exec_())

