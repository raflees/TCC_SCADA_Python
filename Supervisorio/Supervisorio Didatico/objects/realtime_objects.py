import _thread
from PyQt5 import QtWidgets, QtCore, QtGui, QtChart
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import numpy as np
import serial
import time
import simple_pid
import controlpy
import math

class SCADADialog (QtWidgets.QDialog):
	to_be_plotted = []
	fetch = True
	update = True
	porta = None

	def __init__(self, porta='COM3', baud_rate=9600, timeout=1, nInputs=3, labels = []):
		super().__init__()
		self.figure = plt.figure(tight_layout=True)
		self.canvas = FigureCanvas(self.figure)
		self.btn_close = QtWidgets.QPushButton('Cancelar')
		self.btn_stop = QtWidgets.QPushButton('Parar')
		self.btn_create = QtWidgets.QPushButton('Criar Série')

		self.plotted = []
		self.to_be_plotted = []
		for i in range(nInputs):
			self.plotted.append([],)
			self.to_be_plotted.append([],)
		self.nInputs = nInputs
		self.labels = labels

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

		ax = self.figure.gca()
		ax.yaxis.tick_right()

		self.scan_time = 0.2
		self.update_time = 1
		self.lock = False

		try:
			self.setup_connection(porta, baud_rate, timeout)
		except Exception as exc:
			message_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 'Warning!', str(exc), QtWidgets.QMessageBox.StandardButton.Ok)
			return

		if self.porta == None:
			print('Nao foi possivel estabelecer conexao')
			return
		else:
			self.setup_control()
			_thread.start_new_thread(self.fetch_data, ())
			_thread.start_new_thread(self.update_canvas, ())
		return

	def fetch_data(self):
		t0 = time.time()

		while self.fetch:
			new_data = []

			test = []
			while self.porta.inWaiting() > 0:
				line = self.porta.readline().decode()
				test = [float(data.replace('\r', '').replace('\n', '')) for data in line.split('\t') if isFloat(data)]# else np.nan 
				#print(test)
				new_data.append(test)

			if len(test) == self.nInputs:
				self.loop_control([test[1], test[2]])

				new_data = list(np.array(new_data).transpose())

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
			else:
				pass
				#print('Wrong number of inputs ({0})'.format(len(test)))

			time_left = self.scan_time - (time.time() - t0)/1000
			if time_left > 0:
				time.sleep(self.scan_time)
		return

	def update_canvas(self):
		t_max = 0
		t0 = time.time()
		ax = self.figure.gca()

		while self.update:
			if self.to_be_plotted != []:
				while self.lock:
					pass

				try:
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
					#print('Max: {}'.format(t_max))
					ax = self.figure.gca()
					for i, serie in enumerate(series):
						ax.plot(time_serie, serie)
					ax.legend(self.labels)
				except:
					pass

			ax.set_xlabel('Tempo')
			ax.set_ylabel('Valor da Variável')
			self.canvas.draw()
			
			time_left = self.update_time - (time.time() - t0)/1000
			#print(time_left)
			if time_left > 0:
				time.sleep(self.update_time)
		return

	def rejected():
		self.fetch = False
		self.update = False
		return

	def stop_logging(self):
		self.update = False
		self.fetch = False
		time.sleep(max(self.update_time, self.scan_time))
		if self.porta.isOpen():
			self.porta.close()
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
		if self.porta.isOpen():
			self.porta.close()
		time.sleep(timeout)

		n_tries = 0
		if not self.porta.isOpen():
			print('Abrindo porta Serial')
			self.porta.open()
		self.porta.reset_input_buffer()
		time.sleep(2)
		while self.porta.inWaiting() == 0 and n_tries < 100:
			print('Escrevendo na porta')
			self.porta.write('go'.encode('UTF-8'))
			n_tries += 1
			time.sleep(2)
		if n_tries == 100:
			print('O dispositivo não respondeu ao sinal emitido...')
		return

	def setup_control(self):
		self.pids = []
		self.pids.append(simple_pid.PID(0.1067, 0.0067, setpoint=2.5))#, output_limits=(0, 1)))
		self.pids.append(simple_pid.PID(0.1067, 0.0067, setpoint=2.5))#, output_limits=(0, 1)))
		'''A = np.matrix([[-0.063, 0.046],[-0.063, 0]])
		B = np.matrix([[0.937, 0],[0, 0.937]])
		R = np.matrix([[0.5, 0],[0, 0.5]])
		Q = np.matrix([[2, 0],[0, 2]])
		K, P, V = controlpy.synthesis.controller_lqr(A, B, Q, R)
		self.K = K.tolist()'''
		rho = 1000
		g = 9.8
		k = 0.001

		self.sp_h1 = 1
		self.sp_h2 = 1
		self.sp_u1 = 0
		self.sp_u2 = k*math.sqrt(rho*g)

		self.pids = []
		self.pids.append(simple_pid.PID(0.1067, 0.0067, setpoint= 2.5 - self.sp_h1))#, output_limits=(0, 1)))
		self.pids.append(simple_pid.PID(0.1067, 0.0067, setpoint= 2.5 - self.sp_h1))#, output_limits=(0, 1)))

		'''print('Matriz dos ganhos')
		print(self.K)
		print('Leis de controle (em desvio):')
		print('u1 = -({:.2f}*h1 + {:.2f}*h2)'.format(self.K[0][0], self.K[0][1]))
		print('u2 = -({:.2f}*h1 + {:.2f}*h2)'.format(self.K[1][0], self.K[1][1]))'''
		return

	def loop_control(self, input_data):
		if len(input_data) == 0:
			print('No Read')
			return

		input_data[0] = input_data[0] - self.sp_h1
		input_data[1] = input_data[1] - self.sp_h2
		signals = [self.pids[i](input_value) for i, input_value in enumerate(input_data)]
		signals[0] = signals[0] + self.sp_u1
		signals[1] = signals[1] + self.sp_u2
		''' = 	[-(input_data[0]*self.K[0][0] + input_data[1]*self.K[0][1]) + self.sp_u1,
					-(input_data[0]*self.K[1][0] + input_data[1]*self.K[1][1]) + self.sp_u2]'''
		for signal in signals:
			resp = '{:.3f}'.format(float(signal)/10).encode('UTF-8')
			self.porta.write(resp)

		print('Got {}'.format(['{:.2f}'.format(data).encode('UTF-8') for data in input_data]))
		print('Sent {}'.format(['{:.2f}'.format(sig).encode('UTF-8') for sig in signals]))
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
