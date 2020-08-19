from PyQt5 import QtWidgets, QtGui, QtCore
import matplotlib.pyplot as plt
import sys
import numpy as np

def main():
	app = QtWidgets.QApplication(sys.argv)
	main_window = QtWidgets.QMainWindow()

	central_widget = GroupMainWidget()

	main_window.setCentralWidget(central_widget)

	main_window.show()
	sys.exit(app.exec_())

class GroupMainWidget(QtWidgets.QGroupBox):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setTitle('Im a title!')

		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(MyButton('Button 1'))
		layout.addWidget(MyButton('Button 2'))
		layout.addWidget(MyButton('Button 3'))
		self.setLayout(layout)

	def paintEvent(self, event):
		painter = QtGui.QPainter()
		painter.begin(self)
		#self.drawBackground(painter, event.rect())
		painter.end()

	def drawBackground(self, painter, rect):
		painter.setBrush(QtGui.QColor(0, 0, 255, 127))
		painter.fillRect(rect, painter.brush())

class MyButton(QtWidgets.QPushButton):
	def __init__(self, text, parent=None):
		super().__init__(parent)

		self.color = QtGui.QColor(np.random.rand()*255, 0, 0, 127)
		self.text = text

		self.setText(text)


	def paintEvent(self, event):
		painter = QtGui.QPainter()
		painter.begin(self)
		#self.drawBackground(painter, event.rect())
		painter.end()

	def drawBackground(self, painter, rect):
		painter.setBrush(self.color)
		painter.fillRect(rect, painter.brush())
		painter.drawText(rect, QtCore.Qt.AlignCenter, self.text)
		self.created = 0

if __name__ == '__main__':
	main()