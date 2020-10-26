from .realtime_objects import *

from PyQt5 import QtWidgets, QtCore, QtGui, QtChart
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import numpy as np
import serial
import control

#libs padroes
import time
import os
from pprint import pprint

listSeries = []
plottedSeries = []
unplottedSeries = []
nSeries = 0

class ModalSeriesDialog(QtWidgets.QDialog):
	last_header = -1
	def __init__(self, parent=None, series_obj=None, source='Dummy', series_name='Nova Serie', mode=0):
		super().__init__(parent)

		self.series_obj = series_obj

		self.datatable = QtWidgets.QTableWidget(len(series_obj.series[0]), len(series_obj.series))
		lbl_series_name = QtWidgets.QLabel('Nome da Série: ')
		self.edit_series_name = QtWidgets.QLineEdit(series_name)
		lbl_source = QtWidgets.QLabel('Source: ' + source)
		self.edit_header = QtWidgets.QLineEdit()
		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		self.btn_cancel = QtWidgets.QPushButton('Cancelar')
		self.btn_apply = QtWidgets.QPushButton('Aplicar')
		if mode == 0:
			self.btn_ok = QtWidgets.QPushButton('Criar Série')
		else:
			self.btn_ok = QtWidgets.QPushButton('Salvar Alterações')
		self.edit_series_name.setMaximumWidth(300)
		self.datatable.setMinimumWidth(300)

		self.datatable.cellChanged.connect(self.edit_value)
		self.datatable.itemSelectionChanged.connect(self.copy_header)
		self.edit_header.returnPressed.connect(lambda: self.edit_header_func(self.edit_header.text()))
		self.btn_apply.clicked.connect(self.update_plot)
		self.btn_cancel.clicked.connect(self.close)
		self.btn_ok.clicked.connect(self.accept)

		layout_series_name = QtWidgets.QHBoxLayout()
		layout_series_name.addWidget(lbl_series_name)
		layout_series_name.addWidget(self.edit_series_name)

		layout_left = QtWidgets.QVBoxLayout()
		layout_left.addLayout(layout_series_name)
		layout_left.addWidget(lbl_source)
		layout_left.addSpacing(20)
		layout_left.addWidget(self.edit_header)
		layout_left.addSpacing(2)
		layout_left.addWidget(self.datatable)

		layout_buttons = QtWidgets.QHBoxLayout()
		layout_buttons.addWidget(self.btn_apply)
		layout_buttons.addWidget(self.btn_cancel)
		layout_buttons.addWidget(self.btn_ok)
		layout_buttons.setAlignment(QtCore.Qt.AlignRight)

		layout_upper = QtWidgets.QHBoxLayout()
		layout_upper.addLayout(layout_left)
		layout_upper.addWidget(self.canvas)

		layout = QtWidgets.QVBoxLayout()
		layout.addLayout(layout_upper)
		layout.addLayout(layout_buttons)

		self.setFixedWidth(650)
		self.setFixedHeight(400)
		self.setLayout(layout)
		self.populate_datatable()
		self.update_plot()
		return

	def copy_header(self):
		c = self.datatable.currentColumn()
		if c < 0:
			self.edit_header.setText('')
		else:
			self.edit_header.setText(self.datatable.horizontalHeaderItem(c).text())
		self.last_header = c
		return

	def edit_header_func(self, value):
		if self.last_header < 0: return

		self.datatable.setHorizontalHeaderItem(self.last_header, QtWidgets.QTableWidgetItem(value))
		self.series_obj.series_names[self.last_header] = value
		return

	def edit_value(self, row, col):
		value = float(self.datatable.item(row, col).text())
		self.series_obj.series[col][row] = value
		return

	def populate_datatable(self):
		for i, name in enumerate(self.series_obj.series_names):
			try:
				self.datatable.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(name))
			except:
				self.datatable.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem('Serie '+str(i+1)))
		label = []
		for time in self.series_obj.time_axis:
			label.append('{0:.1f}'.format(time))
		self.datatable.setVerticalHeaderLabels(label)

		for i, serie in enumerate(self.series_obj.series):
			for j, data in enumerate(serie):
				self.datatable.setItem(j, i, QtWidgets.QTableWidgetItem('{:0.4f}'.format(data)))
		#self.datatable.horizontalHeader().setStretchLastSection(True)
		self.datatable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
		return

	def update_plot(self):
		self.figure.clear()
		ax = self.figure.gca()
		for serie in self.series_obj.series:
			ax.plot(self.series_obj.time_axis, serie)
		ax.legend(self.series_obj.series_names)
		self.canvas.draw()

