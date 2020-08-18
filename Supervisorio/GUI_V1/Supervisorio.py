# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Supervisorio.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys, os
import serial

class PlotSerie(object):
    xAxis = []
    yAxis = []
    name = ''
    color = ''
    plotted = False;
    
    def __init__(self, name, xAxis, yAxis, color):
        self.name = name
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.color = color
    
    def plot(PlotWidget):
        pen = pg.mkPen(width = 2)
        PlotWidget.setTitle(title="Plotagem")
        PlotWidget.enableAutoRange(enable=True)
        PlotWidget.plot(self.xAxis, self.yAxis, pen=pen, color=self.color)
        

class Ui_MainWindow(object):    
    ListPlots = []
    lastXAxis = []
    lastYAxis = []
    comPort = "1"
    baudRate = 9600
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(797, 0))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.LayoutSeries = QtWidgets.QVBoxLayout()
        self.LayoutSeries.setObjectName("LayoutSeries")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lblSerie_1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSerie_1.sizePolicy().hasHeightForWidth())
        self.lblSerie_1.setSizePolicy(sizePolicy)
        self.lblSerie_1.setMinimumSize(QtCore.QSize(100, 0))
        self.lblSerie_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSerie_1.setObjectName("lblSerie_1")
        self.horizontalLayout_8.addWidget(self.lblSerie_1)
        self.btnPlotar_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPlotar_1.sizePolicy().hasHeightForWidth())
        self.btnPlotar_1.setSizePolicy(sizePolicy)
        self.btnPlotar_1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnPlotar_1.setAutoRepeatDelay(300)
        self.btnPlotar_1.setAutoDefault(False)
        self.btnPlotar_1.setDefault(False)
        self.btnPlotar_1.setFlat(False)
        self.btnPlotar_1.setObjectName("btnPlotar_1")
        self.horizontalLayout_8.addWidget(self.btnPlotar_1)
        self.btnApagar_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnApagar_1.sizePolicy().hasHeightForWidth())
        self.btnApagar_1.setSizePolicy(sizePolicy)
        self.btnApagar_1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnApagar_1.setObjectName("btnApagar_1")
        self.horizontalLayout_8.addWidget(self.btnApagar_1)
        self.LayoutSeries.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lblSerie_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSerie_2.sizePolicy().hasHeightForWidth())
        self.lblSerie_2.setSizePolicy(sizePolicy)
        self.lblSerie_2.setMinimumSize(QtCore.QSize(100, 0))
        self.lblSerie_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSerie_2.setObjectName("lblSerie_2")
        self.horizontalLayout_9.addWidget(self.lblSerie_2)
        self.btnPlotar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlotar_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnPlotar_2.setObjectName("btnPlotar_2")
        self.horizontalLayout_9.addWidget(self.btnPlotar_2)
        self.btnApagar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnApagar_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnApagar_2.setObjectName("btnApagar_2")
        self.horizontalLayout_9.addWidget(self.btnApagar_2)
        self.LayoutSeries.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lblSerie_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSerie_3.sizePolicy().hasHeightForWidth())
        self.lblSerie_3.setSizePolicy(sizePolicy)
        self.lblSerie_3.setMinimumSize(QtCore.QSize(100, 0))
        self.lblSerie_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSerie_3.setObjectName("lblSerie_3")
        self.horizontalLayout_10.addWidget(self.lblSerie_3)
        self.btnPlotar_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlotar_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnPlotar_3.setObjectName("btnPlotar_3")
        self.horizontalLayout_10.addWidget(self.btnPlotar_3)
        self.btnApagar_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnApagar_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnApagar_3.setObjectName("btnApagar_3")
        self.horizontalLayout_10.addWidget(self.btnApagar_3)
        self.LayoutSeries.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lblSerie_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSerie_4.sizePolicy().hasHeightForWidth())
        self.lblSerie_4.setSizePolicy(sizePolicy)
        self.lblSerie_4.setMinimumSize(QtCore.QSize(100, 0))
        self.lblSerie_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSerie_4.setObjectName("lblSerie_4")
        self.horizontalLayout_11.addWidget(self.lblSerie_4)
        self.btnPlotar_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlotar_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnPlotar_4.setObjectName("btnPlotar_4")
        self.horizontalLayout_11.addWidget(self.btnPlotar_4)
        self.btnApagar_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btnApagar_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnApagar_4.setObjectName("btnApagar_4")
        self.horizontalLayout_11.addWidget(self.btnApagar_4)
        self.LayoutSeries.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lblSerie_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSerie_5.sizePolicy().hasHeightForWidth())
        self.lblSerie_5.setSizePolicy(sizePolicy)
        self.lblSerie_5.setMinimumSize(QtCore.QSize(100, 0))
        self.lblSerie_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSerie_5.setObjectName("lblSerie_5")
        self.horizontalLayout_12.addWidget(self.lblSerie_5)
        self.btnPlotar_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlotar_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnPlotar_5.setObjectName("btnPlotar_5")
        self.horizontalLayout_12.addWidget(self.btnPlotar_5)
        self.btnApagar_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btnApagar_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnApagar_5.setObjectName("btnApagar_5")
        self.horizontalLayout_12.addWidget(self.btnApagar_5)
        self.LayoutSeries.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lblSerie_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSerie_6.sizePolicy().hasHeightForWidth())
        self.lblSerie_6.setSizePolicy(sizePolicy)
        self.lblSerie_6.setMinimumSize(QtCore.QSize(100, 0))
        self.lblSerie_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSerie_6.setObjectName("lblSerie_6")
        self.horizontalLayout_13.addWidget(self.lblSerie_6)
        self.btnPlotar_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlotar_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnPlotar_6.setObjectName("btnPlotar_6")
        self.horizontalLayout_13.addWidget(self.btnPlotar_6)
        self.btnApagar_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btnApagar_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnApagar_6.setObjectName("btnApagar_6")
        self.horizontalLayout_13.addWidget(self.btnApagar_6)
        self.LayoutSeries.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lblSerie_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSerie_7.sizePolicy().hasHeightForWidth())
        self.lblSerie_7.setSizePolicy(sizePolicy)
        self.lblSerie_7.setMinimumSize(QtCore.QSize(100, 0))
        self.lblSerie_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSerie_7.setObjectName("lblSerie_7")
        self.horizontalLayout_14.addWidget(self.lblSerie_7)
        self.btnPlotar_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlotar_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnPlotar_7.setObjectName("btnPlotar_7")
        self.horizontalLayout_14.addWidget(self.btnPlotar_7)
        self.btnApagar_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btnApagar_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnApagar_7.setObjectName("btnApagar_7")
        self.horizontalLayout_14.addWidget(self.btnApagar_7)
        self.LayoutSeries.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lblSerie_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSerie_8.sizePolicy().hasHeightForWidth())
        self.lblSerie_8.setSizePolicy(sizePolicy)
        self.lblSerie_8.setMinimumSize(QtCore.QSize(100, 0))
        self.lblSerie_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSerie_8.setObjectName("lblSerie_8")
        self.horizontalLayout_15.addWidget(self.lblSerie_8)
        self.btnPlotar_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlotar_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnPlotar_8.setObjectName("btnPlotar_8")
        self.horizontalLayout_15.addWidget(self.btnPlotar_8)
        self.btnApagar_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btnApagar_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnApagar_8.setObjectName("btnApagar_8")
        self.horizontalLayout_15.addWidget(self.btnApagar_8)
        self.LayoutSeries.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lblSerie_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSerie_9.sizePolicy().hasHeightForWidth())
        self.lblSerie_9.setSizePolicy(sizePolicy)
        self.lblSerie_9.setMinimumSize(QtCore.QSize(100, 0))
        self.lblSerie_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSerie_9.setObjectName("lblSerie_9")
        self.horizontalLayout_16.addWidget(self.lblSerie_9)
        self.btnPlotar_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlotar_9.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnPlotar_9.setObjectName("btnPlotar_9")
        self.horizontalLayout_16.addWidget(self.btnPlotar_9)
        self.btnApagar_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btnApagar_9.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnApagar_9.setObjectName("btnApagar_9")
        self.horizontalLayout_16.addWidget(self.btnApagar_9)
        self.LayoutSeries.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.lblSerie_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSerie_10.sizePolicy().hasHeightForWidth())
        self.lblSerie_10.setSizePolicy(sizePolicy)
        self.lblSerie_10.setMinimumSize(QtCore.QSize(100, 0))
        self.lblSerie_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSerie_10.setObjectName("lblSerie_10")
        self.horizontalLayout_17.addWidget(self.lblSerie_10)
        self.btnPlotar_10 = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlotar_10.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnPlotar_10.setObjectName("btnPlotar_10")
        self.horizontalLayout_17.addWidget(self.btnPlotar_10)
        self.btnApagar_10 = QtWidgets.QPushButton(self.centralwidget)
        self.btnApagar_10.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnApagar_10.setObjectName("btnApagar_10")
        self.horizontalLayout_17.addWidget(self.btnApagar_10)
        self.LayoutSeries.addLayout(self.horizontalLayout_17)
        self.gridLayout_3.addLayout(self.LayoutSeries, 0, 2, 2, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.LayoutControle = QtWidgets.QGridLayout()
        self.LayoutControle.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.LayoutControle.setObjectName("LayoutControle")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LayoutControle.addItem(spacerItem, 0, 4, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLineWidth(5)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.txtTempoSimulacao = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtTempoSimulacao.sizePolicy().hasHeightForWidth())
        self.txtTempoSimulacao.setSizePolicy(sizePolicy)
        self.txtTempoSimulacao.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtTempoSimulacao.setFont(font)
        self.txtTempoSimulacao.setAlignment(QtCore.Qt.AlignCenter)
        self.txtTempoSimulacao.setObjectName("txtTempoSimulacao")
        self.verticalLayout_2.addWidget(self.txtTempoSimulacao)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.LayoutControle.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBoSalvarAuto = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoSalvarAuto.setMinimumSize(QtCore.QSize(200, 0))
        self.checkBoSalvarAuto.setObjectName("checkBoSalvarAuto")
        self.verticalLayout_6.addWidget(self.checkBoSalvarAuto)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEditNome = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditNome.sizePolicy().hasHeightForWidth())
        self.lineEditNome.setSizePolicy(sizePolicy)
        self.lineEditNome.setObjectName("lineEditNome")
        self.horizontalLayout_4.addWidget(self.lineEditNome)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.btnSalvarUltimaResposta = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalvarUltimaResposta.setMinimumSize(QtCore.QSize(150, 30))
        self.btnSalvarUltimaResposta.setObjectName("btnSalvarUltimaResposta")
        self.verticalLayout_6.addWidget(self.btnSalvarUltimaResposta)
        self.btnImportarCSV = QtWidgets.QPushButton(self.centralwidget)
        self.btnImportarCSV.setMinimumSize(QtCore.QSize(150, 30))
        self.btnImportarCSV.setObjectName("btnImportarCSV")
        self.verticalLayout_6.addWidget(self.btnImportarCSV)
        self.btnEnviarDados = QtWidgets.QPushButton(self.centralwidget)
        self.btnEnviarDados.setMinimumSize(QtCore.QSize(0, 50))
        self.btnEnviarDados.setObjectName("btnEnviarDados")
        self.verticalLayout_6.addWidget(self.btnEnviarDados)
        self.LayoutControle.addLayout(self.verticalLayout_6, 0, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setLineWidth(5)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_7.addWidget(self.lineEdit_7)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLineWidth(5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.LayoutControle.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.LayoutControle)
        self.PlotWidget = pg.PlotWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlotWidget.sizePolicy().hasHeightForWidth())
        self.PlotWidget.setSizePolicy(sizePolicy)
        self.PlotWidget.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.PlotWidget.setObjectName("PlotWidget")
        self.verticalLayout_4.addWidget(self.PlotWidget)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 2, 1)
        spacerItem7 = QtWidgets.QSpacerItem(50, 0, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        self.menuProgramas = QtWidgets.QMenu(self.menubar)
        self.menuProgramas.setObjectName("menuProgramas")
        self.menuConfig = QtWidgets.QMenu(self.menubar)
        self.menuConfig.setObjectName("menuConfig")
        self.menuConfigura_es_de_Comm = QtWidgets.QMenu(self.menuConfig)
        self.menuConfigura_es_de_Comm.setObjectName("menuConfigura_es_de_Comm")
        self.menuPorta_COM = QtWidgets.QMenu(self.menuConfigura_es_de_Comm)
        self.menuPorta_COM.setObjectName("menuPorta_COM")
        self.menuDefinir_Baud_Rate = QtWidgets.QMenu(self.menuConfigura_es_de_Comm)
        self.menuDefinir_Baud_Rate.setObjectName("menuDefinir_Baud_Rate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMATLAB = QtWidgets.QAction(MainWindow)
        self.actionMATLAB.setObjectName("actionMATLAB")
        self.actionTerminal = QtWidgets.QAction(MainWindow)
        self.actionTerminal.setObjectName("actionTerminal")
        self.actionPython = QtWidgets.QAction(MainWindow)
        self.actionPython.setObjectName("actionPython")
        self.actionCOM_1 = QtWidgets.QAction(MainWindow)
        self.actionCOM_1.setCheckable(True)
        self.actionCOM_1.setObjectName("actionCOM_1")
        self.actionCOM_2 = QtWidgets.QAction(MainWindow)
        self.actionCOM_2.setCheckable(True)
        self.actionCOM_2.setObjectName("actionCOM_2")
        self.actionCOM_3 = QtWidgets.QAction(MainWindow)
        self.actionCOM_3.setCheckable(True)
        self.actionCOM_3.setObjectName("actionCOM_3")
        self.actionCOM_4 = QtWidgets.QAction(MainWindow)
        self.actionCOM_4.setCheckable(True)
        self.actionCOM_4.setObjectName("actionCOM_4")
        self.actionCOM_5 = QtWidgets.QAction(MainWindow)
        self.actionCOM_5.setCheckable(True)
        self.actionCOM_5.setObjectName("actionCOM_5")
        self.actionCOM_6 = QtWidgets.QAction(MainWindow)
        self.actionCOM_6.setCheckable(True)
        self.actionCOM_6.setObjectName("actionCOM_6")
        self.actionOutra_porta = QtWidgets.QAction(MainWindow)
        self.actionOutra_porta.setObjectName("actionOutra_porta")
        self.action9600_bps = QtWidgets.QAction(MainWindow)
        self.action9600_bps.setCheckable(True)
        self.action9600_bps.setObjectName("action9600_bps")
        self.action4800_bps = QtWidgets.QAction(MainWindow)
        self.action4800_bps.setCheckable(True)
        self.action4800_bps.setObjectName("action4800_bps")
        self.action19200_bps = QtWidgets.QAction(MainWindow)
        self.action19200_bps.setCheckable(True)
        self.action19200_bps.setObjectName("action19200_bps")
        self.action38400_bps = QtWidgets.QAction(MainWindow)
        self.action38400_bps.setCheckable(True)
        self.action38400_bps.setObjectName("action38400_bps")
        self.actionOutros_valores = QtWidgets.QAction(MainWindow)
        self.actionOutros_valores.setObjectName("actionOutros_valores")
        self.menuProgramas.addAction(self.actionMATLAB)
        self.menuProgramas.addAction(self.actionTerminal)
        self.menuProgramas.addSeparator()
        self.menuProgramas.addAction(self.actionPython)
        self.menuPorta_COM.addAction(self.actionCOM_1)
        self.menuPorta_COM.addAction(self.actionCOM_2)
        self.menuPorta_COM.addAction(self.actionCOM_3)
        self.menuPorta_COM.addAction(self.actionCOM_4)
        self.menuPorta_COM.addAction(self.actionCOM_5)
        self.menuPorta_COM.addAction(self.actionCOM_6)
        self.menuPorta_COM.addSeparator()
        self.menuPorta_COM.addAction(self.actionOutra_porta)
        self.menuDefinir_Baud_Rate.addAction(self.action4800_bps)
        self.menuDefinir_Baud_Rate.addAction(self.action9600_bps)
        self.menuDefinir_Baud_Rate.addAction(self.action19200_bps)
        self.menuDefinir_Baud_Rate.addAction(self.action38400_bps)
        self.menuDefinir_Baud_Rate.addSeparator()
        self.menuDefinir_Baud_Rate.addAction(self.actionOutros_valores)
        self.menuConfigura_es_de_Comm.addAction(self.menuPorta_COM.menuAction())
        self.menuConfigura_es_de_Comm.addAction(self.menuDefinir_Baud_Rate.menuAction())
        self.menuConfig.addAction(self.menuConfigura_es_de_Comm.menuAction())
        self.menubar.addAction(self.menuProgramas.menuAction())
        self.menubar.addAction(self.menuConfig.menuAction())

        self.retranslateUi(MainWindow)
        self.actionPython.triggered.connect(self.PlotWidget.hide)
        self.actionCOM_1.triggered.connect(self.actionCOM_1.toggle)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.criarAcoes()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblSerie_1.setText(_translate("MainWindow", "Plot1"))
        self.btnPlotar_1.setText(_translate("MainWindow", "Plotar"))
        self.btnApagar_1.setText(_translate("MainWindow", "Apagar"))
        self.lblSerie_2.setText(_translate("MainWindow", "Plot2"))
        self.btnPlotar_2.setText(_translate("MainWindow", "Plotar"))
        self.btnApagar_2.setText(_translate("MainWindow", "Apagar"))
        self.lblSerie_3.setText(_translate("MainWindow", "Plot3"))
        self.btnPlotar_3.setText(_translate("MainWindow", "Plotar"))
        self.btnApagar_3.setText(_translate("MainWindow", "Apagar"))
        self.lblSerie_4.setText(_translate("MainWindow", "Plot4"))
        self.btnPlotar_4.setText(_translate("MainWindow", "Plotar"))
        self.btnApagar_4.setText(_translate("MainWindow", "Apagar"))
        self.lblSerie_5.setText(_translate("MainWindow", "Plot5"))
        self.btnPlotar_5.setText(_translate("MainWindow", "Plotar"))
        self.btnApagar_5.setText(_translate("MainWindow", "Apagar"))
        self.lblSerie_6.setText(_translate("MainWindow", "Plot6"))
        self.btnPlotar_6.setText(_translate("MainWindow", "Plotar"))
        self.btnApagar_6.setText(_translate("MainWindow", "Apagar"))
        self.lblSerie_7.setText(_translate("MainWindow", "Plot7"))
        self.btnPlotar_7.setText(_translate("MainWindow", "Plotar"))
        self.btnApagar_7.setText(_translate("MainWindow", "Apagar"))
        self.lblSerie_8.setText(_translate("MainWindow", "Plot8"))
        self.btnPlotar_8.setText(_translate("MainWindow", "Plotar"))
        self.btnApagar_8.setText(_translate("MainWindow", "Apagar"))
        self.lblSerie_9.setText(_translate("MainWindow", "Plot9"))
        self.btnPlotar_9.setText(_translate("MainWindow", "Plotar"))
        self.btnApagar_9.setText(_translate("MainWindow", "Apagar"))
        self.lblSerie_10.setText(_translate("MainWindow", "Plot10"))
        self.btnPlotar_10.setText(_translate("MainWindow", "Plotar"))
        self.btnApagar_10.setText(_translate("MainWindow", "Apagar"))
        self.label.setText(_translate("MainWindow", "Tempo de Simulacao (ms)"))
        self.txtTempoSimulacao.setText(_translate("MainWindow", "300"))
        self.checkBoSalvarAuto.setText(_translate("MainWindow", "Salvar respostas automaticamente"))
        self.label_4.setText(_translate("MainWindow", "Nome:"))
        self.lineEditNome.setText(_translate("MainWindow", "NovaSerie"))
        self.btnSalvarUltimaResposta.setText(_translate("MainWindow", "Salvar ultima resposta"))
        self.btnImportarCSV.setText(_translate("MainWindow", "Importar Serie por arquivo .csv"))
        self.btnEnviarDados.setText(_translate("MainWindow", "Enviar Dados ao controlador"))
        self.checkBox.setText(_translate("MainWindow", "Controle PID"))
        self.label_3.setText(_translate("MainWindow", "P"))
        self.lineEdit_3.setText(_translate("MainWindow", "300"))
        self.label_7.setText(_translate("MainWindow", "I"))
        self.lineEdit_7.setText(_translate("MainWindow", "300"))
        self.label_2.setText(_translate("MainWindow", "D"))
        self.lineEdit_2.setText(_translate("MainWindow", "300"))
        self.menuProgramas.setTitle(_translate("MainWindow", "Programas"))
        self.menuConfig.setTitle(_translate("MainWindow", "Config"))
        self.menuConfigura_es_de_Comm.setTitle(_translate("MainWindow", "Configurações de Comm"))
        self.menuPorta_COM.setTitle(_translate("MainWindow", "Escolher Porta"))
        self.menuDefinir_Baud_Rate.setTitle(_translate("MainWindow", "Definir Baud Rate"))
        self.actionMATLAB.setText(_translate("MainWindow", "MATLAB"))
        self.actionTerminal.setText(_translate("MainWindow", "Terminal"))
        self.actionPython.setText(_translate("MainWindow", "Python"))
        self.actionCOM_1.setText(_translate("MainWindow", "COM 1"))
        self.actionCOM_2.setText(_translate("MainWindow", "COM 2"))
        self.actionCOM_3.setText(_translate("MainWindow", "COM 3"))
        self.actionCOM_4.setText(_translate("MainWindow", "COM 4"))
        self.actionCOM_5.setText(_translate("MainWindow", "COM 5"))
        self.actionCOM_6.setText(_translate("MainWindow", "COM 6"))
        self.actionOutra_porta.setText(_translate("MainWindow", "Outra porta"))
        self.action9600_bps.setText(_translate("MainWindow", "9600 bps"))
        self.action4800_bps.setText(_translate("MainWindow", "4800 bps"))
        self.action19200_bps.setText(_translate("MainWindow", "19200 bps"))
        self.action38400_bps.setText(_translate("MainWindow", "38400 bps"))
        self.actionOutros_valores.setText(_translate("MainWindow", "Outros valores"))


    def criarAcoes(self):
        self.dlgCOMPort = QtWidgets.QDialog()
        self.dlgBaudRate = QtWidgets.QDialog()
        self.dlgCSVSelect = QtWidgets.QDialog()
        self.setupDialogBaudRate(self.dlgBaudRate)
        self.setupDialogCOMPort(self.dlgCOMPort)
        self.setupDialogCSVSelect(self.dlgCSVSelect)
        
        self.btnSalvarUltimaResposta.clicked.connect(self.salvarUltimaResposta)
        self.btnEnviarDados.clicked.connect(self.enviarDados)
        
        self.btnApagar_1.clicked.connect(lambda: self.apagarSerie(1))
        self.btnApagar_2.clicked.connect(lambda: self.apagarSerie(2))
        self.btnApagar_3.clicked.connect(lambda: self.apagarSerie(3))
        self.btnApagar_4.clicked.connect(lambda: self.apagarSerie(4))
        self.btnApagar_5.clicked.connect(lambda: self.apagarSerie(5))
        self.btnApagar_6.clicked.connect(lambda: self.apagarSerie(6))
        self.btnApagar_7.clicked.connect(lambda: self.apagarSerie(7))
        self.btnApagar_8.clicked.connect(lambda: self.apagarSerie(8))
        self.btnApagar_9.clicked.connect(lambda: self.apagarSerie(9))
        self.btnApagar_10.clicked.connect(lambda: self.apagarSerie(10))
        
        self.btnPlotar_1.clicked.connect(lambda: self.plotarSerie(1))
        self.btnPlotar_2.clicked.connect(lambda: self.plotarSerie(2))
        self.btnPlotar_3.clicked.connect(lambda: self.plotarSerie(3))
        self.btnPlotar_4.clicked.connect(lambda: self.plotarSerie(4))
        self.btnPlotar_5.clicked.connect(lambda: self.plotarSerie(5))
        self.btnPlotar_6.clicked.connect(lambda: self.plotarSerie(6))
        self.btnPlotar_7.clicked.connect(lambda: self.plotarSerie(7))
        self.btnPlotar_8.clicked.connect(lambda: self.plotarSerie(8))
        self.btnPlotar_9.clicked.connect(lambda: self.plotarSerie(9))
        self.btnPlotar_10.clicked.connect(lambda: self.plotarSerie(10))
        
        self.btnImportarCSV.clicked.connect(lambda: self.dlgCSVSelect.show())
        
        self.actionCOM_1.triggered.connect(lambda: self.setComPort(1))
        self.actionCOM_2.triggered.connect(lambda: self.setComPort(2))
        self.actionCOM_3.triggered.connect(lambda: self.setComPort(3))
        self.actionCOM_4.triggered.connect(lambda: self.setComPort(4))
        self.actionCOM_5.triggered.connect(lambda: self.setComPort(5))
        self.actionCOM_6.triggered.connect(lambda: self.setComPort(6))
        self.actionOutra_porta.triggered.connect(lambda: self.setComPort(0))
        
        self.action4800_bps.triggered.connect(lambda: self.setBaudRate(1))
        self.action9600_bps.triggered.connect(lambda: self.setBaudRate(2))
        self.action19200_bps.triggered.connect(lambda: self.setBaudRate(3))
        self.action38400_bps.triggered.connect(lambda: self.setBaudRate(4))
        self.actionOutros_valores.triggered.connect(lambda: self.setBaudRate(0))
        
        self.actionPython.triggered.connect(self.abrirPython)
        self.actionMATLAB.triggered.connect(self.abrirMATLAB)
        self.actionTerminal.triggered.connect(self.abrirCmd)
        
        self.setComPort(1)
        self.setBaudRate(2)
        self.PlotWidget.enableAutoRange(enable=True)
        self.PlotWidget.setTitle("Área de Plotagem")
        self.limparPlotList()
    
    def setComPort(self, n):
        if n == 0:
            self.dlgCOMPort.open()
            return
        lAction = {
            1:  self.actionCOM_1,
            2:  self.actionCOM_2,
            3:  self.actionCOM_3,
            4:  self.actionCOM_4,
            5:  self.actionCOM_5,
            6:  self.actionCOM_6,
        }
        print("Clearing ports")
        self.actionCOM_1.setChecked(False)
        self.actionCOM_2.setChecked(False)
        self.actionCOM_3.setChecked(False)
        self.actionCOM_4.setChecked(False)
        self.actionCOM_5.setChecked(False)
        self.actionCOM_6.setChecked(False)
        print("Checking current port ({0})".format(n))
        self.comPort = n
        act = lAction.get(n)
        act.setChecked(True)
            
    def setBaudRate(self, n):
        if n == 0:
            self.dlgBaudRate.open()
            return
        lAction = {
            1:  self.action4800_bps,
            2:  self.action9600_bps,
            3:  self.action19200_bps,
            4:  self.action38400_bps,
        }
        print("Clearing rates")
        self.action4800_bps.setChecked(False)
        self.action9600_bps.setChecked(False)
        self.action19200_bps.setChecked(False)
        self.action38400_bps.setChecked(False)
        print("Checking current rate ({0}bps)".format(4800*(2**(n-1))))
        if n != 0:
            self.baudRate = 4800*(2**(n-1))
            act = lAction.get(n)
            act.setChecked(True)
        else:
            self.baudRate = 0   
    
    def abrirCmd(self):
        os.system("cmd.exe")
    
    def abrirMATLAB(self):
        os.system("matlab")
    
    def abrirPython(self):
        print("Python")
        self.lblSerie_1.setStyleSheet("color: rgb(255, 0, 0)")
    
    def plotarSerie(self, n):
        if len(self.ListPlots) < n: return
        
        aux = self.ListPlots[n-1]
        if aux.plotted == False:
            #Plotagem de serie
            print("Plotagem da serie" + "{0}".format(n) + "-" + aux.name)
            self.PlotWidget.plot(aux.xAxis, aux.yAxis, pen=pg.mkPen(width=2), color=aux.color)
            aux.plotted = True
            self.pintarLabel(n, 'color: rgb(0, 0, 255)')
        else:
            #Desplotagem de serie
            aux.plotted = False
            self.pintarLabel(n, 'color: rgb(0, 0, 0)')
            self.updatePlotObject()
    
    def pintarLabel(self, n, ss):
        labels = {
            1: self.lblSerie_1,
            2: self.lblSerie_2,
            3: self.lblSerie_3,
            4: self.lblSerie_4,
            5: self.lblSerie_5,
            6: self.lblSerie_6,
            7: self.lblSerie_7,
            8: self.lblSerie_8,
            9: self.lblSerie_9,
            10: self.lblSerie_10,
        }
        lbl = labels.get(n)
        lbl.setStyleSheet(ss)
        
    def apagarSerie(self, n):
        if len(self.ListPlots) < n: return
        
        nome = self.ListPlots[n-1].name
        flag = self.ListPlots[n-1].plotted
        del self.ListPlots[n-1]
        print("Serie {0}-".format(n) + nome + " apagada!\n")
        if flag:
            print("Ultimo objeto apagado estava plotado\n")
            self.pintarLabel(n, 'color: rgb(0, 0, 0)')
            self.updatePlotObject()
        self.updatePlotList()
    
    def updatePlotObject(self):
        print("Limpando graficos\n")
        self.PlotWidget.clear()
        for aux in self.ListPlots:
            if aux.plotted == True:
                self.PlotWidget.plot(aux.xAxis, aux.yAxis, pen=pg.mkPen(width=2), color=aux.color)       
    
    def enviarDados(self):
        if self.comPort != 0:
            try:
                print("Tentando conexão")
                ser = serial.Serial("COM{0}".format(self.comPort), self.baudRate, timeouot=0)
            except:
                print("Conexão não estabelecida na porta {0}".format(self.comPort))
                return
        print("Enviando dados...")
        ser.write("D")
        print("Dados enviados!")
    
    def salvarUltimaResposta(self):
        print("Salvar Ultima Respota\n")
        tam = len(self.ListPlots)
        if tam == 10:
            box = QtWidgets.QMessageBox()
            box.setText("Numero maximo de plotagens armazenadas atingido.\nApague dados para salvar novas plotagens.")
            box.exec()
            return
        
        novoPlot = self.createRandomPlot(float(10+tam)/10)
        #novoPlot.name = self.lineEditNome.text()
        novoPlot.name = "Serie tg=1.{0}".format(tam)
        print(novoPlot.name + '\n')
        self.ListPlots.append(novoPlot)
        self.updatePlotList()
    
    def updatePlotList(self):
        self.limparPlotList()
        tam = len(self.ListPlots)
        print("Tam")
        print(tam)
        
        i = 0
        nome = ''
        if tam == 0: return            
        if tam > 0:
            nome = self.ListPlots[i].name
            self.lblSerie_1.setText(str(nome))
            i = i+1
        if tam > 1:
            nome = self.ListPlots[i].name
            self.lblSerie_2.setText(str(nome))
            i = i+1
        if tam > 2:
            nome = self.ListPlots[i].name
            self.lblSerie_3.setText(str(nome))
            i = i+1
        if tam > 3:
            nome = self.ListPlots[i].name
            self.lblSerie_4.setText(str(nome))
            i = i+1
        if tam > 4:
            nome = self.ListPlots[i].name
            self.lblSerie_5.setText(str(nome))
            i = i+1
        if tam > 5:
            nome = self.ListPlots[i].name
            self.lblSerie_6.setText(str(nome))
            i = i+1
        if tam > 6:
            nome = self.ListPlots[i].name
            self.lblSerie_7.setText(str(nome))
            i = i+1
        if tam > 7:
            nome = self.ListPlots[i].name
            self.lblSerie_8.setText(str(nome))
            i = i+1
        if tam > 8:
            nome = self.ListPlots[i].name
            self.lblSerie_9.setText(str(nome))
            i = i+1
        if tam > 9:
            nome = self.ListPlots[i].name
            self.lblSerie_10.setText(str(nome))
            i = i+1
         
    def limparPlotList(self):
        self.lblSerie_1.setText("")
        self.lblSerie_2.setText("")
        self.lblSerie_3.setText("")
        self.lblSerie_4.setText("")
        self.lblSerie_5.setText("")
        self.lblSerie_6.setText("")
        self.lblSerie_7.setText("")
        self.lblSerie_8.setText("")
        self.lblSerie_9.setText("")
        self.lblSerie_10.setText("")

    def createRandomPlot(self, tg):
        x = []
        y = []
        for i in range(100):
            x.append(i*tg)
            y.append(i)
        print("Random Plot\n")
        r = PlotSerie(name='Random', xAxis=x, yAxis=y, color='b')
        return r
        
        pen = pg.mkPen(width = 3)
        self.PlotWidget.setTitle(title="Ultimo Resultado")
        self.PlotWidget.setXRange = i*2*1.1
        self.PlotWidget.setYRange = i*1.1
        self.PlotWidget.enableAutoRange(enable=True)
        self.PlotWidget.plot(x, y, pen=pen)
    
    def AbrirImagem(self):
        ImageName = os.path.join(os.path.dirname(sys.argv[0]), "SistemaComMotor.png")
        image = QtGui.QImage(ImageName)
        if image.isNull():
            self.ImagemSistema.setText("Erro ao abrir imagem")
            return
        self.ImagemSistema.setPixmap(QtGui.QPixmap.fromImage(image))
        self.ImagemSistema.adjustSize()
    
    def setupDialogBaudRate(self, dialogBR):
        dialogBR.setObjectName("dialogCOMPort")
        dialogBR.setWindowModality(QtCore.Qt.WindowModal)
        dialogBR.resize(259, 71)
        dialogBR.verticalLayoutWidget = QtWidgets.QWidget(dialogBR)
        dialogBR.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 258, 71))
        dialogBR.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        dialogBR.verticalLayout = QtWidgets.QVBoxLayout(dialogBR.verticalLayoutWidget)
        dialogBR.verticalLayout.setContentsMargins(0, 0, 0, 0)
        dialogBR.verticalLayout.setObjectName("verticalLayout")
        dialogBR.label = QtWidgets.QLabel(dialogBR.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogBR.label.sizePolicy().hasHeightForWidth())
        dialogBR.label.setSizePolicy(sizePolicy)
        dialogBR.label.setObjectName("label")
        dialogBR.verticalLayout.addWidget(dialogBR.label)
        dialogBR.txtBR = QtWidgets.QLineEdit(dialogBR.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogBR.txtBR.sizePolicy().hasHeightForWidth())
        dialogBR.txtBR.setSizePolicy(sizePolicy)
        dialogBR.txtBR.setReadOnly(False)
        dialogBR.txtBR.setObjectName("txtBR")
        dialogBR.verticalLayout.addWidget(dialogBR.txtBR)
        dialogBR.buttonBox = QtWidgets.QDialogButtonBox(dialogBR.verticalLayoutWidget)
        dialogBR.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        dialogBR.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        dialogBR.buttonBox.setObjectName("buttonBox")
        dialogBR.verticalLayout.addWidget(dialogBR.buttonBox)

        dialogBR.buttonBox.accepted.connect(lambda: self.atualizarBaudRate(dialogBR.txtBR.text()))
        dialogBR.buttonBox.rejected.connect(dialogBR.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogBR)
        _translate = QtCore.QCoreApplication.translate
        dialogBR.setWindowTitle(_translate("dialogBR", "Definir Baud Rate"))
        dialogBR.label.setText(_translate("dialogBR", "Digite o Baud Rate em bps"))
    
    def setupDialogCSVSelect(self, dialogCSVSelect):
        dialogCSVSelect.setObjectName("dialogCSVSelect")
        dialogCSVSelect.setWindowModality(QtCore.Qt.WindowModal)
        dialogCSVSelect.resize(276, 92)
        dialogCSVSelect.verticalLayoutWidget = QtWidgets.QWidget(dialogCSVSelect)
        dialogCSVSelect.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 258, 71))
        dialogCSVSelect.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        dialogCSVSelect.verticalLayout = QtWidgets.QVBoxLayout(dialogCSVSelect.verticalLayoutWidget)
        dialogCSVSelect.verticalLayout.setContentsMargins(0, 0, 0, 0)
        dialogCSVSelect.verticalLayout.setObjectName("verticalLayout")
        dialogCSVSelect.label = QtWidgets.QLabel(dialogCSVSelect.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogCSVSelect.label.sizePolicy().hasHeightForWidth())
        dialogCSVSelect.label.setSizePolicy(sizePolicy)
        dialogCSVSelect.label.setObjectName("label")
        dialogCSVSelect.verticalLayout.addWidget(dialogCSVSelect.label)
        dialogCSVSelect.txtPath = QtWidgets.QLineEdit(dialogCSVSelect.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogCSVSelect.txtPath.sizePolicy().hasHeightForWidth())
        dialogCSVSelect.txtPath.setSizePolicy(sizePolicy)
        dialogCSVSelect.txtPath.setObjectName("txtPath")
        dialogCSVSelect.verticalLayout.addWidget(dialogCSVSelect.txtPath)
        dialogCSVSelect.buttonBox = QtWidgets.QDialogButtonBox(dialogCSVSelect.verticalLayoutWidget)
        dialogCSVSelect.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        dialogCSVSelect.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        dialogCSVSelect.buttonBox.setObjectName("buttonBox")
        dialogCSVSelect.verticalLayout.addWidget(dialogCSVSelect.buttonBox)
        dialogCSVSelect.buttonBox.accepted.connect(lambda: self.importarCSV(dialogCSVSelect.txtPath.text()))
        dialogCSVSelect.buttonBox.rejected.connect(dialogCSVSelect.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogCSVSelect)
        
        _translate = QtCore.QCoreApplication.translate
        dialogCSVSelect.setWindowTitle(_translate("dialogCSVSelect", "Escolher arquivo csv"))
        dialogCSVSelect.label.setText(_translate("dialogCSVSelect", "Digite o caminho do arquivo csv com extensão"))

    def setupDialogCOMPort(self, dialogCOMPort):
        dialogCOMPort.setObjectName("dialogCOMPort")
        dialogCOMPort.setWindowModality(QtCore.Qt.WindowModal)
        dialogCOMPort.resize(259, 71)
        dialogCOMPort.verticalLayoutWidget = QtWidgets.QWidget(dialogCOMPort)
        dialogCOMPort.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 258, 71))
        dialogCOMPort.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        dialogCOMPort.verticalLayout = QtWidgets.QVBoxLayout(dialogCOMPort.verticalLayoutWidget)
        dialogCOMPort.verticalLayout.setContentsMargins(0, 0, 0, 0)
        dialogCOMPort.verticalLayout.setObjectName("verticalLayout")
        dialogCOMPort.label = QtWidgets.QLabel(dialogCOMPort.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogCOMPort.label.sizePolicy().hasHeightForWidth())
        dialogCOMPort.label.setSizePolicy(sizePolicy)
        dialogCOMPort.label.setObjectName("label")
        dialogCOMPort.verticalLayout.addWidget(dialogCOMPort.label)
        dialogCOMPort.txtCOMPort = QtWidgets.QLineEdit(dialogCOMPort.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogCOMPort.txtCOMPort.sizePolicy().hasHeightForWidth())
        dialogCOMPort.txtCOMPort.setSizePolicy(sizePolicy)
        dialogCOMPort.txtCOMPort.setReadOnly(False)
        dialogCOMPort.txtCOMPort.setObjectName("txtCOMPort")
        dialogCOMPort.verticalLayout.addWidget(dialogCOMPort.txtCOMPort)
        dialogCOMPort.buttonBox = QtWidgets.QDialogButtonBox(dialogCOMPort.verticalLayoutWidget)
        dialogCOMPort.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        dialogCOMPort.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        dialogCOMPort.buttonBox.setObjectName("buttonBox")
        dialogCOMPort.verticalLayout.addWidget(dialogCOMPort.buttonBox)

        _translate = QtCore.QCoreApplication.translate
        dialogCOMPort.setWindowTitle(_translate("dialogCOMPort", "Definir COM Port"))
        dialogCOMPort.label.setText(_translate("dialogCOMPort", "Digite o nome da porta serial conectada ao arduino"))
        
        dialogCOMPort.buttonBox.accepted.connect(lambda: self.atualizarCOMPort(dialogCOMPort.txtCOMPort.text()))
        dialogCOMPort.buttonBox.rejected.connect(dialogCOMPort.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogCOMPort)
    
    def atualizarCOMPort(self, port):
        self.comPort = port
        print("Porta modificada para {0}".format(port))
        self.dlgCOMPort.accept()
    
    def atualizarBaudRate(self, BR):
        if BR.isnumeric():
            self.baudRate = BR
            print("Baud Rate modificado para {0}".format(BR))
            self.dlgBaudRate.accept()
    
    def importarCSV(self, path):
        try:
            csv = open(path)
            print("Arquivo aberto com sucesso!")
            x = []
            y = []
            for line in csv:
                aux = line.replace(" ", "").split(",")
                x.append(float(aux[0]))
                if len(aux) == 3:
                    y.append(float((aux[1] + "." + aux[2])))
                if len(aux) == 2:
                    y.append(float(aux[1]))
            #ALTERAR PARA PERMITIR USUARIO NOMEAR
            r = PlotSerie(name = "arquivoCSV", xAxis = x, yAxis = y, color = 'w')
            self.ListPlots.append(r)
            print("Incluida a serie CSV na lista de Plots")
            self.updatePlotList()
            csv.close()
            self.dlgCSVSelect.accept()
        except:
            print("Problema na abertura do arquivo, verifique se o caminho esta correto.")