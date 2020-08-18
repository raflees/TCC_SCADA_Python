from PyQt5 import QtWidgets, QtCore, QtGui, QtChart
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import numpy as np
import pprint

listSeries = []

class GraphicPlotConfig(QtWidgets.QWidget):
	series = []
	time_axis = []

	def __init__(self, parent=None, series=None, time_axis=None, description=''):
		super().__init__(parent)
		self.series = series
		self.time_axis = time_axis
		self.description = description

		# Objetos filhos principais
		self.chart_object = SimpleChartObject(series=self.series)
		self.button_plot = ToggleColorButton(text='Plot')
		self.button_edit = ToggleColorButton(text='Edit')
		self.button_delete = ToggleColorButton(text='Delete')

		# Layout dos botoes
		layout_buttons = QtWidgets.QHBoxLayout()
		layout_buttons.addWidget(self.button_plot)
		layout_buttons.addWidget(self.button_edit)
		layout_buttons.addWidget(self.button_delete)

		# Rotulo de nome
		self.label = QtWidgets.QLabel(self.description)
		#self.label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		# Ajuste do layout na parte esquerda do objeto grafico
		layout_left = QtWidgets.QVBoxLayout()
		layout_left.addWidget(self.label)
		layout_left.addLayout(layout_buttons)

		# Finalizacao do layout completo do objeto grafico
		layout = QtWidgets.QHBoxLayout()
		layout.addLayout(layout_left)
		layout.addWidget(self.chart_object)

		self.setLayout(layout)
		self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		self.setMinimumSize(QtCore.QSize(400,100))

class ToggleColorButton(QtWidgets.QPushButton):
	def __init__(self, parent=None, text='Button', color_on=None, color_off=None):
		super().__init__(parent)
		self.color_on = color_on if color_on else QtGui.QColor(127, 127, 127)
		self.color_off = color_off if color_off else QtGui.QColor(127, 127, 127)

		self.setText(text)

class SimpleChartObject(QtWidgets.QWidget):
	def __init__(self, parent=None, series=None, time_axis=None):
		super().__init__(parent)
		self._figure = plt.Figure(figsize=(1,1), frameon=False)
		self._canvas = FigureCanvas(self._figure)
		#self.series = series if series else [[i for i in range(100)], [i*1.5 for i in range(100)]]
		self.series = series
		self.time_axis = time_axis

		layout = QtWidgets.QHBoxLayout()
		layout.addWidget(self._canvas)

		self.setLayout(layout)

		self.plot()
		return

	def plot(self):
		if not self.series:
			self._figure.clear()
			return

		ax = axisartist.Subplot(self._figure, 111)
		self._figure.add_subplot(ax)
		ax.set_yticks([])
		ax.set_xticks([])
		for serie in self.series:
			if self.time_axis:
				ax.plot(serie, self.time_axis)
			else:
				ax.plot(serie)
		self._canvas.draw()
		return

class GraphicPlotList(QtWidgets.QScrollArea):
	def __init__(self, parent=None):
		super().__init__(parent)
		#self.plot_list = []
		self.widget = QtWidgets.QWidget()
		self.layout = QtWidgets.QVBoxLayout()

		self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.setWidgetResizable(True)
		self.setWidget(self.widget)

		self.widget.setLayout(self.layout)
		return

	def add(self, series=None, time_axis=None, description=''):
		self.layout.addWidget(GraphicPlotConfig(series=series, time_axis=time_axis, description=description))
		print('Tentando incluir item novo')
		return


class PlotManager(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.plot_list = GraphicPlotList()

		add_series_button = QtWidgets.QPushButton('Add Series')
		add_series_button.setFixedWidth(100)
		add_series_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		add_series_button.clicked.connect(self.create_series_object)

		layout_bottom = QtWidgets.QHBoxLayout()
		layout_bottom.setAlignment(QtCore.Qt.AlignLeft)
		layout_bottom.addWidget(add_series_button)
		#layout_bottom.addItem(spacer)

		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(GraphicPlotList())
		layout.addLayout(layout_bottom)

		self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		self.setMinimumSize(QtCore.QSize(400,100))

		self.setLayout(layout)
		return

	def create_series_object(self):
		series = []
		nSeries = int(np.random.rand()*4) + 1
		for j in range(nSeries):
			tg = np.random.rand()*3
			serie = [k*tg for k in range(100)]
			series.append(serie)
		n = len(listSeries)
		self.plot_list.add(series=series, description='Serie '+str(n))
		return

class MainPlotArea(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self._figure = plt.Figure()
		self._canvas = FigureCanvas(self._figure)


		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(QtWidgets.QLabel('Awesome Graph'))
		layout.addWidget(self._canvas)
		self.setLayout(layout)

class MainWidget(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)

		layout = QtWidgets.QHBoxLayout()
		layout.addWidget(MainPlotArea())
		layout.addWidget(PlotManager())

		self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		self.setMinimumSize(QtCore.QSize(400,100))

		self.setLayout(layout)
