# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PaymentReceipt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateReceipt(object):
    def setupUi(self, CreateReceipt):
        CreateReceipt.setObjectName("CreateReceipt")
        CreateReceipt.resize(513, 450)
        self.centralwidget = QtWidgets.QWidget(CreateReceipt)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 90, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 210, 55, 16))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(220, 180, 104, 87))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 280, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(220, 280, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 320, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 140, 61, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 140, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        CreateReceipt.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CreateReceipt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 26))
        self.menubar.setObjectName("menubar")
        CreateReceipt.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CreateReceipt)
        self.statusbar.setObjectName("statusbar")
        CreateReceipt.setStatusBar(self.statusbar)

        self.retranslateUi(CreateReceipt)
        QtCore.QMetaObject.connectSlotsByName(CreateReceipt)

    def retranslateUi(self, CreateReceipt):
        _translate = QtCore.QCoreApplication.translate
        CreateReceipt.setWindowTitle(_translate("CreateReceipt", "CreateReceipt"))
        self.label.setText(_translate("CreateReceipt", "Receipts"))
        self.label_2.setText(_translate("CreateReceipt", "Med. List"))
        self.label_3.setText(_translate("CreateReceipt", "Price"))
        self.pushButton.setText(_translate("CreateReceipt", "Pay"))
        self.label_4.setText(_translate("CreateReceipt", "PaymentID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateReceipt = QtWidgets.QMainWindow()
    ui = Ui_CreateReceipt()
    ui.setupUi(CreateReceipt)
    CreateReceipt.show()
    sys.exit(app.exec_())
