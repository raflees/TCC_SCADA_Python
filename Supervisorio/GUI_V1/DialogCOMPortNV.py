# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogCOMPort.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialogCOMPort(object):
    def setupUi(self, dialogCOMPort):
        dialogCOMPort.setObjectName("dialogCOMPort")
        dialogCOMPort.setWindowModality(QtCore.Qt.WindowModal)
        dialogCOMPort.resize(259, 71)
        self.verticalLayoutWidget = QtWidgets.QWidget(dialogCOMPort)
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

        self.retranslateUi(dialogCOMPort)
        self.buttonBox.accepted.connect(dialogCOMPort.accept)
        self.buttonBox.rejected.connect(dialogCOMPort.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogCOMPort)

    def retranslateUi(self, dialogCOMPort):
        _translate = QtCore.QCoreApplication.translate
        dialogCOMPort.setWindowTitle(_translate("dialogCOMPort", "Definir COM Port"))
        self.label.setText(_translate("dialogCOMPort", "Digite o nome da porta serial conectada ao arduino"))
