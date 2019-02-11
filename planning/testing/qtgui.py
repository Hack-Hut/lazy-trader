from PyQt5 import QtGui, QtCore
import qdarkgraystyle
import sys
from PyQt5.QtWidgets import QTableWidget,QMessageBox, QPushButton, QMainWindow, QWidget, QApplication, QVBoxLayout, QTableWidgetItem, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import datetime

GREY = "#313133"
WHITE = "#e2e2e2"

class Window(QMainWindow, QWidget):
	def __init__(self):
		super(Window, self).__init__()
		# x,y,w,h
		self.setGeometry(1920,1080,1920,1080) # main
		self.setWindowTitle("./Lazy-Trader")
		self.createTable()	
		self.layout = QVBoxLayout()		
		self.layout.addWidget(self.tableWidget) 
		self.setLayout(self.layout)
		self.update_status_bar()
		self.home()
		self.show()
 

	def update_status_bar(self, message="Last updated:\t", time=True):
		if time:
			display = str(message) + str(datetime.datetime.now())
		else:
			display = message
		self.statusBar().showMessage(display)


	def home(self):
		btnQuit = NewBtn.create(self, "Quit")
		btnQuit.clicked.connect(self.close_application)
		btnQuit.move(10,60)
		
		btnUpdate = NewBtn.create(self, "Update")
		btnUpdate.move(10,10)
		btnUpdate.clicked.connect(self.update_status_bar)

		# Creating multipl buttons 
		# for x in range(0, 15):
		# 	btnTemp = NewBtn.create(self, "button_" + str(x))
		# 	btnTemp.move(10,(50 * x))
		# 	btnTemp.clicked.connect(lambda: self.print_test(x))



	def createTable(self):
		self.tableWidget = QTableWidget()
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

		# table selection change
		self.tableWidget.doubleClicked.connect(self.on_click)

		
	@pyqtSlot()
	def on_click(self):
		print("\n")
		for currentQTableWidgetItem in self.tableWidget.selectedItems():
			print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

	def print_test(self, x):
		print(x)

	def download(self):
		self.completed = 0	
		while self.completed < 100:
			self.completed += 0.0001
			self.progress.setValue(self.completed)


	def close_application(self):
		# Yes No pop up 
		choice = QMessageBox.question(self, "extract!", "Quit?", QMessageBox.Yes | QMessageBox.No)
		if choice == QMessageBox.Yes:
			print("Exiting")
			sys.exit()


class NewBtn(QMainWindow):
	def __inti__(self):
		pass

	def create(self, name):
		btn = QPushButton(name, self)
		btn.setStyleSheet("background-color: " + GREY + "; color: " + WHITE )
		btn.resize(btn.sizeHint())
		return btn

def run():
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkgraystyle.load_stylesheet())
	GUI = Window()
	sys.exit(app.exec_())	

run()