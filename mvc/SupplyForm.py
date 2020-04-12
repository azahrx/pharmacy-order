from PyQt5 import QtCore, QtGui, QtWidgets
from MedicineController import MedicineController
from StockList import Ui_SupplyPage


class Ui_FormPage(object):
    
    def __init__(self):
        self.FormPage =QtWidgets.QMainWindow()
        self.setupUi(self.FormPage)
        self.FormPage.show()

    def setupUi(self, FormPage):
        FormPage.setObjectName("FormPage")
        FormPage.resize(547, 477)
        self.centralwidget = QtWidgets.QWidget(FormPage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 130, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 190, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 230, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 190, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 280, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(230, 230, 42, 22))
        self.spinBox.setObjectName("spinBox")
        FormPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FormPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 26))
        self.menubar.setObjectName("menubar")
        FormPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FormPage)
        self.statusbar.setObjectName("statusbar")
        FormPage.setStatusBar(self.statusbar)

        self.retranslateUi(FormPage)
        QtCore.QMetaObject.connectSlotsByName(FormPage)

    def retranslateUi(self, FormPage):
        _translate = QtCore.QCoreApplication.translate
        FormPage.setWindowTitle(_translate("FormPage", "FormPage"))
        self.label.setText(_translate("FormPage", "Supply Form"))
        self.label_2.setText(_translate("FormPage", "medID"))
        self.label_3.setText(_translate("FormPage", "Quantity"))
        self.pushButton.setText(_translate("FormPage", "Proceed"))
        self.pushButton.clicked.connect(lambda: self.increaseStock(FormPage))

    def increaseStock(self, FormPage):
        idMed = self.lineEdit.text()
        stock = self.spinBox.value()

        medController = MedicineController()
        medController.increaseStock(idMed, stock)
        
        FormPage.close()
        
        self.supply = Ui_SupplyPage(medController)

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormPage = QtWidgets.QMainWindow()
    ui = Ui_FormPage()
    ui.setupUi(FormPage)
    FormPage.show()
    sys.exit(app.exec_())