class ScriptEditorDialog(QtWidgets.QDialog):
	def __init__(self, parent=None, text=''):
		super().__init__()
		self.text_editor = QtWidgets.QTextEdit(text)
		self.btn_model_1 = QtWidgets.QPushButton('Modelo')
		self.btn_control = QtWidgets.QPushButton('T. Func')
		self.btn_ok = QtWidgets.QPushButton('OK')
		self.btn_cancel = QtWidgets.QPushButton('Cancelar')

		self.btn_ok.clicked.connect(self.accept)
		self.btn_cancel.clicked.connect(self.close)
		self.btn_model_1.clicked.connect(self.write_model)
		self.btn_control.clicked.connect(self.write_control)

		self.btn_model_1.setFixedWidth(80)
		self.btn_control.setFixedWidth(80)

		layout_models = QtWidgets.QHBoxLayout()
		layout_models.addWidget(self.btn_model_1)
		layout_models.addWidget(self.btn_control)
		layout_models.setAlignment(QtCore.Qt.AlignLeft)

		layout_buttons = QtWidgets.QHBoxLayout()
		layout_buttons.addWidget(self.btn_ok)
		layout_buttons.addWidget(self.btn_cancel)
		layout_buttons.setAlignment(QtCore.Qt.AlignRight)

		layout = QtWidgets.QVBoxLayout()
		layout.addLayout(layout_models)
		layout.addWidget(self.text_editor)
		layout.addLayout(layout_buttons)

		self.setLayout(layout)
		self.setWindowTitle('Editor de Python')
		self.resize(400, 400)
		return

	def write_model(self):
		text = 'import math \n\nt = range(100) \
		\nseries = [[math.sin(i/10) for i in t], [math.cos(i/10) for i in t]] \
		\nheader = ["seno", "cosseno"] \nreturn series, t, header\n'

		self.text_editor.setPlainText(text)
		return

	def write_control(self):
		text = 'import control \n\nsys1 = control.tf([2,], [1, 0.1, 1]) \
			\nsys2 = control.tf([1,], [1, 2]) \nsys = control.series(sys1, sys2) \
			\nt = range(100) \nt, u = control.step_response(control.tf([1,],[10,1]), t) \
			\nt, y, x = control.forced_response(sys, t, u) \
			\nh = ["u(t)", "y(t)"] \nreturn [u, y], t, h'

		self.text_editor.setPlainText(text)
		return


