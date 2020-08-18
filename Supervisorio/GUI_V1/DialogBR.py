# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogBR.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialogBR(object):
    def setupUi(self, dialogBR):
        dialogBR.setObjectName("dialogBR")
        dialogBR.setWindowModality(QtCore.Qt.WindowModal)
        dialogBR.resize(258, 72)
        self.verticalLayoutWidget = QtWidgets.QWidget(dialogBR)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 258, 71))
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
        self.txtCOMPort = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtCOMPort.sizePolicy().hasHeightForWidth())
        self.txtCOMPort.setSizePolicy(sizePolicy)
        self.txtCOMPort.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtCOMPort.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtCOMPort.setUndoRedoEnabled(True)
        self.txtCOMPort.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.txtCOMPort.setReadOnly(False)
        self.txtCOMPort.setObjectName("txtCOMPort")
        self.verticalLayout.addWidget(self.txtCOMPort)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dialogBR)
        self.buttonBox.accepted.connect(dialogBR.accept)
        self.buttonBox.rejected.connect(dialogBR.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogBR)

    def retranslateUi(self, dialogBR):
        _translate = QtCore.QCoreApplication.translate
        dialogBR.setWindowTitle(_translate("dialogBR", "Definir Baud Rate"))
        self.label.setText(_translate("dialogBR", "Digite o Baud Rate em bps"))
