from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox
import matplotlib.pyplot as plt

from gui.gui import Ui_MainWindow
from logic.fp import calculate_fp, adjust_fp, get_loc_by_fp
from logic.cocomo2 import app_composition, early_architecture


class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resizeTables()

        # Data
        self.loc = None

        # Buttons
        self.ui.resultFuncDotBtn.clicked.connect(self.funcDotsMethod)
        self.ui.resultCompositionBtn.clicked.connect(self.appCompositionCocomo2)
        self.ui.resultArchitectureBtn.clicked.connect(self.earlyArchitectureCocomo2)


    def earlyArchitectureCocomo2(self):
        # 1. Get data
        if (self.loc is None): 
            QMessageBox.warning(self, "Ошибка", "Количество строк кода пока неизвестно")
            return
        
        parametersDict = {
            "MULTIPLIERS": [self.ui.modelSelectPERS.currentIndex(),
                            self.ui.modelSelectRCPX.currentIndex(),
                            self.ui.modelSelectRUSE.currentIndex(),
                            self.ui.modelSelectPDIF.currentIndex(),
                            self.ui.modelSelectPREX.currentIndex(),
                            self.ui.modelSelectFSIL.currentIndex(),
                            self.ui.modelSelectSCED.currentIndex(),],
            "FACTORS"    : [self.ui.factorSelectPREC.currentIndex(),
                            self.ui.factorSelectFLEX.currentIndex(),
                            self.ui.factorSelectRESL.currentIndex(),
                            self.ui.factorSelectTEAM.currentIndex(),
                            self.ui.factorSelectPMAT.currentIndex(),],
            "LOC"        : self.loc,
        }

        salary = self.ui.avgSalaryArchitectureInput.value()

        # 2. Calculate
        resultDict = early_architecture(salary, parametersDict)

        # 3. Show result
        self.ui.resultArchitectureTable.setItem(0, 0, QTableWidgetItem(str(resultDict["WORK"])))
        self.ui.resultArchitectureTable.setItem(0, 1, QTableWidgetItem(str(resultDict["TIME"])))
        self.ui.resultArchitectureTable.setItem(0, 2, QTableWidgetItem(str(resultDict["BUDGET"])))



    def appCompositionCocomo2(self):
        # 1. Get data
        parametersDict = {
            "FORMS"  : [self.ui.screenFormEasyInput.value(), 
                        self.ui.screenFormNormalInput.value(), 
                        self.ui.screenFormHardInput.value(),],
            "REPORTS": [self.ui.reportEasyInput.value(),
                        self.ui.reportNormalInput.value(),
                        self.ui.reportHardInput.value(),],
            "MODULES": self.ui.modulesInput.value(),
            "RUSE"   : self.ui.RUSEPercentInput.value(),
            "PROD"   : self.ui.teamExpSelect.currentIndex(),
            "FACTORS": [self.ui.factorSelectPREC.currentIndex(),
                        self.ui.factorSelectFLEX.currentIndex(),
                        self.ui.factorSelectRESL.currentIndex(),
                        self.ui.factorSelectTEAM.currentIndex(),
                        self.ui.factorSelectPMAT.currentIndex(),],
        }

        salary = self.ui.avgSalaryCompositionInput.value()

        # 2. Calculate
        resultDict = app_composition(salary, parametersDict)

        # 3. Show result
        self.ui.resultCompositionTable.setItem(0, 0, QTableWidgetItem(str(resultDict["WORK"])))
        self.ui.resultCompositionTable.setItem(0, 1, QTableWidgetItem(str(resultDict["TIME"])))
        self.ui.resultCompositionTable.setItem(0, 2, QTableWidgetItem(str(resultDict["BUDGET"])))


    def funcDotsMethod(self):
        # 1. Get data
        productAttributes = self.getPoductAttributes()
        print(f"1. productAttributes = {productAttributes}")

        languagePercents = self.getLanguagePercents()
        print(f"2. languagePercents = {languagePercents}")

        funcDotsTableMatrix = self.getFuncDotsTableMatrix()
        if (funcDotsTableMatrix is None): return
        print(f"3. funcTableMatrix = \n")
        [print(row) for row in funcDotsTableMatrix]

        # 2. Calculate
        fp = calculate_fp(funcDotsTableMatrix)
        afp = adjust_fp(fp[-1], productAttributes)
        loc = get_loc_by_fp(afp, languagePercents)
        self.loc = loc

        print(f"4. fp = {fp}; afp = {afp}; loc = {loc}")

        # 3. Show result
        self.ui.resultFuncDotsTable.setItem(0, 0, QTableWidgetItem(str(fp[1])))
        self.ui.resultFuncDotsTable.setItem(0, 1, QTableWidgetItem(str(round(afp, 2))))
        self.ui.resultFuncDotsTable.setItem(0, 2, QTableWidgetItem(str(loc)))

        rows = self.ui.funcDotsTable.rowCount()
        column = self.ui.funcDotsTable.columnCount() - 1
        table = self.ui.funcDotsTable

        for row in range(rows):
            table.setItem(row, column, QTableWidgetItem(str(fp[0][row])))
            

    def getFuncDotsTableMatrix(self):
        matrix = []

        rows = self.ui.funcDotsTable.rowCount()
        columns = self.ui.funcDotsTable.columnCount()
        table = self.ui.funcDotsTable

        for row in range(rows):
            rowMatrix = []

            for column in range(columns - 1):
                try:
                    rowMatrix.append(int(table.item(row, column).text()))
                except:
                    QMessageBox.warning(self, "Ошибка", "Не целое число в таблице")
                    return None
            
            matrix.append(rowMatrix)

        return matrix


    def getPoductAttributes(self):
        return [
            self.ui.productAttributeSelect1.currentIndex(),
            self.ui.productAttributeSelect2.currentIndex(),
            self.ui.productAttributeSelect3.currentIndex(),
            self.ui.productAttributeSelect4.currentIndex(),
            self.ui.productAttributeSelect5.currentIndex(),
            self.ui.productAttributeSelect6.currentIndex(),
            self.ui.productAttributeSelect7.currentIndex(),
            self.ui.productAttributeSelect8.currentIndex(),
            self.ui.productAttributeSelect9.currentIndex(),
            self.ui.productAttributeSelect10.currentIndex(),
            self.ui.productAttributeSelect11.currentIndex(),
            self.ui.productAttributeSelect12.currentIndex(),
            self.ui.productAttributeSelect13.currentIndex(),
            self.ui.productAttributeSelect14.currentIndex(),
        ]
    

    def getLanguagePercents(self):
        return [
            self.ui.languagePercentInput1.value(),
            self.ui.languagePercentInput2.value(),
            self.ui.languagePercentInput3.value(),
            self.ui.languagePercentInput4.value(),
            self.ui.languagePercentInput5.value(),
            self.ui.languagePercentInput6.value(),
            self.ui.languagePercentInput7.value(),
            self.ui.languagePercentInput8.value(),
            self.ui.languagePercentInput9.value(),
            self.ui.languagePercentInput10.value(),
            self.ui.languagePercentInput11.value(),
            self.ui.languagePercentInput12.value(),
            self.ui.languagePercentInput13.value(),
            self.ui.languagePercentInput14.value(),
            self.ui.languagePercentInput15.value(),
            self.ui.languagePercentInput16.value(),
        ]
    

    def resizeTables(self):
        self.ui.funcDotsTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.funcDotsTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.ui.resultFuncDotsTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.resultFuncDotsTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.ui.resultCompositionTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.resultCompositionTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.ui.resultArchitectureTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.resultArchitectureTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    