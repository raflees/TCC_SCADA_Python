import _thread
from PyQt5 import QtWidgets, QtCore, QtGui, QtChart
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import numpy as np
import serial
import time

class SCADADialog (QtWidgets.QDialog):
	to_be_plotted = []
	fetch = True
	update = True
	porta = None

	def __init__(self, qtd_x, porta='COM3', baud_rate=9600, timeout=1):
		super().__init__()
		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		self.btn_close = QtWidgets.QPushButton('Cancelar')
		self.btn_stop = QtWidgets.QPushButton('Parar')
		self.btn_create = QtWidgets.QPushButton('CriarSerie')

		self.plotted = []
		for i in range(qtd_x):
			self.plotted.append([],)

		self.btn_close.clicked.connect(self.close)
		self.btn_stop.clicked.connect(self.stop_logging)
		self.btn_create.clicked.connect(self.export_serie)

		layout_buttons = QtWidgets.QHBoxLayout()
		layout_buttons.addWidget(self.btn_close)
		layout_buttons.addWidget(self.btn_stop)
		layout_buttons.addWidget(self.btn_create)
		layout_buttons.setAlignment(QtCore.Qt.AlignRight)

		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(self.canvas)
		layout.addLayout(layout_buttons)

		self.setLayout(layout)

		scan_time = 0.5
		update_time = 1
		self.lock = False

		self.setup_connection(porta, baud_rate, timeout)
		if self.porta == None:
			print('Nao foi possivel estabelecer conexao')
			return
		else:
			_thread.start_new_thread(self.fetch_data, (scan_time,))
			_thread.start_new_thread(self.update_canvas, (update_time,))
		return

	def fetch_data(self, scan_time):
		t0 = time.time()

		while self.fetch:
			print('Fetching Data...')
			new_data = []

			# for i in range(int(np.random.rand()*10)):
			# 	new_data.append([time.time()-t0, np.random.rand(), np.random.rand(), np.random.rand()],)
			# 	#new_data.append([time.time()-t0, 1, 2, 3],)
			# 	time.sleep(0.1)
			# new_data = list(np.array(new_data).transpose())

			while self.porta.inWaiting() > 0:
				line = self.porta.readline().decode()
				test = [float(data.replace('\r', '').replace('\n', '')) for data in line.split('\t')]#if isFloat(data) else np.nan 
				#print(test)
				new_data.append(test)
			new_data = list(np.array(new_data).transpose())

			print(new_data)

			i = 0
			if not new_data == []:
				while self.lock:
					time.sleep(0.05)
				self.lock = True
				for i in range(len(self.to_be_plotted)):
					for elem in new_data[i]:
						self.to_be_plotted[i] = np.append(self.to_be_plotted[i], elem)
					new_data[i] = []
				for left in new_data:
					if not left == []:
						self.to_be_plotted.append(left)
				self.lock = False 
			time.sleep(scan_time)
		return

	def update_canvas(self, update_time):
		t_max = 0

		while self.update:
			if self.to_be_plotted == []:
				print ('Empty!')
			else:
				print('Updating Canvas...')

				while self.lock: pass
				self.lock = True

				for i in range(len(self.plotted)):
					for elem in self.to_be_plotted[i]:
						self.plotted[i] = np.append(self.plotted[i], elem)

				self.to_be_plotted = []
				self.lock = False

				time_serie = self.plotted[0]
				series = self.plotted[1:]

				self.figure.clear()
				try:
					t_max = time_serie[-1]
					if t_max > 20:
						plt.xlim([t_max-20, t_max])
					else:
						plt.xlim([0, t_max])
				except:
					t_max = 0
				print('Max: {}'.format(t_max))
				ax = self.figure.gca()
				for serie in series:
					ax.plot(time_serie, serie)
			self.canvas.draw()
			time.sleep(update_time)
		return

	def rejected():
		self.fetch = False
		self.update = False
		return

	def stop_logging(self):
		self.update = False
		self.fetch = False
		return

	def export_serie(self):
		if (self.update and self.fetch):
			return

		self.update = False
		self.fetch = False
		self.series = self.plotted[1:]
		self.time_serie = self.plotted[0]
		self.accept()
		return

	def setup_connection(self, porta, baud_rate, timeout):
		#try:
		print('Tentando conexao')
		self.porta = serial.Serial(porta, baud_rate, timeout=timeout)
		time.sleep(timeout)

		# except Exception:
		# 	print(Exception)
		# 	self.porta = None
		# 	return

		n_tries = 0
		if not self.porta.isOpen():
			print('Abrindo porta Serial')
			self.porta.open()
		while self.porta.inWaiting() == 0 and n_tries < 100:
			print('Escrevendo na porta')
			self.porta.write(chr(97).encode('UTF-8'))
			n_tries += 1
		return

	def input_function(self):

		return

def isFloat(string):
	try:
		float(string)
		return True
	except:
		return False

class Window4Dialog(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		dialog = SCADADialog(4)
		dialog.exec_()
		dialog.fetch = False
		dialog.update = False
