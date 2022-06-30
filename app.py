import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QBrush, QColor
from qt.uic.mainViushka import Ui_Practica
from qt.uic import resultViushka, resultViushka2, resultViushka4table, resultViushka2Label, resultViushka2tableOnly, resultAllOptions1col, resultAllOptions2col
import traceback
from app_controller import *
app = QtWidgets.QApplication(sys.argv)
Practica = QtWidgets.QMainWindow()
ui = Ui_Practica()
Practica.setWindowIcon(QIcon("grade.png"))

ui.setupUi(Practica)
Practica.show()

global ResultForm
ResultOneTableForm = QtWidgets.QWidget()
ResultOneTableUI = resultViushka.Ui_Form()
ResultOneTableUI.setupUi(ResultOneTableForm)

SimpleVariableResultForm = QtWidgets.QWidget()
SimpleVariableResultUI = resultViushka2.Ui_Form()
SimpleVariableResultUI.setupUi(SimpleVariableResultForm)

Result4TablesForm = QtWidgets.QWidget()
Result4TablesUI = resultViushka4table.Ui_Form()
Result4TablesUI.setupUi(Result4TablesForm)

Result2TablesForm = QtWidgets.QWidget()
Result2TablesUI = resultViushka2tableOnly.Ui_Form()
Result2TablesUI.setupUi(Result2TablesForm)

TwoVariablesResultForm = QtWidgets.QWidget()
TwoVariablesResultUI = resultViushka2Label.Ui_Form()
TwoVariablesResultUI.setupUi(TwoVariablesResultForm)

AllResultsForm = QtWidgets.QWidget()
AllResultsUI = resultAllOptions1col.Ui_Form()
AllResultsUI.setupUi(AllResultsForm)

AllResults2colsForm = QtWidgets.QWidget()
AllResultsUI2cols = resultAllOptions2col.Ui_Form()
AllResultsUI2cols.setupUi(AllResults2colsForm)

Practica.setWindowTitle("УжНУ Практика")
ResultOneTableForm.setWindowTitle("УжНУ Практика, результат обчислювань")
Result4TablesForm.setWindowTitle("УжНУ Практика, результат обчислювань")
SimpleVariableResultForm.setWindowTitle("УжНУ Практика, результат обчислювань")
Result2TablesForm.setWindowTitle("УжНУ Практика, результат обчислювань")
TwoVariablesResultForm.setWindowTitle("УжНУ Практика, результат обчислювань")
AllResultsForm.setWindowTitle("УжНУ Практика, результат обчислювань")
AllResults2colsForm.setWindowTitle("УжНУ Практика, результат обчислювань")


appcontroller = None

col_1 = QColor(255, 255, 255)
col_2 = QColor(230, 230, 230)
col_3 = QColor(170, 170, 170)

class OneDimensionTableModelX(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.__data = data

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if role == QtCore.Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.__data[section][0])
            else:
                return str(section + 1)
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

