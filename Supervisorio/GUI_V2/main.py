import objects.form_objects as objs
import objects.realtime_objects as rtobjs
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

main_window = QtWidgets.QMainWindow()
main_window.setWindowTitle('Supervisorio Didatico')

central_widget = objs.MainWidget()
main_window.setCentralWidget(central_widget)
main_window.show()

app.exec_()