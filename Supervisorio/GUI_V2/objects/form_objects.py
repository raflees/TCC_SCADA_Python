from PyQt5 import QtWidgets, QtCore, QtGui, QtChart
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import numpy as np
import serial
import time

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

class SeriesConfig(QtWidgets.QTabWidget):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.addTab(TransferFunctionConfig(), 'Função Transferência')
		self.addTab(FileConfig(), 'Arquivo')
		self.addTab(SerialConfig(), 'Serial')

		self.setFixedHeight(180)
		self.setFixedWidth(350)
		return

class TransferFunctionConfig(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		lbl_num = QtWidgets.QLabel(' num')
		lbl_den = QtWidgets.QLabel(' den')
		self.edit_num = QtWidgets.QLineEdit()
		self.edit_den = QtWidgets.QLineEdit()
		self.list_tf = QtWidgets.QListWidget()
		self.btn_add = QtWidgets.QPushButton('Adicionar função')
		self.btn_remove = QtWidgets.QPushButton('-')
		self.btn_move_up = QtWidgets.QPushButton()
		self.btn_move_down = QtWidgets.QPushButton()
		lbl_obs = QtWidgets.QLabel('OBS: A dimensão do numerador não pode ultrapassar a do denominador. Funções de transferência serão multiplicadas na ordem mostrada na lista. Configure a entrada no botão ''Editar'' na lista de séries à direita após sua inclusão.')
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
		lbl_obs.setWordWrap(True)
		self.edit_num.setFixedWidth(100)
		self.edit_den.setFixedWidth(100)

		layout_func = QtWidgets.QGridLayout()
		layout_func.addWidget(lbl_num, 0, 0)
		layout_func.addWidget(lbl_den, 1, 0)
		layout_func.addWidget(self.edit_num, 0, 2)
		layout_func.addWidget(self.edit_den, 1, 2)

		layout_add_func = QtWidgets.QVBoxLayout()
		layout_add_func.addLayout(layout_func)
		layout_add_func.addWidget(self.btn_add)
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
		layout.addWidget(lbl_obs)
		#layout.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))

		self.setLayout(layout)

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

class MainWidget(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)

		nSeries = 0

		main_plot_area = MainPlotArea()

		layout_left = QtWidgets.QVBoxLayout()
		layout_left.addWidget(SeriesConfig())
		layout_left.addWidget(main_plot_area)

		layout = QtWidgets.QHBoxLayout()
		layout.addLayout(layout_left)
		layout.addWidget(PlotManager(main_plot_area))

		#self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		self.setMinimumSize(QtCore.QSize(1000,600))

		self.setLayout(layout)
