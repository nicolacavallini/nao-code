# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 397)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yesButton = QtWidgets.QPushButton(self.centralwidget)
        self.yesButton.setObjectName("yesButton")
        self.horizontalLayout.addWidget(self.yesButton)
        self.noButton = QtWidgets.QPushButton(self.centralwidget)
        self.noButton.setObjectName("noButton")
        self.horizontalLayout.addWidget(self.noButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.speakButton = QtWidgets.QPushButton(self.centralwidget)
        self.speakButton.setObjectName("speakButton")
        self.verticalLayout_5.addWidget(self.speakButton)
        self.phraseEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.phraseEdit.setObjectName("phraseEdit")
        self.verticalLayout_5.addWidget(self.phraseEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MCNP input Constructor"))
        self.yesButton.setText(_translate("MainWindow", "Yes"))
        self.noButton.setText(_translate("MainWindow", "No"))
        self.speakButton.setText(_translate("MainWindow", "Speak"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

