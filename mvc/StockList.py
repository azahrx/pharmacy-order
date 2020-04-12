from PyQt5 import QtCore, QtGui, QtWidgets
from MedicineController import MedicineController


class Ui_SupplyPage(object):
    
    def __init__(self,medController):
        self.medlist = medController.getAllMed()
        SupplyPage = QtWidgets.QMainWindow()
        self.setupUi(SupplyPage)
        SupplyPage.show()

     
    
    def setupUi(self, SupplyPage):
        SupplyPage.setObjectName("SupplyPage")
        SupplyPage.resize(576, 430)
        self.centralwidget = QtWidgets.QWidget(SupplyPage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 90, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 130, 531, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(200, 330, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        SupplyPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SupplyPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 576, 26))
        self.menubar.setObjectName("menubar")
        SupplyPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SupplyPage)
        self.statusbar.setObjectName("statusbar")
        SupplyPage.setStatusBar(self.statusbar)

        self.retranslateUi(SupplyPage)
        QtCore.QMetaObject.connectSlotsByName(SupplyPage)

    def retranslateUi(self, SupplyPage):
        _translate = QtCore.QCoreApplication.translate
        SupplyPage.setWindowTitle(_translate("SupplyPage", "SupplyPage"))
        self.label.setText(_translate("SupplyPage", "Stock List"))
        
        
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SupplyPage = QtWidgets.QMainWindow()
    ui = Ui_SupplyPage()
    ui.setupUi(SupplyPage)
    SupplyPage.show()
    sys.exit(app.exec_())
