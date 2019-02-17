try:
	from gui import Ui_LazyTrader
	import sys
	import qdarkgraystyle
	from PyQt5 import QtGui, QtCore
	from PyQt5.QtWidgets import QTableWidget,QMessageBox, QPushButton, QMainWindow, QWidget, QApplication, QVBoxLayout, QTableWidgetItem, QAction
	from PyQt5.QtGui import QIcon
	from PyQt5.QtCore import pyqtSlot
	from PyQt5 import QtCore, QtGui, QtWidgets

except Exception as e:
	raise e
	print("Please Use Python3")
	exit()


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkgraystyle.load_stylesheet())
	LazyTrader = QtWidgets.QMainWindow()
	ui = Ui_LazyTrader()
	ui.setupUi(LazyTrader)
	LazyTrader.show()
	sys.exit(app.exec_())
