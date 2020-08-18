# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogCSVSelect.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialogCSVSelect(object):
    def setupUi(self, dialogCSVSelect):
        dialogCSVSelect.setObjectName("dialogCSVSelect")
        dialogCSVSelect.setWindowModality(QtCore.Qt.WindowModal)
        dialogCSVSelect.resize(276, 92)
        self.verticalLayoutWidget = QtWidgets.QWidget(dialogCSVSelect)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 258, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.txtPath = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPath.sizePolicy().hasHeightForWidth())
        self.txtPath.setSizePolicy(sizePolicy)
        self.txtPath.setObjectName("txtPath")
        self.verticalLayout.addWidget(self.txtPath)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dialogCSVSelect)
        self.buttonBox.accepted.connect(dialogCSVSelect.accept)
        self.buttonBox.rejected.connect(dialogCSVSelect.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogCSVSelect)

    def retranslateUi(self, dialogCSVSelect):
        _translate = QtCore.QCoreApplication.translate
        dialogCSVSelect.setWindowTitle(_translate("dialogCSVSelect", "Escolher arquivo csv"))
        self.label.setText(_translate("dialogCSVSelect", "Digite o caminho do arquivo csv com extensão"))