class GraphicPlotConfig(QtWidgets.QWidget):
	series = []
	time_axis = []

	def __init__(self, plot_object, series_obj,
				plot_list_layout=None,
				parent=None,
				description='',
				source='Dummy'):
		super().__init__(parent)
		self.series_obj = series_obj
		self.description = description
		self.plot_object = plot_object
		self.plot_list_layout = plot_list_layout
		self.source = source
		self.plotted = False

		# Objetos filhos principais
		self.chart_object = SimpleChartObject(parent=self, series=self.series_obj.series,
											time_axis=series_obj.time_axis)
		self.button_plot = QtWidgets.QPushButton(text='Plot')
		self.button_edit = QtWidgets.QPushButton(text='Edit')
		self.button_delete = QtWidgets.QPushButton(text='Delete')
		self.lbl_title = QtWidgets.QLabel('<big><b>'+self.description+'</b></big>')

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
		layout_left.addWidget(self.lbl_title)
		layout_left.addWidget(QtWidgets.QLabel(source))
		layout_left.addSpacerItem(QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
		layout_left.addLayout(layout_buttons)

		# Finalizacao do layout completo do objeto grafico
		layout = QtWidgets.QHBoxLayout()
		layout.addLayout(layout_left)
		layout.addWidget(self.chart_object)

		listSeries.append(self.series_obj)
		unplottedSeries.append(self.series_obj)
		global nSeries
		nSeries += 1

		self.setLayout(layout)
		self.setFixedHeight(120)
		return

	def togglePlot(self):
		global unplottedSeries
		global plottedSeries
		if self.plotted:
			#print('Unploting...')
			plottedSeries.remove(self.series_obj)
			unplottedSeries.append(self.series_obj)
		else:
			#print('Plotting...')
			unplottedSeries.remove(self.series_obj)
			plottedSeries.append(self.series_obj)
		self.plotted = not self.plotted
		self.plot_object.update_plot()
		self.repaint()

	def edit(self):
		dialog = ModalSeriesDialog(series_obj=self.series_obj, source=self.source,
									series_name=self.description, mode=1)
		if dialog.exec_():
			if self.plotted:
				plottedSeries.remove(self.series_obj)
			else:
				unplottedSeries.remove(self.series_obj)

			if not dialog.edit_series_name.text().strip() == '':
				self.description = dialog.edit_series_name.text()
			self.series_obj = dialog.series_obj

			if self.plotted:
				plottedSeries.append(self.series_obj)
			else:
				unplottedSeries.append(self.series_obj)
			
			self.lbl_title.setText('<b>' + self.description + '</b>')
			self.chart_object.update_plot()
			self.plot_object.update_plot()
		return

	def delete(self):
		self.plot_list_layout.layout.removeWidget(self)
		listSeries.remove(self.series_obj)
		if self.series_obj in plottedSeries:
			plottedSeries.remove(self.series_obj)
			self.plot_object.update_plot()
		if self.series_obj in unplottedSeries:
			unplottedSeries.remove(self.series_obj)
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

		self.update_plot()
		return

	def update_plot(self):
		# Criando um axisartist para remover marcas e número nos eixos do grafico
		ax = axisartist.Subplot(self._figure, 111)
		self._figure.add_subplot(ax)
		ax.set_yticks([])
		ax.set_xticks([])

		# Tratando series iniciadas como None
		if self.series is None:
			self._figure.clear()
			return

		# Plotando cada serie
		ax = self._figure.gca()
		for serie in self.series:
			if not self.time_axis is None:
				ax.plot(self.time_axis, serie)
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


class SeriesObject():
	sys = control.tf([1,], [1,])
	tfs=[]

	def __init__(self, tfs=[], series=[], series_names=[], time_axis=[]):
		self.tfs = tfs
		self.series = series
		self.series_names = series_names
		self.time_axis = time_axis

		if len(series) == 0 and len(tfs) > 0:
			for tf in tfs:
				self.sys = control.append(self.sys, control.tf(tf[0], tf[1]))
			t, response = control.step_response(self.sys)
			self.time_axis = t
			self.series.append(response)
		return


class PlotManager(QtWidgets.QWidget):
	def __init__(self, plot_object, parent=None):
		super().__init__(parent)
		self.plot_list = GraphicPlotList(self)
		self.plot_object = plot_object

		add_series_button = QtWidgets.QPushButton('Add Dummy Series')
		add_series_button.setFixedWidth(150)
		add_series_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

		add_series_button.clicked.connect(self.dummy_series_dialog)

		layout_bottom = QtWidgets.QHBoxLayout()
		layout_bottom.setAlignment(QtCore.Qt.AlignLeft)
		layout_bottom.addWidget(add_series_button)

		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(self.plot_list)
		layout.addLayout(layout_bottom)

		self.setLayout(layout)
		return

	def dummy_series_dialog(self):
		series_obj = self.create_dummy_series_object()
		dialog = ModalSeriesDialog(series_obj=series_obj)
		if dialog.exec_():
			if dialog.edit_series_name.text().strip() == '':
				global nSeries
				description = 'Plot Series #' + str(nSeries + 1)
			else:
				description = dialog.edit_series_name.text()
			series_obj = dialog.series_obj
			new_serie = GraphicPlotConfig(plot_object=self.plot_object, series_obj=series_obj,
					plot_list_layout=self.plot_list, description=description)
			self.add(new_serie)
		return

	def add(self, new_serie):
		self.plot_list.layout.addWidget(new_serie)

	def create_dummy_series_object(self):
		global nSeries
		series = []
		quantidade_series = int(np.random.rand()*4) + 1
		for j in range(quantidade_series):
			tg = np.random.rand()*3
			serie = [k*tg for k in range(100)]
			series.append(serie)
		n = nSeries + 1
		names = ['Serie '+str(i+1) for i in range(quantidade_series)]
		series_obj = SeriesObject(series=series, time_axis=range(100), series_names=names)

		return series_obj

class MainPlotArea(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.figure = plt.Figure()
		self.canvas = FigureCanvas(self.figure)
		self.toolbar = NavigationToolbar2QT(self.canvas, self)

		ax = self.figure.gca()
		ax.set_xlim([0, 1])
		ax.set_ylim([0, 1])

		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(self.canvas)
		layout.addWidget(self.toolbar)
		layout.setAlignment(QtCore.Qt.AlignRight)
		
		self.setLayout(layout)
		self.setMinimumWidth(400)
		self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

	def update_plot(self):
		self.figure.clear()
		ax = self.figure.gca()
		global plottedSeries
		legends = []
		for series_obj in plottedSeries:
			legends += series_obj.series_names
			for leg, serie in enumerate(series_obj.series):
				ax.plot(serie)
		ax.legend(legends)
		self.canvas.draw()
		return

class DatasetConfig(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ds_layout_config = DatasetLayoutConfig(parent=self) 
		self.series_source_config = SeriesSourceConfig(parent=self)

		self.ds_layout_config.btn_go.clicked.connect(self.import_series)

		layout = QtWidgets.QHBoxLayout()
		layout.addWidget(self.series_source_config)
		layout.addWidget(self.ds_layout_config)
		layout.addSpacerItem(QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
		layout.setAlignment(QtCore.Qt.AlignLeft)

		self.setLayout(layout)

	def import_series(self):
		series_obj = None
		obj = self.series_source_config
		use_header = self.ds_layout_config.chkbox_headers.isChecked()
		use_1st_col = self.ds_layout_config.chkbox_first_col.isChecked()
		
		# FUNCAO DE TRANSFERENCIA
		if obj.currentIndex() == 0:
			source = 'transfer function'
			if obj.tf_tab.edit_k.text() == '':
				gain = 1
			else:
				try: gain = float(obj.tf_tab.edit_k.text())
				except: gain = 1

			if obj.tf_tab.edit_x0.text() == '':
				x0 = 1
			else:
				try: x0 = float(obj.tf_tab.edit_x0.text())
				except: x0 = 1
			if obj.tf_tab.list_tf.count() == 0:
				return
			series_obj = self.import_series_tf(obj.tf_tab.list_tf, gain, x0)

		# TRANFERENCIA POR ARQUIVO
		elif obj.currentIndex() == 1:
			file_extension = obj.file_config_tab
			path = os.path.join(file_extension.edit_directory.text(), file_extension.edit_file.text())
			
			try:
				with open(path, 'r'):
					pass
			except:
				print('Não foi possivel abrir o arquivo em {}. Ou ele não existe ou já se encontra aberto'.format(path)) 
				return

			if file_extension.btn_tsv.isChecked():
				source = '.tsv file'
				series_obj = self.import_series_tsv(path, use_header, use_1st_col)
			elif file_extension.btn_csv.isChecked():
				source = '.csv file'
				series_obj = self.import_series_csv(path, use_header, use_1st_col)
			elif file_extension.btn_xls.isChecked():
				source = '.xls file'
				series_obj = self.import_series_xls(path, use_header, use_1st_col)
			elif file_extension.btn_xlsx.isChecked():
				source = '.xlsx file'
				series_obj = self.import_series_xlsx(path, use_header, use_1st_col)
			else:
				series_obj = None

		# PORTA SERIAL
		elif obj.currentIndex() == 2:
			source = 'dummy serial'
			series_obj = self.import_series_serial()

		# SCRIPT PYTHON
		elif obj.currentIndex() == 3:
			source = 'python script'
			series_obj = self.import_series_script()

		if series_obj is None:
			print('Erro na importação')
			return

		name = self.ds_layout_config.edit_name_serie.text()
		dialog = ModalSeriesDialog(series_obj=series_obj, source=source, series_name=name)
		
		if dialog.exec_():
			if dialog.edit_series_name.text().strip() == '':
				global nSeries
				description = 'Plot Series #' + str(nSeries+1)
			else:
				description = dialog.edit_series_name.text()
			new_serie = GraphicPlotConfig(plot_object=self.parent().main_plot_area,
				series_obj=dialog.series_obj, plot_list_layout=self.parent().plot_manager.plot_list,
				source=source, description=description)
			self.parent().plot_manager.add(new_serie)
		return

	def import_series_csv(self, path, use_header, use_1st_col):
		import csv
		with open(path) as f:
			series_t = []
			headers = []
			reader = csv.reader(f)
			n_lines = 0
			for line in reader:
				serie_t = []
				if (n_lines == 0) and use_header:
					for elem in line:
						headers.append(elem)
				else:
					#print(line)
					for elem in line:
						try:
							serie_t.append(float(elem))
						except:
							serie_t.append(np.nan)
					series_t.append(serie_t)
				n_lines += 1

		series = np.array(series_t).transpose()
		if use_1st_col:
			time_serie = series[0]
			series = series[1:]
			headers = headers[1:]
		else:
			time_serie = [i for i in range(len(series[0]))]

		for i in range(len(headers), len(series)):
			headers.append('Serie ' + str(i+1))

		series_obj = SeriesObject(series=series, series_names=headers, time_axis=time_serie)
		return series_obj

	def import_series_tsv(self, path, use_header, use_1st_col):
		with open(path, 'r') as f:
			series = []
			headers = []
			n = 0
			for line in f.readlines():
				serie = []
				if (n == 0) and use_header:
					for elem in line.split('\t'):
						headers.append(elem)
				else:
					for elem in line.split('\t'):
						try:
							serie.append(float(elem))
						except:
							serie.append(np.nan)
					series.append(serie)
				n += 1

		series = np.array(series).transpose()

		if use_1st_col:
			time_serie = series[0]
			series = series[1:]
			headers = headers[1:]
		else:
			time_serie = [i for i in range(len(series[0]))]

		for i in range(len(headers), len(series)):
			headers.append('Serie ' + str(i+1))

		pprint(headers)
		pprint(series)
		pprint(time_serie)

		series_obj = SeriesObject(series=series, series_names=headers, time_axis=time_serie)
		return series_obj


	def import_series_xls(self, path, use_header, use_1st_col):
		import xlrd

		workbook = xlrd.open_workbook(filename=path)
		worksheet = workbook.sheet_by_index(0)
		series = []
		headers = []
		
		for c in range(worksheet.ncols):
			serie = []
			for r in range(worksheet.nrows):
				if r == 0 and use_header:
					headers.append(worksheet.cell(r, c).value)
				else:
					try:
						serie.append(float(worksheet.cell(r, c).value))
					except:
						serie.append(np.nan)
			series.append(serie)
		
		if use_1st_col:
			time_serie = series[0]
			series = series[1:]
			headers = headers[1:]
		else:
			time_serie = [i for i in range(len(series[0]))]

		for i in range(len(headers), len(series)):
			headers.append('Serie ' + str(i+1))

		series_obj = SeriesObject(series=series, series_names=headers, time_axis=time_serie)
		return series_obj

	def import_series_xlsx(self, path, use_header, use_1st_col):
		import pandas

		if use_header:
			dataframe = pandas.read_excel(path, sheet_name=0, header=0)
			headers = [col for col in dataframe.columns]
		else:
			dataframe = pandas.read_excel(path, sheet_name=0, header=None)
			headers = ['Serie '+str(i+1) for i in range(len(dataframe.columns))]

		series = []
		for col in dataframe:
			serie = []
			for value in dataframe[col]:
				try:
					serie.append(float(value))
				except:
					serie.append(np.nan)
			series.append(serie)
		#pprint(headers)
		if use_1st_col:
			time_serie = series[0]
			series = series[1:]
			headers = headers[1:]
		else:
			time_serie = [i for i in range(len(series[0]))]

		if len(series) < 1:
			print('Arquivo importado vazio ou com uma coluna somente')
			return None

		if headers == []:
			headers = ['Serie '+str(i+1) for i in range(len(series))]

		series_obj = SeriesObject(series=series, series_names=headers, time_axis=time_serie)
		return series_obj

	def import_series_serial(self):
		#porta = 
		#baud_rate = 
		#timeout = 
		dialogSCADA = SCADADialog(3)
		if dialogSCADA.exec_():
			series = dialogSCADA.series
			time_serie = dialogSCADA.time_serie
			headers = ['Serie '+str(i+1) for i in range(len(series))]
			series_obj = SeriesObject(series=series, series_names=headers, time_axis=time_serie)
			return series_obj
		else:
			dialogSCADA.update = False
			dialogSCADA.fetch = False
			return None

	def import_series_script(self):
		import pickle

		script = self.series_source_config.python_script_tab.edit_script.toPlainText()
		file = 'script.py'

		try:
			open(file, 'x')
		except:
			pass
		with open(file, 'w') as f:
			f.write('def func(): \n')
			lines = script.split('\n')
			for line in lines:
				f.write('\t' + line + '\n')
			f.write('\n\nobj = func() \n')
			f.write('import pickle \ntry: \n\topen("returned_obj", "x") \nexcept: \n\tpass')
			f.write("\nwith open('returned_obj', 'wb') as f: \n\tpickle.dump(obj, f) \n\tf.close() \nexit(0)")
		
		try:
			os.system('python ' + file)
		except:
			print('Erro no script')
			return None

		try:
			with open('returned_obj', 'rb') as f:
				obj = pickle.load(f)
		except:
			return None

		try:
			series = obj[0]
		except:
			print('Verifique seu script python!')
			return None
		try:
			time_serie = obj[1]
			if time_serie is None: raise Exception
		except:
			time_serie = range(len(series[0]))
		try:
			headers = obj[2]
			if headers is None: raise Exception
		except:
			headers = ['Serie '+str(i+1) for i in range(len(series))]

		series_obj = SeriesObject(series=series, series_names=headers, time_axis=time_serie)
		return series_obj

	def import_series_tf(self, list_tf, gain=1, x0=0):
		if list_tf.count == 0: return None

		tfs = []
		for i in range(list_tf.count()):
			item = list_tf.item(i)
			nums = []
			dens = []
			text = item.text()
			text = text.replace('[', '')
			text = text.replace(']', '')
			split = text.split('\t')

			for n in split[0].split(' '):
				nums.append(float(n))
			for n in split[1].split(' '):
				dens.append(float(n))

			#pprint(nums)
			#pprint(dens)

			tfs.append(control.tf(nums, dens))

		sys = control.series(control.tf([1,], [1,]), tfs[0])
		if len(tfs) > 1:
			for tf in tfs[1:]:
				sys = control.series(sys, tf)
		time_serie, y = control.step_response(sys, None, X0=x0)
		headers = ['u(t)', 'y(t)']
		u = [gain if i>0 else 0 for i in range(len(y))]
		y = [gain*i for i in y]
		series = [u, y]

		series_obj = SeriesObject(series=series, series_names=headers, time_axis=time_serie)
		return series_obj



class DatasetLayoutConfig(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.edit_name_serie = QtWidgets.QLineEdit()
		self.edit_ncol = QtWidgets.QLineEdit()
		self.edit_time_col = QtWidgets.QLineEdit()
		self.chkbox_headers = QtWidgets.QCheckBox('Considerar cabeçalho')
		self.chkbox_first_col = QtWidgets.QRadioButton('1ª coluna como eixo de tempo')
		self.chkbox_time_serie = QtWidgets.QRadioButton('Gerar eixo de tempo autom.')
		self.btn_go = QtWidgets.QPushButton('Puxar Dados')
		self.lbl_time_col = QtWidgets.QLabel(' Posição coluna tempo (>0)')
		self.lbl_ncol = QtWidgets.QLabel(' Nº de Colunas')
		lbl_name_serie = QtWidgets.QLabel('Nome da nova série')

		self.edit_ncol.setMaximumWidth(30)
		self.edit_time_col.setMaximumWidth(30)

		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(lbl_name_serie)
		layout.addWidget(self.edit_name_serie)
		layout.addWidget(self.chkbox_first_col)
		layout.addWidget(self.chkbox_time_serie)
		layout.addWidget(self.chkbox_headers)
		layout.addSpacerItem(QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
		layout.addWidget(self.btn_go)

		self.chkbox_first_col.click()

		self.setFixedWidth(190)
		self.setLayout(layout)

	def paintEvent(self, event):
		painter = QtGui.QPainter()
		painter.begin(self)
		self.paint(painter, event.rect())
		painter.end()
		return

	def paint(self, painter, area):
		painter.setBrush(QtGui.QColor(255, 255, 255, 255))
		painter.setPen(QtGui.QColor(127, 127, 127, 255))
		painter.fillRect(area, QtGui.QColor(255, 255, 255, 255))
		return


class SeriesSourceConfig(QtWidgets.QTabWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.parent = parent
		self.tf_tab = TransferFunctionConfig(self)
		self.file_config_tab = FileConfig(self)
		self.serial_config_tab = SerialConfig(self)
		self.python_script_tab = PythonScriptRunner(self)

		self.addTab(self.tf_tab, 'Função Transferência')
		self.addTab(self.file_config_tab, 'Arquivo')
		self.addTab(self.serial_config_tab, 'Serial')
		self.addTab(self.python_script_tab, 'Script Python')

		self.currentChanged.connect(self.chk_tab)

		self.chk_tab(self.currentIndex())

		self.setFixedHeight(180)
		self.setFixedWidth(350)
		return

	def chk_tab(self, index):
		#pprint(index)
		obj = self.parent.ds_layout_config
		if index == 3 or index == 0: # Python Script
			obj.chkbox_headers.hide()
			obj.chkbox_first_col.hide()
			obj.chkbox_time_serie.hide()
		else:
			obj.chkbox_headers.show()
			obj.chkbox_first_col.show()
			obj.chkbox_time_serie.show()
		return
		

class TransferFunctionConfig(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		lbl_num = QtWidgets.QLabel('num')
		lbl_den = QtWidgets.QLabel('den')
		lbl_k = QtWidgets.QLabel('Ganho <i>K</i> da entrada')
		lbl_x0 = QtWidgets.QLabel('Condição inicial da saída')
		lbl_obs = QtWidgets.QLabel('OBS: Funções de transferência serão multiplicadas na ordem mostrada na lista.')
		self.edit_num = QtWidgets.QLineEdit()
		self.edit_den = QtWidgets.QLineEdit()
		self.edit_k = QtWidgets.QLineEdit()
		self.edit_x0 = QtWidgets.QLineEdit()
		self.btn_add = QtWidgets.QPushButton('Adicionar função')
		self.btn_remove = QtWidgets.QPushButton('-')
		self.btn_move_up = QtWidgets.QPushButton()
		self.btn_move_down = QtWidgets.QPushButton()
		self.list_tf = QtWidgets.QListWidget()
		icon_up = QtGui.QIcon('./icons/arrow_up.png')
		icon_down = QtGui.QIcon('./icons/arrow_down.png')

		self.btn_move_up.setIcon(icon_up)
		self.btn_move_down.setIcon(icon_down)

		self.btn_move_up.setMaximumWidth(20)
		self.btn_move_down.setMaximumWidth(20)
		self.btn_remove.setMaximumWidth(20)
		self.btn_move_up.setMaximumHeight(20)
		self.btn_move_down.setMaximumHeight(20)
		self.btn_remove.setMaximumHeight(20)
		#self.edit_k.setFixedWidth(50)
		lbl_num.setMargin(2)
		lbl_den.setMargin(2)
		lbl_obs.setMargin(2)
		lbl_k.setMargin(2)
		lbl_obs.setWordWrap(True)
		self.edit_num.setFixedWidth(100)
		self.edit_den.setFixedWidth(100)
		#self.list_tf.setMaximumHeight(100)

		self.btn_add.clicked.connect(self.add_function)
		self.btn_remove.clicked.connect(self.remove_function)

		layout_func = QtWidgets.QGridLayout()
		layout_func.addWidget(lbl_num, 0, 0)
		layout_func.addWidget(lbl_den, 1, 0)
		layout_func.addWidget(self.edit_num, 0, 2)
		layout_func.addWidget(self.edit_den, 1, 2)

		layout_bottom = QtWidgets.QGridLayout()
		layout_bottom.addWidget(lbl_k, 0, 0)
		layout_bottom.addWidget(self.edit_k, 0, 1)
		layout_bottom.addWidget(lbl_x0, 1, 0)
		layout_bottom.addWidget(self.edit_x0, 1, 1)

		layout_add_func = QtWidgets.QVBoxLayout()
		layout_add_func.addLayout(layout_func)
		layout_add_func.addWidget(self.btn_add)
		layout_add_func.addLayout(layout_bottom)
		layout_add_func.setAlignment(QtCore.Qt.AlignCenter)

		layout_ctrl = QtWidgets.QVBoxLayout()
		layout_ctrl.addWidget(self.btn_move_up)
		layout_ctrl.addWidget(self.btn_move_down)
		layout_ctrl.addWidget(self.btn_remove)
		layout_ctrl.setAlignment(QtCore.Qt.AlignBottom)
		layout_ctrl.setSpacing(1)

		layout_config = QtWidgets.QHBoxLayout()
		layout_config.addLayout(layout_add_func)
		layout_config.addWidget(self.list_tf)
		layout_config.addLayout(layout_ctrl)

		layout = QtWidgets.QVBoxLayout()
		layout.addLayout(layout_config)
		#layout.addWidget(lbl_obs)

		self.setLayout(layout)

	def remove_function(self):
		if self.list_tf.currentItem() is None:
			return
		self.list_tf.takeItem(self.list_tf.currentRow())
		return

	def add_function(self):
		num = self.edit_num.text().strip()
		den = self.edit_den.text().strip()
		if num == '' or den == '': return

		num = num.replace('[', '')
		num = num.replace(']', '')
		num = num.replace(',', ' ')
		num = num.strip()

		den = den.replace('[', '')
		den = den.replace(']', '')
		den = den.replace(',', ' ')
		den = den.strip()

		nums = num.split(' ')
		dens = den.split(' ')

		if len(nums) == len(dens) and len(nums) == 1:
			self.edit_num.setText('')
			self.edit_den.setText('')
			return

		formatted_nums = '['
		for n in nums:
			if n != '': formatted_nums += str(n) + ' '
		if (len(formatted_nums) > 2): formatted_nums = formatted_nums[:-1]
		formatted_nums += ']'

		formatted_dens = '['
		for d in dens:
			if d != '': formatted_dens += str(d) + ' '
		if (len(formatted_dens) > 2): formatted_dens = formatted_dens[:-1]
		formatted_dens += ']'

		self.list_tf.addItem(formatted_nums + '\t' + formatted_dens)
		self.edit_num.setText('')
		self.edit_den.setText('')

		return


class SerialConfig(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.lbl_porta = QtWidgets.QLabel('Porta')
		self.edit_porta = QtWidgets.QLineEdit()
		self.list_porta = QtWidgets.QListWidget()
		self.lbl_br = QtWidgets.QLabel('Baud Rate')
		self.edit_br = QtWidgets.QLineEdit()
		self.list_br = QtWidgets.QListWidget()
		self.lbl_timeout = QtWidgets.QLabel('Timeout (ms)')
		self.edit_timeout = QtWidgets.QLineEdit()
		self.btn_check_connection = QtWidgets.QPushButton('Testar')

		self.edit_porta.setText('COM 3')
		self.edit_br.setText('9600')
		self.edit_timeout.setText('5000')
		self.list_porta.addItems(['COM '+str(i+1) for i in range(6)])
		self.list_br.addItems([str(9600+i*1600) for i in range(7)])

		self.edit_porta.setMaximumWidth(100)
		self.list_porta.setMaximumWidth(100)
		self.edit_br.setMaximumWidth(100)
		self.list_br.setMaximumWidth(100)
		self.edit_timeout.setMaximumWidth(80)

		self.list_porta.itemClicked.connect(self.overwrite_porta)
		self.list_br.itemClicked.connect(self.overwrite_br)
		self.btn_check_connection.clicked.connect(self.test_connection)

		layout = QtWidgets.QGridLayout(self)
		layout.addWidget(self.lbl_porta, 0, 0)
		layout.addWidget(self.edit_porta, 1, 0)
		layout.addWidget(self.list_porta, 2, 0)
		layout.addWidget(self.lbl_br, 0, 2)
		layout.addWidget(self.edit_br, 1, 2)
		layout.addWidget(self.list_br, 2, 2)
		layout.addWidget(self.lbl_timeout, 0, 4)
		layout.addWidget(self.edit_timeout, 1, 4)
		layout.addWidget(self.btn_check_connection, 2, 4, alignment=QtCore.Qt.AlignBottom)

		layout.setColumnMinimumWidth(1, 10)
		layout.setColumnMinimumWidth(3, 10)

		self.setLayout(layout)
		return

	def overwrite_porta(self, item):
		self.edit_porta.setText(item.text())
		return

	def overwrite_br(self, item):
		self.edit_br.setText(item.text())
		return

	def test_connection(self):
		desc = ''
		try:
			if not self.edit_br.text().isnumeric():
				desc = 'Baud Rate inválido, certifique-se que se trata de um número.'
				raise Exception
			if self.edit_br.text() == '' or self.edit_porta.text() == '' or self.edit_timeout.text() == '':
				desc = 'Um ou mais parametros estão vazio. Certifique-se de preencher todos os campos'
				raise Exception

			with serial.Serial(self.edit_porta.text(), self.edit_br.text(),\
				timeout=int(self.edit_timeout.text())) as porta_teste:
				if porta_teste.is_open:
					desc = 'Porta serial está correta, mas já iniciou uma comunicação. Certifique-se que nenhuma ' \
					'outra aplicação está utilizando esta porta. (Ex: Serial Monitor / Plotter da IDE Arduino)'
					raise Exception

			desc = 'Conexão realizada com sucesso!'
			message_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'All Good!', desc, QtWidgets.QMessageBox.StandardButton.Ok)
		except Exception as exc:
			if desc == '':
				desc = str(exc)
			message_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 'Warning!', desc, QtWidgets.QMessageBox.StandardButton.Ok)
		message_box.setFixedWidth(400)
		message_box.setFixedHeight(100)
		message_box.exec_()
		return

class FileConfig(QtWidgets.QWidget):
	file_path = ''

	def __init__(self, parent=None):
		super().__init__(parent)

		lbl_file = QtWidgets.QLabel('Arquivo')
		lbl_directory = QtWidgets.QLabel('Diretório')
		self.edit_file = QtWidgets.QLineEdit()
		self.edit_directory = QtWidgets.QLineEdit()
		self.btn_file_dialog = QtWidgets.QPushButton('...')
		self.btn_csv = QtWidgets.QRadioButton('.csv')
		self.btn_tsv = QtWidgets.QRadioButton('.tsv')
		self.btn_xls = QtWidgets.QRadioButton('.xls')
		self.btn_xlsx = QtWidgets.QRadioButton('.xlsx')

		self.btn_file_dialog.setFixedWidth(25)
		self.btn_file_dialog.setFixedHeight(22)
		self.btn_csv.click()

		self.btn_file_dialog.clicked.connect(self.open_file_dialog)
		self.btn_xls.clicked.connect(self.clear_contents)
		self.btn_xlsx.clicked.connect(self.clear_contents)
		self.btn_csv.clicked.connect(self.clear_contents)
		self.btn_tsv.clicked.connect(self.clear_contents)
		
		layout_btns = QtWidgets.QHBoxLayout()
		layout_btns.addWidget(self.btn_csv)
		layout_btns.addWidget(self.btn_tsv)
		layout_btns.addWidget(self.btn_xls)
		layout_btns.addWidget(self.btn_xlsx)

		layout_directory = QtWidgets.QHBoxLayout()
		layout_directory.addWidget(lbl_directory)
		layout_directory.addWidget(self.edit_directory)

		layout_file = QtWidgets.QHBoxLayout()
		layout_file.addWidget(lbl_file)
		layout_file.addWidget(self.edit_file)
		layout_file.addWidget(self.btn_file_dialog)
		
		layout = QtWidgets.QVBoxLayout()
		layout.addLayout(layout_btns)
		layout.addLayout(layout_directory)
		layout.addLayout(layout_file)

		self.setLayout(layout)
		return

	def clear_contents(self):
		self.edit_directory.setText('')
		self.edit_file.setText('')
		return

	def open_file_dialog(self):
		caption = 'Selecione um arquivo'
		directory = 'C://'
		if self.btn_csv.isChecked(): file_filter = 'Comma Separated Values (*.csv)'
		if self.btn_tsv.isChecked(): file_filter = 'Tab Separated Values (*.tsv)'
		if self.btn_xls.isChecked(): file_filter = 'Old Excel Files (*.xls)'
		if self.btn_xlsx.isChecked(): file_filter = 'Modern Excel Files (*.xlsx)'

		fd = QtWidgets.QFileDialog(self, caption, directory, file_filter)
		fd.setFileMode(QtWidgets.QFileDialog.ExistingFile)

		file_path = ''
		if fd.exec():
			file_path = fd.selectedFiles()[0]
		self.update_file(file_path)
		return

	def update_file(self, path):
		file = path.split('/')[-1]
		self.edit_directory.setText(path.replace(file, ''))
		self.edit_file.setText(file)
		self.file_path = path
		return

class ScriptEditor(QtWidgets.QTextEdit):
	def __init__(self):
		super().__init__()

	def mouseDoubleClickEvent(self, event):
		#print('click')
		dialog = ScriptEditorDialog(text=self.toPlainText())
		if dialog.exec_():
			self.setPlainText(dialog.text_editor.toPlainText())
		return


class PythonScriptRunner(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__()

		lbl_script = QtWidgets.QLabel('Digite seu script abaixo (double-click para expandir)')
		lbl_obs = QtWidgets.QLabel('Escreva um script simples, <b>sem cabeçalho de função</b>. \
			Inclua um <i>return</i> [lista_de_series], [serie_temporal], [lista_de_nomes].\n \
			Caso tudo corra bem, aparecerá uma caixa diálogo com a série criada.')
		self.edit_script = ScriptEditor()

		self.edit_script.setPlaceholderText('t = range(50) \
			\nseries = [[i*0.2 for i in t], [i*0.25 for i in t]] \
			\nheaders = ["Reta Inclinada", "Reta + Inclinada"] \
			\nreturn series, t, headers')

		lbl_obs.setWordWrap(True)

		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(lbl_script)
		layout.addWidget(self.edit_script)
		layout.addWidget(lbl_obs)

		self.setLayout(layout)


class MainWidget(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)

		nSeries = 0

		self.main_plot_area = MainPlotArea(parent=self)
		self.plot_manager = PlotManager(parent=self, plot_object=self.main_plot_area)
		self.ds_config = DatasetConfig(parent=self)

		layout_left = QtWidgets.QVBoxLayout()
		layout_left.addWidget(self.ds_config)
		layout_left.addWidget(self.main_plot_area)

		layout = QtWidgets.QHBoxLayout()
		layout.addLayout(layout_left)
		layout.addWidget(self.plot_manager)

		#self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		self.setMinimumSize(QtCore.QSize(1000,600))

		self.setLayout(layout)
		return