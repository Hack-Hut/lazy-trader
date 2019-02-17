from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QMessageBox, QPushButton, QMainWindow, QWidget, QApplication, QVBoxLayout, QTableWidgetItem, QAction



class All:

	"""
	Used for the all trades tab
	"""
	
	def __init__(self, dict_list):
		self.data = dict_list
		self.create_table()

	def create_table(self):
		self.tableWidget = QtWidgets.QTableWidget()
		self.tableWidget.setRowCount(4)
		self.tableWidget.setColumnCount(2)
		self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
		self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
		self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
		self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
		self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
		self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
		self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
		self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
		self.tableWidget.move(0,0)
		print(self.tableWidget)
		return self.tableWidget