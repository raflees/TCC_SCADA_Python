import _thread
from PyQt5 import QtWidgets, QtCore, QtGui, QtChart
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import numpy as np
import time

f = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
s = [[5, 6], [6, 7], [7, 8], [8, 9]]

to_be_plotted = []

def fetch_data(scan_time):
		t0 = time.time()

		while time.time()-t0 < 10:
			print('Fetching Data...')
			new_data = []
			for i in range(int(np.random.rand()*10)):
				#new_data.append([time.time()-t0, np.random.rand(), np.random.rand(), np.random.rand()],)
				new_data.append([time.time()-t0, 1, 2, 3],)
				time.sleep(0.1)
			new_data = list(np.array(new_data).transpose())
			print('New Data: ')
			print(new_data)
			i = 0
			if not new_data == []:
				for i in range(len(to_be_plotted)):
					for elem in new_data[i]:
						to_be_plotted[i] = np.append(to_be_plotted[i], elem)
					new_data[i] = []
				for left in new_data:
					if not left == []:
						to_be_plotted.append(left) 
			time.sleep(scan_time)
		return

fetch_data(2)
