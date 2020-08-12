# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Supervisorio.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Supervisorio import Ui_MainWindow
import sys

print("Abrindo")
app = QtWidgets.QApplication(sys.argv)
win = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(win)
win.show()
sys.exit(app.exec_())
print("Done")
