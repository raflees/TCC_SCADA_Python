from PyQt5 import QtWidgets, QtCore, QtGui, QtChart
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import numpy as np
import pprint

listSeries = []
plottedSeries = []
unplottedSeries = []
nSeries = 0

class GraphicPlotConfig(QtWidgets.QWidget):
	series = []
	time_axis = []

	def __init__(self, plot_object,
				plot_list_layout=None,
				parent=None,
				series=None,
				time_axis=None,
				description=''):
		super().__init__(parent)
		self.series = series
		self.time_axis = time_axis
		self.description = description
		self.plot_object = plot_object
		self.plot_list_layout = plot_list_layout
		self.plotted = False

		# Objetos filhos principais
		self.chart_object = SimpleChartObject(series=self.series)
		self.button_plot = QtWidgets.QPushButton(text='Plot')
		self.button_edit = QtWidgets.QPushButton(text='Edit')
		self.button_delete = QtWidgets.QPushButton(text='Delete')
		self.label = QtWidgets.QLabel(self.description)

		# Definicoes dos eventos
		self.button_plot.clicked.connect(self.togglePlot)
		self.button_delete.clicked.connect(self.delete)
		self.button_edit.clicked.connect(self.edit)

		# Layout dos botoes
		layout_buttons = QtWidgets.QHBoxLayout()
		layout_buttons.addWidget(self.button_plot)
		layout_buttons.addWidget(self.button_edit)
		layout_buttons.addWidget(self.button_delete)

		# Ajuste do layout na parte esquerda do objeto grafico
		layout_left = QtWidgets.QVBoxLayout()
		layout_left.addWidget(self.label)
		layout_left.addLayout(layout_buttons)

		# Finalizacao do layout completo do objeto grafico
		layout = QtWidgets.QHBoxLayout()
		layout.addLayout(layout_left)
		layout.addWidget(self.chart_object)

		listSeries.append(self.series)
		unplottedSeries.append(self.series)
		global nSeries
		nSeries += 1

		self.setLayout(layout)
		self.setFixedHeight(120)
		return

	def plot(self):
		ax = self.plot_object.figure.gca()
		for serie in self.series:
			ax.plot(serie)
		self.plot_object.canvas.draw()
		self.plotted = not self.plotted
		self.repaint()
		return

	def togglePlot(self):
		global unplottedSeries
		global plottedSeries
		if self.plotted:
			print('Unploting...')
			plottedSeries.remove(self.series)
			unplottedSeries.append(self.series)
		else:
			print('Plotting...')
			unplottedSeries.remove(self.series)
			plottedSeries.append(self.series)
		self.plotted = not self.plotted
		self.plot_object.update_plot()
		self.repaint()

	def edit(self):
		return

	def delete(self):
		self.plot_list_layout.removeWidget(self)
		listSeries.remove(self.series)
		if self.series in plottedSeries:
			plottedSeries.remove(self.series)
			self.plot_object.update_plot()
		if self.series in unplottedSeries:
			unplottedSeries.remove(self.series)
		self.hide()
		del self
		return

	def paintEvent(self, event):
		painter = QtGui.QPainter()
		painter.begin(self)
		self.paint(painter, event.rect())
		painter.end()
		return

	def paint(self, painter, area):
		painter.setPen(QtGui.QColor(0,0,0,0))
		if self.plotted:
			painter.setBrush(QtGui.QColor(0,255,0,127))
		else:
			painter.setBrush(QtGui.QColor(255,0,0,127))
		painter.drawRect(area)


class SimpleChartObject(QtWidgets.QWidget):
	def __init__(self, parent=None, series=None, time_axis=None):
		super().__init__(parent)
		self._figure = plt.Figure(figsize=(1,1), frameon=False)
		self._canvas = FigureCanvas(self._figure)
		self.series = series
		self.time_axis = time_axis

		# Incluindo FigureCanvas num layout, para centraliza-lo em seu espaco
		layout = QtWidgets.QHBoxLayout()
		layout.addWidget(self._canvas)
		self.setLayout(layout)

		# Criando um axisartist para remover marcas e número nos eixos do grafico
		ax = axisartist.Subplot(self._figure, 111)
		self._figure.add_subplot(ax)
		ax.set_yticks([])
		ax.set_xticks([])

		# Tratando series iniciadas como None
		if not self.series:
			self._figure.clear()
			return
		# Plotando cada serie
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
		self.layout.setAlignment(QtCore.Qt.AlignTop)

		self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.setWidgetResizable(True)
		self.setWidget(self.widget)
		self.setMinimumWidth(400)
		self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)

		self.widget.setLayout(self.layout)
		return

	def add(self, series=None, time_axis=None, description='', plot_object=None):
		
		return

	def paintEvent(self, event):
		painter = QtGui.QPainter()
		painter.begin(self)
		self.paint(painter, event.rect())
		painter.end()
		return

	def paint(self, painter, area):
		painter.setBrush(QtGui.QColor(0, 127, 127, 127))
		painter.drawRect(area)
		return


class PlotManager(QtWidgets.QWidget):
	def __init__(self, plot_object, parent=None):
		super().__init__(parent)
		self.plot_list = GraphicPlotList()
		self.plot_object = plot_object

		add_series_button = QtWidgets.QPushButton('Add Series')
		add_series_button.setFixedWidth(100)
		add_series_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		add_series_button.clicked.connect(self.create_series_object)

		layout_bottom = QtWidgets.QHBoxLayout()
		layout_bottom.setAlignment(QtCore.Qt.AlignLeft)
		layout_bottom.addWidget(add_series_button)

		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(self.plot_list)
		layout.addLayout(layout_bottom)

		self.setLayout(layout)
		return

	def create_series_object(self):
		series = []
		global nSeries
		quantidade_series = int(np.random.rand()*4) + 1
		for j in range(quantidade_series):
			tg = np.random.rand()*3
			serie = [k*tg for k in range(100)]
			series.append(serie)
		n = nSeries + 1
		new_widget = GraphicPlotConfig(series=series, description='Serie ' + str(n),
								plot_object=self.plot_object, plot_list_layout=self.plot_list.layout)
		self.plot_list.layout.addWidget(new_widget)
		return

class MainPlotArea(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.figure = plt.Figure()
		self.canvas = FigureCanvas(self.figure)

		ax = self.figure.gca()
		ax.set_xlim([0, 1])
		ax.set_ylim([0, 1])

		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(QtWidgets.QLabel('Awesome Graph'))
		layout.addWidget(self.canvas)
		self.setLayout(layout)
		self.setMinimumWidth(400)
		self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

	def update_plot(self):
		self.figure.clear()
		ax = self.figure.gca()
		global plottedSeries
		# print('Updating plot ({} series to plot)'.format(len(plottedSeries)))
		for series in plottedSeries:
			for serie in series:
				ax.plot(serie)
		self.canvas.draw()
		return

class MainWidget(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)

		nSeries = 0

		main_plot_area = MainPlotArea()

		layout = QtWidgets.QHBoxLayout()
		layout.addWidget(main_plot_area)
		layout.addWidget(PlotManager(main_plot_area))

		self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		self.setMinimumSize(QtCore.QSize(850,400))

		self.setLayout(layout)