class OneDimensionTableModelY(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.__data = data

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if role == QtCore.Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(section + 1)
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
            num = self.__data[row][col + 1]
            if isinstance(num, float):
                return "{:.3f}".format(num)
            return str(num)


class OneDimensionTableModelXColorized(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.__data = data

        mn = mx = None
        for k, v in data:
            if mn:
                mn = min(mn, v)
            else:
                mn = v
            if mx:
                mx = max(mx, v)
            else:
                mx = v
        self.__R = mx - mn

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if role == QtCore.Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.__data[section][0])
            else:
                return str(section + 1)
        return None

    def columnCount(self, parent=None):
        return len(self.__data)

    def rowCount(self, parent=None):
        return 1

    def data(self, index: QModelIndex, role: int):
        row = index.row()
        col = index.column()
        num = self.__data[col][row + 1]
        if role == QtCore.Qt.DisplayRole:
            if isinstance(num, float):
                return "{:.3f}".format(num)
            return str(num)
        elif role == Qt.BackgroundRole:
            if 2 * self.__R / 3 <= num:
                return QBrush(col_3)
            elif self.__R / 3 <= num:
                return QBrush(col_2)
            else:
                return QBrush(col_1)

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
        row = index.row()
        col = index.column()
        num = self.__data[row][col]
        if role == QtCore.Qt.DisplayRole:
            if isinstance(num, float):
                return "{:.3f}".format(num)
            return str(num)

class TwoDimensionTableModelColorized(QtCore.QAbstractTableModel):
    def __init__(self, data, rows, columns, parent=None):
        super().__init__(parent)
        self.__data = data
        self.__rows = rows
        self.__columns = columns

        mn = mx = None
        for v in self.__data:
            for v2 in v:
                if mn:
                    mn = min(mn, v2)
                else:
                    mn = v2
                if mx:
                    mx = max(mx, v2)
                else:
                    mx = v2
        self.__R = mx - mn

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
        row = index.row()
        col = index.column()
        num = self.__data[row][col]
        if role == QtCore.Qt.DisplayRole:
            if isinstance(num, float):
                return "{:.3f}".format(num)
            return str(num)
        elif role == Qt.BackgroundRole:
            if 2 * self.__R / 3 <= num:
                return QBrush(col_3)
            elif self.__R / 3 <= num:
                return QBrush(col_2)
            else:
                return QBrush(col_1)

def OneDimensionResultView(data: list):
    model = OneDimensionTableModelXColorized(data)
    llist = data.copy()
    llist.sort(key = lambda x: x[1], reverse = True)
    llist = llist[:10]
    model2 = OneDimensionTableModelX(llist)
    Result2TablesUI.tableView.setModel(model)
    Result2TablesUI.tableView_2.setModel(model2)
    Result2TablesUI.label_2.setText("10 найбільших значень")
    Result2TablesForm.show()

def TwoDimensionResultView(data):
    rows = []
    columns = []
    new_data = []

    for k, v in data:
        rows.append(k)
    for k, v in data[0][1]:
        columns.append(k)

    llist = []
    mn = mx = None
    for k, v in data:
        tmp = []
        for k2, v2 in v:
            tmp.append(v2)
            llist.append((str(k) + ', ' + str(k2), v2))
            if mx:
                mx = max(mx, v2)
            else:
                mx = v2
            if mn:
                mn = min(mn, v2)
            else:
                mn = v2
        new_data.append(tmp)
    R = mx - mn
    llist.sort(key = lambda x: x[1], reverse = True)
    cur_pos = 0
    while cur_pos < len(llist) and 2/3 * R <= llist[cur_pos][1]:
        cur_pos += 1
    llist = llist[:cur_pos]

    model = TwoDimensionTableModelColorized(new_data, rows, columns)
    model2 = OneDimensionTableModelX(llist)
    Result2TablesUI.tableView.setModel(model)
    Result2TablesUI.tableView_2.setModel(model2)
    Result2TablesUI.label_2.setText("Значення які ходять в проміжок [2/3 * R; R]")
    Result2TablesForm.show()

def TwoTablesViews(data):
    data1, data2 = data
    model1 = OneDimensionTableModelXColorized(data1)
    model2 = OneDimensionTableModelXColorized(data2)
    llist1 = data1.copy()
    llist1.sort(key = lambda x: x[1], reverse = True)
    llist1 = llist1[:10]
    llist2 = data2.copy()
    llist2.sort(key = lambda x: x[1], reverse = True)
    llist2 = llist2[:10]
    model1_1 = OneDimensionTableModelX(llist1)
    model2_1 = OneDimensionTableModelX(llist2)
    Result4TablesUI.tableView.setModel(model1)
    Result4TablesUI.tableView_2.setModel(model2)
    Result4TablesUI.tableView_3.setModel(model1_1)
    Result4TablesUI.tableView_4.setModel(model2_1)
    Result4TablesForm.show()

def SimpleVariableResultView(str):
    SimpleVariableResultUI.label_3.setText(str)
    SimpleVariableResultForm.show()

def result_to_str(result, add = ""):
    num = result[1]
    if isinstance(num, float):
        num = "{:.3f}".format(num)
    else:
        num = str(num)

    return str(result[0]) + add + ' = ' + num

def TwoVariableResultView(strs):
    str1, str2 = strs
    TwoVariablesResultUI.input_one.setText(str1)
    TwoVariablesResultUI.input_two.setText(str2)
    TwoVariablesResultForm.show()

def createModaStr(result, dimension=None):
    if dimension:
        return 'Мода (' + dimension + '):"' + str(result[0]) + '", N(Mo_' + dimension + ') = ' + str(result[1])

    return 'Мода: "' + str(result[0]) + '", N(Mo) = ' + str(result[1])

def result_to_str2(result, add = ""):
    print(result)
    return [str(result[0][0]) + add + " = " + str(result[0][1]), str(result[1][0]) + add + " = " + str(result[1][1])]

def result_to_str2_plus(result):
    return [createModaStr(result[0][0], 'x'), createModaStr(result[1][0], 'y')]

operation_id_to_result_converter = [
    lambda result: result,
    lambda result: result,
    lambda result: result,
    lambda result: result,
    lambda result: result_to_str(result),
    lambda result: result_to_str(result),
    lambda result: result_to_str(result),
    lambda result: createModaStr(result[0]),
    lambda result: result_to_str(result),
    lambda result: result_to_str(result),
    lambda result: result_to_str(result),
    lambda result: result_to_str(result) + '%',
    lambda result: result_to_str(result, " в 2-му степені"),
]

operation_id_to_ui_opener = [
    OneDimensionResultView,
    OneDimensionResultView,
    OneDimensionResultView,
    OneDimensionResultView,
    SimpleVariableResultView,
    SimpleVariableResultView,
    SimpleVariableResultView,
    SimpleVariableResultView,
    SimpleVariableResultView,
    SimpleVariableResultView,
    SimpleVariableResultView,
    SimpleVariableResultView,
    SimpleVariableResultView,
]

def open_ui_opener(id, result):
    return operation_id_to_ui_opener[id](operation_id_to_result_converter[id](result))

operation_id_to_2d_to_result_converter = [
    lambda result: result,
    lambda result: result,
    lambda result: result,
    lambda result: result,
    lambda result: result_to_str2(result),
    lambda result: result_to_str2(result),
    lambda result: result_to_str2(result),
    lambda result: result_to_str2_plus(result),
    lambda result: result_to_str2(result),
    lambda result: result_to_str(result),
    lambda result: result_to_str2(result),
    lambda result: result_to_str2(result),
    lambda result: result_to_str2(result, " у 2-му степені"),

]

operation_id_to_2d_ui_opener = [
    TwoDimensionResultView,
    TwoTablesViews,
    TwoTablesViews,
    TwoTablesViews,
    TwoVariableResultView,
    TwoVariableResultView,
    TwoVariableResultView,
    TwoVariableResultView,
    TwoVariableResultView,
    SimpleVariableResultView,
    TwoVariableResultView,
    TwoVariableResultView,
    TwoVariableResultView,
]

def open_ui_opener_2d(id, result):
    return operation_id_to_2d_ui_opener[id](operation_id_to_2d_to_result_converter[id](result))


def showResultWindow():
    if appcontroller:
        try:
            result = appcontroller(ui.lang_combo.currentIndex(), ui.first_item_combo.currentIndex(), ui.second_item_combo.currentIndex(), ui.operation_combo.currentIndex())

            if ui.second_item_combo.currentIndex() == 0:
                open_ui_opener(ui.operation_combo.currentIndex(), result)
            else:
                open_ui_opener_2d(ui.operation_combo.currentIndex(), result)
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
    appcontroller = AppController(fileName, Practica)

def showAllResults():
    if appcontroller:
        try:
            results = appcontroller.calc_all(ui.lang_combo.currentIndex(), ui.first_item_combo.currentIndex(), ui.second_item_combo.currentIndex())

            if ui.second_item_combo.currentIndex() == 0:
                methods = appcontroller.methods_for_calc_all
                results_new = []
                for id in range(len(results)):
                    results_new.append(operation_id_to_result_converter[methods[id]](results[id]))
                
                cols = [AllResultsUI.val1, AllResultsUI.val2, AllResultsUI.val3, AllResultsUI.val4, AllResultsUI.val5, AllResultsUI.val6, AllResultsUI.val7, AllResultsUI.val8]
                for id in range(len(cols)):
                    cols[id].setText(results_new[id])
                
                AllResultsForm.show()
            else:
                methods = appcontroller.methods_for_calc_all_2d
                results_new = []
                for id in range(len(results)):
                    results_new.append(operation_id_to_2d_to_result_converter[methods[id]](results[id]))
                
                cols1 = [AllResultsUI2cols.val1, AllResultsUI2cols.val2, AllResultsUI2cols.val3, AllResultsUI2cols.val4, AllResultsUI2cols.val5, AllResultsUI2cols.val6, AllResultsUI2cols.val7, AllResultsUI2cols.val8, AllResultsUI2cols.val9]
                cols2 = [AllResultsUI2cols.val1_2, AllResultsUI2cols.val2_2, AllResultsUI2cols.val3_2, AllResultsUI2cols.val4_2, AllResultsUI2cols.val5_2, AllResultsUI2cols.val6_2, AllResultsUI2cols.val7_2, AllResultsUI2cols.val8_2, AllResultsUI2cols.val9_2]
                
                for id in range(9):
                    if id == 5:
                        cols1[id].setText(results_new[id])
                    else:
                        cols1[id].setText(results_new[id][0])
                        cols2[id].setText(results_new[id][1])

                AllResults2colsForm.show()
        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical(Practica, "Помилка", "Не можливо виконати операцію!")

def showAllResultsDone():
    pass

ui.calculate.clicked.connect(showResultWindow)
ui.calculate_2.clicked.connect(showAllResults)
ui.action.triggered.connect(chooseFile)
ResultOneTableUI.pushButton.clicked.connect(lambda: backToMain(ResultOneTableForm))
SimpleVariableResultUI.pushButton.clicked.connect(lambda: backToMain(SimpleVariableResultForm))
Result4TablesUI.pushButton.clicked.connect(lambda: backToMain(Result4TablesForm))
Result2TablesUI.pushButton.clicked.connect(lambda: backToMain(Result2TablesForm))
TwoVariablesResultUI.pushButton.clicked.connect(lambda: backToMain(TwoVariablesResultForm))
AllResultsUI.pushButton.clicked.connect(lambda: backToMain(AllResultsForm))
AllResultsUI2cols.pushButton.clicked.connect(lambda: backToMain(AllResults2colsForm))
Practica.setStyleSheet("* {background-color: white; color: black;}")

sys.exit(app.exec_())

