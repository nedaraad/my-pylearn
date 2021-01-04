# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/frontend/ui/addForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import model
import control

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 413)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(10, 80, 81, 31))
        self.name.setObjectName("name")
        self.family = QtWidgets.QLabel(self.centralwidget)
        self.family.setGeometry(QtCore.QRect(10, 130, 101, 31))
        self.family.setObjectName("family")
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(10, 230, 141, 31))
        self.email.setObjectName("email")
        self.fname = QtWidgets.QLineEdit(self.centralwidget)
        self.fname.setGeometry(QtCore.QRect(130, 90, 201, 25))
        self.fname.setObjectName("fname")
        self.lname = QtWidgets.QLineEdit(self.centralwidget)
        self.lname.setGeometry(QtCore.QRect(130, 140, 201, 25))
        self.lname.setObjectName("lname")
        self.phone = QtWidgets.QLineEdit(self.centralwidget)
        self.phone.setGeometry(QtCore.QRect(130, 190, 113, 25))
        self.phone.setObjectName("phone")
        self.adress = QtWidgets.QLineEdit(self.centralwidget)
        self.adress.setGeometry(QtCore.QRect(130, 240, 201, 25))
        self.adress.setObjectName("adress")
        self.number = QtWidgets.QLabel(self.centralwidget)
        self.number.setGeometry(QtCore.QRect(10, 180, 121, 31))
        self.number.setObjectName("number")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(300, 330, 89, 25))
        self.add.setObjectName("add")
        self.display = QtWidgets.QTextBrowser(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(0, 270, 256, 192))
        self.display.setObjectName("display")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.add.clicked.connect(self.addPerson)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addPerson(self):
        p = model.Person(self.fname.text(), self.lname.text(), self.phone.text(), self.adress.text())
        csvpath = 'person.csv'
        control.writeToCSV(p, csvpath)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Add New Contact"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.family.setText(_translate("MainWindow", "Family"))
        self.email.setText(_translate("MainWindow", "Email Adress"))
        self.number.setText(_translate("MainWindow", "Phone Number"))
        self.add.setText(_translate("MainWindow", "ADD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
